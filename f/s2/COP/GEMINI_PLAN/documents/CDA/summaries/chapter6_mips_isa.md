# Chapter 6: MIPS Instruction Set Architecture (ISA)

## 1. Register File
The MIPS architecture is built around a central **Register File** that acts as the primary hardware workspace. Instructions operate heavily on these registers.

*   **Structure:** Registers are constructed from flip-flops. The MIPS architecture specifies 32 general-purpose registers, each 32 bits wide. A 32-bit entity is referred to as a \"word.\"
*   **Design Principle:** \"Smaller is faster.\" Using a limited set of 32 registers enables faster access compared to reading and writing directly to main memory, supporting high-speed execution.
*   **MIPS Software Register Convention:** Registers are numbered 0-31 and map to specific software roles:
    *   **`$zero` (0):** Hardwired to the constant `0`. It cannot be overwritten. This is heavily used to synthesize common operations (e.g., copying a register or negation).
    *   **`$at` (1):** Assembler Temporary, reserved for the assembler to construct pseudo-instructions.
    *   **`$v0-$v1` (2-3):** Used for expression evaluation and to return function/procedure results.
    *   **`$a0-$a3` (4-7):** Argument registers used to pass parameters to functions.
    *   **`$t0-$t9` (8-15, 24-25):** Temporary registers. These are *caller-saved*, meaning the callee function can use them freely without preserving their original contents.
    *   **`$s0-$s7` (16-23):** Saved registers. These are *callee-saved*, meaning if a function wants to use them, it must first push their original values to the stack and restore them before returning.
    *   **`$k0-$k1` (26-27):** Reserved for the Operating System kernel.
    *   **`$gp` (28):** Global pointer, points to the middle of a 64K block of memory in the static data segment.
    *   **`$sp` (29):** Stack pointer, points to the current \"top\" (lowest address) of the stack.
    *   **`$fp` (30):** Frame pointer, serves as a stable base for the current procedure's activation record.
    *   **`$ra` (31):** Return address register. When a procedure is called via `jal`, this register automatically stores the location to return to.
*   **Special-Purpose Registers (`Hi` and `Lo`):** Used exclusively for hardware multiplication and division.
    *   **Multiply:** Yields a 64-bit product. The upper 32 bits are stored in `Hi`, lower 32 bits in `Lo`.
    *   **Divide:** The quotient is stored in `Lo`, and the remainder is stored in `Hi`.
*   **Floating-Point Registers:** MIPS also defines a separate co-processor with 32 floating-point registers (`$f0-$f31`). These can be paired (even/odd) to handle 64-bit double-precision numbers.

---\n
## 2. Memory Layout
MIPS utilizes a structured memory layout to separate instructions, constants, dynamic allocations, and function states. 

*   **Byte-Addressed & Word-Aligned:** Memory is viewed as a large array of 8-bit bytes. Because registers are 32 bits (4 bytes), full \"word\" accesses must be **word-aligned**—meaning the starting memory address must be a multiple of 4 (e.g., 0, 4, 8, 12).
*   **Memory Segments:**
    1.  **Text Segment:** Located at lower memory addresses, this segment stores the compiled machine code (the program instructions).
    2.  **Static Data:** Stores global variables and constants that exist for the lifetime of the program (like string literals and C `static` variables). The `$gp` register is used for quick access via \u00B1 offsets.
    3.  **Dynamic Data (Heap):** Area of memory allocated dynamically at runtime (e.g., using `malloc` in C or `new` in Java). The heap grows *upwards* toward higher memory addresses.
    4.  **Stack:** Automatic storage primarily used for procedure calls to manage local variables, pass extra arguments (if more than 4), and spill registers (save `$s` registers or nested `$ra` addresses). The stack starts at a high memory address and grows *downwards* toward the heap.
*   **Stack Operations:** MIPS does not have explicit `push` or `pop` instructions. Instead, stack manipulation is done manually:
    *   **Push:** Subtract from `$sp` (e.g., `addi $sp, $sp, -4`), then store the value to memory (`sw $t0, 0($sp)`).
    *   **Pop:** Load the value from memory (`lw $t0, 0($sp)`), then add to `$sp` (`addi $sp, $sp, 4`).

---\n
## 3. MIPS Instruction Formats
MIPS adheres strictly to the RISC design principle that *simplicity favors regularity*. Therefore, **every instruction is exactly 32 bits long.** To accommodate different operational needs, MIPS uses three specific instruction layouts (formats):

### 1. R-Type (Register Format)
Used primarily for arithmetic and logical operations where all operands are contained within registers.
**Format (6 fields):** `[op: 6 bits] [rs: 5 bits] [rt: 5 bits] [rd: 5 bits] [shamt: 5 bits] [funct: 6 bits]`
*   **`op` (Opcode):** For almost all R-Type instructions, the opcode is `000000`.
*   **`rs` (Register Source):** The first source register index.
*   **`rt` (Register Target):** The second source register index.
*   **`rd` (Register Destination):** The destination register where the result is stored.
*   **`shamt` (Shift Amount):** Used only in shift instructions (like `sll` or `srl`) to indicate the number of bits to shift (0-31). For non-shift instructions, this is `00000`.
*   **`funct` (Function Code):** Since the opcode is `000000`, the `funct` field acts as an extended opcode to specify the exact operation (e.g., `add`, `sub`, `and`, `or`).

### 2. I-Type (Immediate Format)
Used for operations that involve a constant (immediate) value, load/store data transfers, and conditional branching.
**Format (4 fields):** `[op: 6 bits] [rs: 5 bits] [rt: 5 bits] [constant/address: 16 bits]`
*   **`op` (Opcode):** Uniquely identifies the instruction (e.g., `addi`, `lw`, `beq`).
*   **`rs` (Register Source):** The source register or the base register for memory accesses.
*   **`rt` (Register Target):** Acts as the destination register for arithmetic operations/loads, or a source register for branches and stores.
*   **`constant/address` (Immediate):** A 16-bit field containing a literal value or a memory/branch offset. This constraint means constants are limited; for larger 32-bit constants, instructions like `lui` (Load Upper Immediate) and `ori` are combined.

### 3. J-Type (Jump Format)
Used for long unconditional jumps and procedure calls.
**Format (2 fields):** `[op: 6 bits] [address: 26 bits]`
*   **`op` (Opcode):** Identifies the jump instruction (`j` or `jal`).
*   **`address`:** A 26-bit pseudo-direct target address.

---\n
## 4. Addressing Modes
Addressing modes define how an architecture calculates the target memory address or identifies the operands for an instruction. MIPS implements five distinct addressing modes:

1.  **Register Addressing:**
    *   The operands are entirely located in the registers specified by the instruction.
    *   *Examples:* R-Type instructions like `add $t0, $t1, $t2`.
2.  **Immediate Addressing:**
    *   One of the operands is a hardcoded constant value embedded directly within the instruction itself (the 16-bit immediate field).
    *   *Examples:* Arithmetic I-Types like `addi $t0, $t1, 100` or `andi $s0, $s1, 0xFF`.
3.  **Base Addressing (Displacement Addressing):**
    *   The effective memory address is calculated by taking the value in a specified base register (`rs`) and adding a 16-bit signed constant offset to it.
    *   *Examples:* Used in memory access instructions like `lw $t0, 32($s3)` or `sw $t1, 8($sp)`.
4.  **PC-Relative Addressing:**
    *   Used specifically for conditional branches. The target instruction address is calculated relative to the Program Counter (PC).
    *   The 16-bit address field represents an offset in *words* (not bytes). The hardware shifts this value left by 2 (multiplying by 4) and adds it to the current `PC + 4` to determine the jump destination.
    *   *Benefit:* Branches generally jump to nearby code (like loops or if/else statements). This mode allows branching up to \u00B12^15 words from the current execution point.
    *   *Examples:* `beq $s0, $s1, Label`, `bne $t0, $zero, Loop`.
5.  **Pseudodirect Addressing:**
    *   Used for unconditional jumps. To compute a full 32-bit target address, the 26-bit address field inside the J-Type instruction is first shifted left by 2 bits (creating a 28-bit word-aligned address). This 28-bit value is then concatenated with the upper 4 bits of the current `PC`.
    *   *Examples:* `j Target`, `jal Function`.