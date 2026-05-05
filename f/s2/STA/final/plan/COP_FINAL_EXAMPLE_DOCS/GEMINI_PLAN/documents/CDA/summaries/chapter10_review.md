# Chapter 10: Midterm & Final Synthesis

## Overview
This document provides a comprehensive review of key Computer Organization and Design (CDA) concepts, ranging from low-level binary conversions and combinational logic design to the complete MIPS processor datapath. It also serves as the ultimate synthesis by detailing the requirements and implementation of a MIPS processor simulator in C (the `spimcore` project).

## Part 1: Midterm Review & Core Concepts

### 1. Binary Conversions & Representations
*   **Unsigned Integers:** Represented using the standard positional weighted sum.
    *   *Example:* $(1100\ 1111)_2 = 128 + 64 + 8 + 4 + 2 + 1 = 207_{10}$
*   **Decimal to Binary (Unsigned):** Successive division by 2, where remainders form the binary digits (least significant bit first).
    *   *Example:* $55_{10} \rightarrow 55/2 = 27$ r $1 \rightarrow (0011\ 0111)_2$
*   **2's Complement (Signed Integers):** The most significant bit (MSB) carries a negative weight. It is used to represent both positive and negative values.
    *   *Example (Binary to Decimal):* $(1100\ 1111)_2$ has a sign bit of 1 (negative). Inverting the bits gives $(0011\ 0000)_2$, and adding 1 gives $(0011\ 0001)_2 = 49_{10}$. Therefore, the original value is $-49_{10}$.
    *   *Example (Decimal to Binary):* To represent $-55_{10}$, first convert $+55$ to binary $(0011\ 0111)_2$, then invert the bits to $(1100\ 1000)_2$ and add 1 to get $(1100\ 1001)_2$.

### 2. Binary Arithmetic & ALU Operations
*   **Binary Subtraction:** $A - B$ is calculated using addition and the 2's complement of B: $A + (\text{bitwise inverse of } B) + 1$.
*   **Overflow Detection:** Overflow occurs when the addition of two numbers with the same sign produces a result with the opposite sign (e.g., adding two positive numbers yields a negative result, or two negative numbers yield a positive result).
*   **Booth's Algorithm:** A multiplication algorithm for signed 2's complement numbers utilizing arithmetic shifting and conditional addition/subtraction based on the current and previous least significant bits (LSB) of the multiplier.
    *   *Steps:* Initialize the Product and set the Previous LSB to 0. At each step, analyze the current LSB and the Previous LSB:
        *   `01`: Add Multiplicand.
        *   `10`: Subtract Multiplicand.
        *   `00` or `11`: No arithmetic action.
        *   After the arithmetic step, perform an Arithmetic Right Shift.
*   **32-bit ALU Interfaces:**
    *   **Inputs:** `A` (32 bits), `B` (32 bits), `ALU operation` (control signal).
    *   **Outputs:** `Result` (32 bits), `Zero` flag (1 bit), `Overflow` flag (1 bit).

### 3. Combinational & Sequential Logic Design
*   **Karnaugh Maps (K-Maps):** Used for boolean logic simplification to find the minimal sum-of-products equation. Groupings of adjacent 1s must be in powers of 2 (1, 2, 4, 8) and can wrap around the edges.
    *   *Example simplified equation from a K-map:* $F = AC' + AB' + A'BC$
*   **Logic Design Process:** 
    1.  Define the system inputs and outputs.
    2.  Create a truth table based on the system description (e.g., designing an Automatic Light with Motion Detection using a Switch `S`, Motion detector `M`, and Daylight sensor `D`).
    3.  Transfer the truth table outputs to a K-Map.
    4.  Derive the simplified boolean equation (e.g., $L = S + M + D'$).
    5.  Draw the logic gate diagram mapping the equation to AND, OR, and NOT gates.

---\n
## Part 2: Final Synthesis - MIPS Processor Simulation Project (spimcore)

### Project Overview
The capstone project requires simulating the datapath and control of a complete MIPS processor using the C programming language. Students must implement specific stage functions within `project.c`, which act as the heart of the simulation driven by the `spimcore.c` framework.

*   **Rules & Constraints:**
    *   Do **NOT** modify `spimcore.c` or `spimcore.h`.
    *   No standard I/O functions (like `printf` or `scanf`) are needed within `project.c`. The simulation engine handles this.
    *   Compilation must be done on a Linux environment using GCC: `gcc -o spimcore spimcore.c project.c`.
    *   The compiled program executes `.asc` files containing sequential 32-bit MIPS instructions in hexadecimal format.

### Memory Architecture Details
*   **Word-Aligned Array:** The main memory (`Mem`) is modeled as an array of 32-bit unsigned integers (`unsigned int`). Therefore, it is an array of words, not bytes.
*   **Addressing & Indexing:** Standard MIPS memory addresses are byte-addressed (e.g., `0x4000`, `0x4004`). Because the C array holds words, you must convert the byte address to a word index by shifting right by 2.
    *   *Index Calculation:* `Mem[PC >> 2]`
*   **Alignment Checks:** Address alignment must be tested *before* any shifting occurs. Functions like `rw_memory` and `instruction_fetch` must verify word alignment (`address % 4 == 0`) and halt the simulator if unaligned access is attempted.

### Datapath Execution Stages (Implementation in C)

The step-by-step execution of a MIPS instruction is divided into specific functions within `project.c`:

1.  **`instruction_fetch`:** Retrieves the instruction from instruction memory.
    *   Check if `PC` is word-aligned (`PC % 4 == 0`).
    *   Fetch the instruction: `Instruction = Mem[PC >> 2]`.
2.  **`instruction_partition`:** Slices the 32-bit instruction into its fundamental MIPS component fields.
    *   *Implementation:* Use bitwise AND (`&`) for masking and right bit shifts (`>>`) for positioning.
    *   *Example:* `unsigned op = (instruction & 0xFC000000) >> 26;`
    *   Ensure `r1`, `r2`, `r3`, `funct`, `offset`, and `jsec` are extracted cleanly, regardless of the instruction format.
3.  **`instruction_decode`:** Sets the specific processor control signals within the `struct_controls` struct based on the `op` code.
    *   Signals are stored as `char` data types (acting as 8-bit containers for 0 or 1), except for `ALUOp` which is a 3-bit signal (0-7).
    *   *Multiple Levels of Decoding:* For R-type instructions, `ALUOp` is initially set to 7 (`111`). This signals the subsequent `ALU_operations` function that it must decode the `funct` field to determine the final ALU command.
    *   *Don't Cares:* If a control signal is not used by the current instruction (e.g., `RegDst` during a Jump), its value does not matter and will not affect datapath execution.
4.  **`read_register`:** Retrieves operand data from the Register File (`Reg` array) using the specified source register indices (`r1` and `r2`).
5.  **`sign_extend`:** Extends a 16-bit immediate `offset` into a full 32-bit value. If the 16th bit (the sign bit) is a 1, the upper 16 bits must be padded with 1s to preserve the negative value.
6.  **`ALU_operations`:** Prepares the inputs and multiplexer logic for the ALU.
    *   Use the `ALUSrc` signal to choose between `data2` (the register value) and the `extended_value` (immediate) as the second ALU input.
    *   If it's an R-type instruction (`ALUOp == 7`), decode the `funct` parameter to dictate the specific arithmetic or logic operation.
    *   Invoke the core ALU function, capturing the `Result` and updating the `Zero` flag.
7.  **`rw_memory`:** Handles reading from and writing to Data Memory.
    *   If `MemRead` or `MemWrite` is asserted, verify that `ALUresult` (which acts as the memory address) is word-aligned (`ALUresult % 4 == 0`). If unaligned, halt the simulation.
    *   Perform the read or write using the corrected array index: `Mem[ALUresult >> 2]`.
8.  **`write_register`:** Writes computed or retrieved data back to the register file.
    *   Use `MemtoReg` as a multiplexer to select whether data comes from Memory or the `ALUresult`.
    *   Use `RegDst` to select the correct destination register index (`r2` for I-type, `r3` for R-type).
    *   Write the final value into the `Reg` array only if `RegWrite == 1`.
9.  **`PC_update`:** Updates the Program Counter for the next clock cycle.
    *   *Sequential:* `PC = PC + 4`.
    *   *Branching:* If `Branch == 1` and `Zero == 1` (indicating a taken branch like `beq`), add the shifted sign-extended offset to the `PC`.
    *   *Jumping:* If `Jump == 1`, shift the `jsec` target left by 2 and combine it with the upper 4 bits of the updated `PC`.

### Critical Control Signals Reference
*   `RegDst`: Determines the destination register index source. `0` for I-type (uses `rt`), `1` for R-type (uses `rd`).
*   `ALUSrc`: Determines the second input to the ALU. `0` for R-type and branching instructions (uses `Read Data 2`), `1` for most I-types (uses the sign-extended immediate value).
*   `MemtoReg`: Selects the data to be written to the register file. `0` routes the ALU result, `1` routes Data Memory read data.
*   `Zero`: An ALU output flag indicating a zero result. It is fundamentally used alongside the `Branch` signal to resolve conditional branches.