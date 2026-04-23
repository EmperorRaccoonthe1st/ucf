# Chapter 5: Arithmetic Hardware and Algorithms

This chapter covers the foundational algorithms and hardware implementations for computer arithmetic, including integer addition, subtraction, multiplication, division, and IEEE 754 floating-point operations.

## Integer Arithmetic

The Arithmetic Logic Unit (ALU) is the component of the processor responsible for performing arithmetic and logical operations.

### Addition and Subtraction
*   **Addition:** Binary addition operates similarly to decimal addition. 
    *   **Half Adder:** Adds two 1-bit inputs to produce a Sum and CarryOut. `Sum = A XOR B`, `Cout = A AND B`.
    *   **Full Adder:** Adds two 1-bit inputs and a CarryIn to produce a Sum and CarryOut. `Sum = A XOR B XOR Cin`, `Cout = AB + BCin + ACin`.
    *   **Ripple-Carry Adder:** Cascades multiple 1-bit full adders to add multi-bit numbers. A significant disadvantage is the long propagation delay, as the carry bit may have to ripple from the least significant bit (LSB) to the most significant bit (MSB).
    *   **Carry-Lookahead Adder:** Solves the ripple delay by determining carry values sooner using Carry Generate (`Gi = AiBi`) and Carry Propagate (`Pi = Ai XOR Bi`) logic.
*   **Subtraction:** Subtraction ($A - B$) is performed using addition and two's complement representation: $A + (-B) = A + B' + 1$. 
    *   The hardware takes the bitwise inverse of $B$ (using a 2:1 multiplexer) and sets the initial `CarryIn` to 1.
*   **Overflow:** Occurs when the result is too large or too small to be represented in the available bits. It can be detected by comparing the carry-in and carry-out of the most significant bit; if they are different, an overflow has occurred.

### Integer Multiplication
Multiplication is conceptually based on the \"paper and pencil\" method of shifting and adding.

*   **Version 1:** Uses a 64-bit Multiplicand register, a 64-bit ALU, a 64-bit Product register, and a 32-bit Multiplier register. 
    *   *Algorithm:* If the LSB of the multiplier is 1, add the multiplicand to the product. Shift the multiplicand left 1 bit. Shift the multiplier right 1 bit. Repeat 32 times (96 steps total).
    *   *Disadvantage:* Wastes space (half of the multiplicand bits are always 0) and wastes a 64-bit adder.
*   **Version 2:** Reduces hardware cost. Uses a 32-bit Multiplicand register, a 32-bit ALU, a 64-bit Product register, and a 32-bit Multiplier register.
    *   *Algorithm:* Instead of shifting the multiplicand left, the multiplicand is added to the left half of the product, and the product register is shifted right.
*   **Version 3:** Optimizes further by combining the Multiplier and Product registers into a single 64-bit register. Uses a 32-bit Multiplicand and a 32-bit ALU.
    *   *Algorithm:* The multiplier is initially placed in the right half of the product register. If the LSB is 1, add the multiplicand to the left half of the product register. Then, shift the entire product register right 1 bit.
*   **Multiplying by Constants:** Compilers often replace multiplications by constants with a series of shifts and adds (e.g., `A * 4` is equivalent to `A << 2`).

### Integer Division
Binary division uses the same hardware components as multiplication but executes a different algorithm (Restoring Division).

*   **Hardware Setup:** The multiplicand register is repurposed as the Divisor register (32 bits), and the product register becomes the Remainder register (64 bits). The dividend is placed in the lower half of the remainder register, and it is shifted left once to initialize.
*   **Algorithm for each pass:**
    1.  Subtract the divisor from the left half of the remainder register, placing the result back in the left half.
    2.  Check the sign of the remainder.
        *   *If negative (result < 0):* Restore the previous value by adding the divisor back. Shift the entire remainder register left, shifting in a 0 into the LSB.
        *   *If positive (result >= 0):* Do not restore. Shift the entire remainder register left, shifting in a 1 into the LSB.
    3.  After 32 iterations, shift the left half of the remainder register right by 1 bit.
    4.  *Result:* The lower half contains the Quotient, and the upper half contains the Remainder.
*   **Signed Division:** Store the signs of the divisor and dividend, convert negative values to positive, perform the division, and then apply signs. The Dividend and Remainder are defined to have the same sign. The Quotient is negated if the Divisor and Dividend signs disagree.

## Booth's Algorithm
Booth's Algorithm is an efficient method for multiplying two's complement signed integers. It allows multiplication without needing to strip signs and adjust them later. It is especially efficient for multipliers with long sequences (runs) of 1s or 0s.

*   **Setup:** Requires an $X$-bit multiplicand and an $X$-bit multiplier, and a $2X$-bit product register. An implied \"previous LSB\" (initially 0) is tracked just to the right of the LSB of the product register. The multiplier is placed in the right half of the product register.
*   **Algorithm Steps (repeated $X$ times for $X$-bit operands):**
    1.  **Examine the current LSB and the previous LSB** to determine the arithmetic action:
        *   **`00`** (Middle of a run of 0s): No arithmetic operation.
        *   **`01`** (End of a run of 1s): Add multiplicand to the left half of the product.
        *   **`10`** (Beginning of a run of 1s): Subtract multiplicand from the left half of the product.
        *   **`11`** (Middle of a run of 1s): No arithmetic operation.
    2.  **Arithmetic Shift Right (ASR):** Shift the entire product register right by 1 bit. An ASR preserves the sign bit (the MSB is copied into the new MSB position).
*   **Example: `(-5) x 2` using 5-bit representation**
    *   Multiplier `(-5)` = `11011`
    *   Multiplicand `2` = `00010`
    *   Initial Product: `00000 11011 0` (with previous LSB = 0)
    *   *Pass 1:* Ends are `10` -> Subtract multiplicand. ASR product.
    *   ... (Repeat for 5 total passes)
    *   *Final Product:* Drop the previous LSB to obtain the 10-bit two's complement result.

## IEEE 754 Floating-Point
The IEEE 754 standard defines the representation and arithmetic operations for real (\"float\") numbers.

### Representation
*   **Formats:** Single precision (32 bits) and Double precision (64 bits).
*   **Fields:**
    *   **Sign (1 bit):** `0` for positive, `1` for negative.
    *   **Exponent:** 8 bits for Single precision (Bias = 127), 11 bits for Double precision (Bias = 1023). Stored as a biased exponent (`Stored = Actual + Bias`).
    *   **Mantissa (Significand/Fraction):** 23 bits for Single precision, 52 bits for Double precision. Represents the fractional part after the normalized leading `1` (which is implied and not stored).
*   **Value Formula:** $(-1)^{\text{Sign}} \times (1.\text{Mantissa}) \times 2^{(\text{Exponent} - \text{Bias})}$

### Floating-Point Addition Algorithm
1.  **Align Binary Points:** Compare the exponents. Denormalize the smaller value by shifting its significand to the right until its exponent matches the larger exponent.
2.  **Add Significands:** Perform binary addition on the aligned significands.
3.  **Normalize Result:** Shift the resulting significand right (and increment exponent) or left (and decrement exponent) until it is in the format $1.XXXX$. Check for overflow/underflow.
4.  **Round:** Round the significand to the appropriate number of bits. If rounding causes the number to become un-normalized, repeat Step 3.

### Floating-Point Multiplication Algorithm
1.  **Calculate Exponent:** Add the biased exponents of the two operands and subtract the bias to prevent double-biasing: `New Biased Exponent = (Exp1 + Exp2) - Bias`.
2.  **Multiply Significands:** Perform standard binary integer multiplication on the significands (including the implied leading 1).
3.  **Normalize Product:** Shift the product right and increment the exponent if necessary. Check for overflow/underflow.
4.  **Round:** Round the significand to the appropriate number of bits. If it becomes un-normalized, go back to step 3.
5.  **Set Sign:** The product is positive if the original operands have the same sign, and negative if they have different signs.