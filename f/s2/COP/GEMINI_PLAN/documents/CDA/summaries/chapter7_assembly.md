# Chapter 7: Assembly Programming

## 1. Introduction to MIPS Assembly
When a higher-level programming language (like C) is compiled, it is first converted into an assembly language, and then processed into machine code (binary) capable of running on a processor. The \"instruction set architecture\" (ISA) represents the processor's capability to run a particular set of commands. MIPS is a classic RISC (Reduced Instruction Set Computer) ISA. 

**Vocabulary (MIPS Instructions):** Individual commands that the MIPS processor can understand, categorized mainly into R-Type (Register), I-Type (Immediate), and J-Type (Jump).

## 2. Conditionals and Branching
Conditionals allow programs to execute different code paths based on dynamic evaluations. In MIPS, this is achieved through branch and jump instructions.

**Definition (Branch Instructions):**
*   `beq $s1, $s2, L` (Branch if equal): If `$s1 == $s2`, jump to label `L`.
*   `bne $s1, $s2, L` (Branch if not equal): If `$s1 != $s2`, jump to label `L`.
*   Branches are **I-Type instructions**. The offset (16 bits) is used to calculate the \"branch target address\".

**Definition (Jump Instructions):**
*   `j L` (Jump): Unconditionally jump to label `L`.
*   Jumps are **J-Type instructions**. The 26-bit address is a \"pseudo-direct address\". It is shifted left by 2 (multiplied by 4) and concatenated with the top 4 bits of the current Program Counter (PC) to calculate the next instruction address.

**Remark (spimcore Implementation Context):** 
In the `spimcore` project (`project.c`), the datapath for conditionals is explicit. For a `beq` (opcode `4`), the control signals are set as `Branch = 1` and `ALUOp = 1` (subtraction). The ALU subtracts the two registers, and if the result is 0, the `Zero` flag is set. The `PC_update` function checks `if (Branch && Zero)` to add the left-shifted extended offset to the PC. For a jump `j` (opcode `2`), `Jump = 1`, and the PC directly inherits the left-shifted 26-bit `jsec` combined with the upper 4 bits of the PC.

## 3. Loops (While, For, Do-While)
High-level loop constructs are synthesized in MIPS using a combination of initialization, condition checking (via `slt`, `slti`), branching (`beq`, `bne`), and unconditional jumps (`j`).

**Example (While Loop Execution):**
Consider the C code:
```c
i = 0;
while (i <= 20) {
    A[i] = i;
    i++;
}
```
**MIPS Assembly Conversion:**
```assembly
        addi $s1, $zero, 0      # Initialize i = 0 in $s1
loop:   slti $t1, $s1, 21       # Check if i < 21 (i.e., i <= 20). $t1 = 1 if true
        beq  $t1, $zero, end    # If $t1 == 0 (i > 20), exit loop
        
        # Calculate address of A[i]
        sll  $t2, $s1, 2        # $t2 = i * 4 (byte offset)
        add  $t2, $t2, $s0      # $t2 = base address of A ($s0) + offset
        
        sw   $s1, 0($t2)        # Store i ($s1) into A[i]
        addi $s1, $s1, 1        # i++
        j    loop               # Jump back to start of loop
end:    ...                     # Loop termination
```
*   **For Loops:** Similar to while loops, but the initialization happens once before the loop label, and the increment happens right before the jump back to the loop.
*   **Do-While Loops:** The condition check (`slt`, `beq`) is placed at the *end* of the loop, branching back to the start if the condition is true. This saves an unconditional jump instruction.

## 4. Procedure Calls
Programming languages separate individual tasks into functions or methods. In assembly, these are called \"procedures\".

**Vocabulary (Procedure Registers):**
*   `$a0` - `$a3`: Argument registers used to pass parameters to the procedure.
*   `$v0` - `$v1`: Return value registers used to pass results back to the caller.
*   `$ra`: Return address register (`$31`), storing where the procedure should return.

**Definition (Procedure Instructions):**
*   **Jump and Link (`jal`):** e.g., `jal 10000`. Sets `$ra = PC + 4` (saving the return address) and sets `PC = 40000` (jumping to the procedure).
*   **Jump Register (`jr`):** e.g., `jr $ra`. Sets `PC = $ra`, returning control to the calling function.

## 5. Stack Usage
When executing procedures, the processor has a limited number of registers. If a procedure needs to use registers that the caller also needs, or if the procedure calls another procedure (overwriting `$ra`), we must use memory to temporarily save these values.

**Definition (The Stack):** A region of memory used for dynamic storage during procedure execution. It typically grows downwards in memory.
*   `$sp`: The Stack Pointer register (`$29`). It points to the top (lowest address) of the stack.

**Mechanism (Prologue and Epilogue):**
*   **Prologue:** The start of a procedure. We move the stack pointer down to allocate space, then store (`sw`) registers. 
    *   *Example:* `addi $sp, $sp, -8` (allocate 8 bytes for 2 words), followed by `sw $ra, 4($sp)` and `sw $a0, 0($sp)`.
*   **Epilogue:** The end of a procedure. We load (`lw`) the saved values back into the registers, then move the stack pointer up to deallocate the space.
    *   *Example:* `lw $ra, 4($sp)`, `lw $a0, 0($sp)`, followed by `addi $sp, $sp, 8`.

## 6. Recursion in MIPS
Recursion occurs when a procedure calls itself. Because every call to the procedure overwrites the return address (`$ra`) and potentially the arguments (`$a0`), a recursive function **must** utilize the stack heavily to preserve state across recursive descents.

**Example (Recursive Sum):**
Convert the C function:
```c
int recSum(int n) {
    if (n <= 1) return n;
    else return n + recSum(n-1);
}
```

**MIPS Assembly Implementation:**
```assembly
recSum: slti $t0, $a0, 2        # Base case check: if n <= 1
        beq  $t0, $zero, else   # If n > 1, jump to recursive 'else' branch
        
        # Base case: return n
        add  $v0, $a0, $zero    # Place n ($a0) into return register ($v0)
        jr   $ra                # Return to caller
        
else:   # Recursive case: preserve state on stack
        addi $sp, $sp, -8       # Make room on stack for 2 words
        sw   $ra, 4($sp)        # Preserve the return address
        sw   $a0, 0($sp)        # Preserve the original argument (n)
        
        # Prepare for recursive call: recSum(n-1)
        addi $a0, $a0, -1       # Argument becomes n - 1
        jal  recSum             # Jump and link to recSum
        
        # Return from recursion: restore state
        lw   $a0, 0($sp)        # Restore original n
        lw   $ra, 4($sp)        # Restore original return address
        addi $sp, $sp, 8        # Deallocate stack space
        
        # Calculate: n + recSum(n-1)
        add  $v0, $v0, $a0      # $v0 currently holds recSum(n-1), add n
        jr   $ra                # Return to caller
```
*   **Remark:** Notice that without saving `$ra` on the stack, the `jal recSum` instruction would overwrite the original return address, causing an infinite loop upon trying to return. Without saving `$a0`, the final addition `add $v0, $v0, $a0` would use `1` (the base case argument) instead of the caller's value of `n`.