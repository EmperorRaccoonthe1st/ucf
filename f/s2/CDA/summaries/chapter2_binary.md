# Chapter 2: Number Systems and Binary Representation

## 1. Representations of Integers
In the modern world, we use decimal (base 10) notation to represent integers. However, we can represent numbers using any base $b$, where $b$ is a positive integer greater than 1. Computers represent integers and perform arithmetic using binary (base 2) expansions, which only use the digits 0 and 1.

**Theorem (Base $b$ Expansion):**
Let $b$ be a positive integer greater than 1. Then if $n$ is a positive integer, it can be expressed uniquely in the form:
$$n = a_k b^k + a_{k-1} b^{k-1} + \dots + a_1 b + a_0$$
where $k$ is a nonnegative integer and $a_0, a_1, \dots, a_k$ are nonnegative integers less than $b$.

---\n
## 2. Base Conversions

### Binary to Decimal (Unsigned)
To convert an unsigned binary number to decimal, express the binary number $n$ in the polynomial form using base $b=2$:
$$n = a_k 2^k + a_{k-1} 2^{k-1} + \dots + a_1 2^1 + a_0 2^0$$
Start with $k=0$ for the least significant bit (rightmost) and count upward to the most significant bit (leftmost).

**Example:** Convert $(11011)_2$ to decimal.
*   $(1 \cdot 2^4) + (1 \cdot 2^3) + (0 \cdot 2^2) + (1 \cdot 2^1) + (1 \cdot 2^0)$
*   $= 16 + 8 + 0 + 2 + 1 = 27$

### Decimal to Binary (Unsigned)
To construct the base $b$ expansion of an integer $n$ (such as converting to binary where $b=2$, or potentially to octal/hex by changing $b$):
1.  Divide $n$ by $b$ using integer division to obtain a quotient and remainder. ($n = b \cdot q_0 + a_0$)
2.  The remainder, $a_0$, is the rightmost (least significant) digit.
3.  Next, divide the quotient $q_0$ by $b$. ($q_0 = b \cdot q_1 + a_1$)
4.  The new remainder, $a_1$, is the next digit to the left.
5.  Continue successively dividing the quotients by $b$ until the quotient is 0. The remainders read from bottom to top (or last to first) form the binary result.

**Example:** Convert $(19)_{10}$ to binary.
*   $19 \div 2 = 9$ R $1$ (Least Significant Bit)
*   $9 \div 2 = 4$ R $1$
*   $4 \div 2 = 2$ R $0$
*   $2 \div 2 = 1$ R $0$
*   $1 \div 2 = 0$ R $1$ (Most Significant Bit)
Result: $(10011)_2$

---\n
## 3. Signed Integer Representations

To represent negative numbers, we use a **sign bit**. The most significant bit (MSB) acts as the sign:
*   `0` represents a positive number.
*   `1` represents a negative number.

### Method 1: Sign-Magnitude
The first bit represents the sign, and the remaining bits represent the absolute value (magnitude).
*   **Drawbacks:** It features cumbersome addition/subtraction (must compare magnitudes to determine the sign of the result) and has two representations for zero (`+0` and `-0`).
*   **Example:** $-55$ in 8 bits. Magnitude of $55 = (0011 0111)_2$. Set MSB to 1 $\rightarrow (1011 0111)_2$.

### Method 2: 1's Complement
If a number is negative, its representation is the bitwise inverse (complement) of its positive counterpart.
*   **Drawbacks:** Like Sign-Magnitude, it still has the \"Zero Problem\" with two representations of zero: `+0 = 0000` and `-0 = 1111`.
*   **Example:** $-55$ in 8 bits. Positive $55 = (0011 0111)_2$. Bitwise inverse $\rightarrow (1100 1000)_2$.

### Method 3: 2's Complement
This is the standard representation for signed integers in modern computing (e.g., used by the `int` data type in C).
To represent a negative value:
1.  Find the binary representation of the positive magnitude.
2.  Perform a bitwise inverse (1's complement).
3.  Add `1` to the result.

*   **Advantage:** It fixes the Zero Problem. `+0 = 0000`. Inverting yields `1111`. Adding `1` yields `0000` (the carry-out is ignored), resulting in a single zero. It also simplifies binary arithmetic.
*   **Example:** $-55$ in 8 bits. Positive $55 = (0011 0111)_2$. Inverse $\rightarrow 1100 1000$. Add $1 \rightarrow (1100 1001)_2$.

### Sign Extension
When moving a value to a larger data type (e.g., 4 bits to 8 bits), we use sign extension to fill the new bits:
*   **Unsigned:** Pad with leading `0`s (e.g., `0110` $\rightarrow$ `0000 0110`).
*   **Signed (2's Complement):** Pad with copies of the MSB.
    *   Positive: `0110` $\rightarrow$ `0000 0110`
    *   Negative: `1010` $\rightarrow$ `1111 1010`

---\n
## 4. Binary Arithmetic and Overflow Detection

### Binary Addition and Subtraction
Binary numbers are added the same way decimal numbers are added.
For subtraction, we implement it by adding the 2's complement equivalent of the subtrahend: $A - B = A + (-B)$. The extra carry-out from the MSB during 2's complement arithmetic is normally ignored.

### Overflow Detection
Overflow occurs when the result of an arithmetic operation is too large or too small to be represented in the allocated number of bits.

**Unsigned Addition:**
In unsigned addition, an overflow occurs simply if the final carry-out from the most significant bit is `1`.

**Signed Addition (2's Complement):**
In signed addition, examining the final carry-out is not enough. Overflow happens when:
*   Two positive numbers are added, and the result appears negative.
*   Two negative numbers are added, and the result appears positive.
*   *(Note: Adding a positive and a negative number can never cause an overflow).*

**The XOR Rule for Signed Overflow:**
An easy hardware/algorithmic way to spot overflow is to compare the **\"Carry-in\"** of the MSB to the **\"Carry-out\"** of the MSB.
*   If `CarryIn(MSB) != CarryOut(MSB)` (Mathematically: `CarryIn XOR CarryOut == 1`), then an overflow has occurred.
*   If they are the same, no overflow occurred.