# Chapter 9: Exceptions and Interrupts

## Introduction to Unexpected Events
Handling unexpected events is a fundamental requirement for robust processor design. These events require a sudden change in the flow of control, pausing the current program to handle the underlying issue.

- **Exception**: An unexpected event that arises *within* the CPU during instruction execution. Examples include an undefined opcode, an arithmetic overflow, or a system call (syscall).
- **Interrupt**: An unexpected event originating from an *external* source, typically an I/O controller (e.g., a disk drive completing a transfer, or a hardware timer).

## Evolution of Exception Handling (VM/0 Conceptual Model)
To understand how processors handle exceptions, we observe the conceptual addition of hardware to a simple sequential processor (VM/0).

1. **Error Handling**: We add an **Overflow (OV) flip-flop** and a **NEWPC** register. Before fetching the next instruction, the CPU checks the OV flag. If it is set, the CPU bypasses the normal flow and executes the instruction at NEWPC (the error handler).
2. **Memory Protection**: To support multiple programs, we introduce a **FENCE** register to store the maximum memory boundary for a process, and an **MP (Memory Protection) flip-flop** that triggers if a memory request exceeds this bound.
3. **Privileged Instructions**: To prevent ordinary programs from altering critical hardware (like the FENCE register), a **Mode bit** is added (e.g., 0 for User, 1 for Privileged). Certain opcodes are restricted. If an unprivileged process attempts to execute them, a **PI (Privileged Instruction) flag** is set.
4. **I/O Interrupts**: By adding an **I/O flag**, an **OLDPC** register (to save the current Program Counter), and an **OLDR0** register (to save current data), the CPU can pause a program, switch to an I/O handler, and later restore the original state.
5. **Interrupt Handler Vector (IHV)**: Instead of an unmanageable array of individual flip-flops for every possible exception, systems utilize a unified structure: the Interrupt Handler Vector. This is a table in system memory containing the starting addresses of specific handler routines (e.g., Overflow Handler, Timer Handler, I/O Handler, System Call Handler).

## MIPS Exception Handling Implementation
In the MIPS architecture, exceptions and interrupts are managed by the **System Control Coprocessor (CP0)**. When an exception occurs, the processor must freeze the execution state and identify the cause.

### The Exception Program Counter (EPC)
The **Exception Program Counter (EPC)** is a special 32-bit register within CP0 used to precisely save the address of the offending (or interrupted) instruction. 
- If the exception is **restartable** (e.g., an I/O interrupt or an operating system page fault), the handler takes corrective action and uses the EPC to return execution to the exact point the program was interrupted.
- If the exception is **fatal** (e.g., an undefined opcode or memory protection violation), the program is terminated, and the operating system uses the EPC to report the exact location of the error to the user.

### The Cause and Status Registers
To determine why the exception occurred, MIPS utilizes specific registers in CP0:
- **Cause Register**: Saves an encoded indication of the exact problem. The handler reads this register to determine which specific corrective routine to execute.
- **Status Register**: Contains the operating mode, interrupt enabling flags, and diagnostic states. For instance, specific codes indicate an undefined instruction (e.g., `0000`) or an arithmetic overflow (e.g., `0180`).

### Handler Actions
When an exception is triggered, the processor automatically performs a sequence of events:
1. Reads the Cause register to identify the source.
2. Transfers control to the relevant handler routine (often utilizing the IHV).
3. The handler determines the required action.
4. If restartable, it corrects the issue and returns via the EPC. Otherwise, it terminates the process and issues an error report using the EPC.

## Exceptions in a Pipelined Datapath
In a pipelined processor, an exception is treated as another form of a **control hazard**. It disrupts the steady flow of instructions.

### Datapath Modifications
Consider an arithmetic overflow occurring during an `add` instruction that is currently in the Execution (EX) stage:
1. **Prevent State Corruption**: The datapath must immediately prevent the offending instruction from overwriting registers or memory (e.g., disabling the `RegWrite` and `MemWrite` control signals).
2. **Complete Previous Instructions**: Instructions that entered the pipeline *before* the offending instruction (those in the MEM and WB stages) are allowed to safely complete their execution.
3. **Flush the Pipeline**: The offending `add` instruction and all subsequent instructions behind it (in the IF and ID stages) are flushed from the pipeline.
4. **Record State**: The hardware sets the `Cause` and `EPC` register values.
5. **Transfer Control**: The PC is updated to the address of the exception handler.

This process is mechanically similar to handling a mispredicted branch, and modern processors reuse much of the same flushing and multiplexing hardware for both tasks.

### Precise vs. Imprecise Exceptions
Because pipelining overlaps the execution of multiple instructions, it is highly possible for multiple exceptions to occur within the exact same clock cycle.
- **Precise Exceptions**: MIPS handles this by dealing with the exception originating from the *earliest* instruction in the logical program order (the instruction furthest along in the pipeline). 
- Any subsequent instructions in the pipeline, even if they also generated exceptions, are simply flushed. This ensures the processor state remains perfectly consistent, allowing the program to be accurately restarted or debugged sequentially.