# Topic: Bitwise Operators & Binary Numbers

## 1. Theoretical Core
### Binary Representation
* **Binary System**: A base-2 number system using only digits 0 and 1. Each digit is a *bit*. Often grouped in 8 bits (a *byte*).
* **Signed Integers**: Represent negative numbers using systems like 1's complement or 2's complement.
    * **1's Complement**: Inverts all bits of the positive number. Contains two representations for zero (+0 and -0).
    * **2's Complement**: Inverts all bits of the positive number and adds 1 to the least significant bit (LSB). The most significant bit (MSB) determines the sign (0 for non-negative, 1 for negative). For an 8-bit byte, the range is -128 to +127.
* **Unsigned Integers**: Use the full range of bits to represent only non-negative numbers, increasing the maximum representable value (e.g., a 32-bit unsigned integer ranges from 0 to 4,294,967,295).

### Core Concepts (Bitwise Operators)
* **`&` (AND)**: Performs a bit-by-bit comparison. The result bit is 1 if both operand bits are 1.
* **`|` (OR)**: Performs a bit-by-bit comparison. The result bit is 1 if at least one operand bit is 1.
* **`^` (XOR)**: Performs a bit-by-bit comparison. The result bit is 1 if the operand bits are different (one is 1, the other is 0).
* **`~` (NOT)**: Flips every bit in a value (0 becomes 1, 1 becomes 0). Result depends on the assumed bit width (e.g., `~n = -(n+1)` in 2's complement).
* **`<<` (Left Shift)**: Shifts bits to the left, filling with 0s on the right. `var << n` multiplies `var` by $2^n$.
* **`>>` (Right Shift)**: Shifts bits to the right. 
    * *Logical shift*: Fills the left with 0s (typically for unsigned integers).
    * *Arithmetic shift*: Fills the left with the MSB (sign bit) to preserve the sign (typically for signed integers). 
    * `var >> n` divides `var` by $2^n$ if `var` is non-negative.

### Base Conversions
* **Decimal to Binary**: Repeatedly divide by 2, keeping remainders (e.g., $41_{10}$ = $101001_2$).
* **Binary to Hexadecimal**: Group bits in sets of 4 (nibbles) and convert to Hex digits 0-F (e.g., $1010 0111_2$ = $\text{A}7_{16}$).
* **Hexadecimal to Decimal**: Multiply each digit by powers of 16 (e.g., $2\text{F}_{16} = 2 \times 16^1 + 15 \times 16^0 = 47_{10}$).

## 2. Algorithmic Tracing
### Common Bitwise Tricks (Bit Masking)
Bit masking is a technique to inspect or manipulate individual bits using a `BITMASK` (a binary value where target bits are set to 1).
* **Set a bit on**: `var |= BITMASK`
* **Set a bit off**: `var &= ~BITMASK`
* **Toggle a bit**: `var ^= BITMASK`
* **Check a bit**: `var & BITMASK` (returns non-zero if the bit is set)
* **Check for Power of 2**: `(n & (n - 1)) == 0` (returns true if `n` is a power of 2, since powers of 2 have only one bit set, and subtracting 1 flips all lower bits and clears the set bit).

### Tracing XOR for Difference Counting
Counting how many bit positions differ between unsigned integers `a` and `b`:
1. XOR `a` and `b` (`num = a ^ b`). The 1s in `num` represent the differing bits.
2. Iterate through each bit of `num` (e.g., using a loop up to `sizeof(num)*8` bits).
3. Use `(num & 1) == 1` to check if the rightmost bit is 1. If so, increment the difference counter.
4. Shift `num` right by 1 (`num = num >> 1`) to move the next bit to the LSB position.

## 3. Code Implementation
The following snippet demonstrates common bitwise operations, including checking for an odd number, isolating a specific bit, and applying bit masks:

```c
#include <stdio.h>

// Check if a number is odd without using the modulo operator
int is_odd(int num) {
    return num & 1;
}

// Find the value of the rightmost 1 bit in a positive integer N
int rightmost_one_bit_value(int N) {
    int m = 1;
    // Perform a repeated bitwise AND and terminate at the first 1
    while ((N & m) == 0) {
        m = m << 1;
    }
    return m;
}

// Bitmask operations demonstration
void manipulate_bits() {
    unsigned int flags = 0; // All bits 0
    unsigned int MASK = 1 << 3; // Mask for the 4th bit (00001000)

    // Set a bit on
    flags |= MASK;

    // Toggle a bit
    flags ^= MASK;

    // Set a bit off
    flags &= ~MASK;

    // Check if a bit is set
    if (flags & MASK) {
        printf("Bit is set!\\n");
    }
}
```

## 4. Skills & Pitfalls
### Must-Know Skills
* **Bit Width Awareness**: Always be mindful of the variable's size in bits (e.g., `sizeof(int) * 8`) when shifting or masking, especially for operations like finding the leftmost bit.
* **Using Unsigned Types for Bit Manipulation**: Prefer `unsigned int` or explicitly sized types like `uint32_t` for pure bitwise manipulation to avoid ambiguous behavior with arithmetic right shifts and sign extension.
* **Parentheses for Precedence**: Bitwise operators (`&`, `^`, `|`) have lower precedence than relational operators (`==`, `!=`). Always use parentheses to ensure correct evaluation order, e.g., `if ((x & mask) == mask)` instead of `if (x & mask == mask)`.

### Common Mistakes (Pitfalls)
* **Sign Extension on Right Shift**: Using the right shift operator `>>` on negative signed integers often results in an arithmetic shift, where the sign bit (1) is duplicated into the newly vacated bits on the left. This can cause infinite loops or unexpected values if you assume a logical shift.
* **Operator Confusion**: Accidentally swapping bitwise operators (`&`, `|`, `~`) with logical operators (`&&`, `||`, `!`).
* **Shifting Out of Bounds**: Shifting a value by an amount greater than or equal to its bit width (e.g., shifting a 32-bit integer by 32 or more) results in undefined behavior in C.
