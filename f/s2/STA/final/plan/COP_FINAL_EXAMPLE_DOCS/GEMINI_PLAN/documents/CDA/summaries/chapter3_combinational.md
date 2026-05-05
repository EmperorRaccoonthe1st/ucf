# Chapter 3: Combinational Logic

## 1. Logic Gates

Combinational logic circuits are built using fundamental logic gates where the output is strictly a function of the present inputs (no feedback or memory). The primary voltage levels in digital systems are Low (0) and High (1).

### Fundamental Gates
*   **NOT (Inverter):** Unary operator. Flips the input. $Z = X'$ or $\overline{X}$.
    *   Truth Table: `0->1, 1->0`
*   **AND:** Logical product. Output is 1 only if all inputs are 1. $Z = X \cdot Y$.
    *   Truth Table: `(0,0)->0, (0,1)->0, (1,0)->0, (1,1)->1`
*   **OR:** Logical sum. Output is 1 if at least one input is 1. $Z = X + Y$.
    *   Truth Table: `(0,0)->0, (0,1)->1, (1,0)->1, (1,1)->1`

### Universal and Advanced Gates
*   **NAND:** NOT-AND. Output is 0 only if all inputs are 1. $Z = (X \cdot Y)'$.
*   **NOR:** NOT-OR. Output is 1 only if all inputs are 0. $Z = (X + Y)'$.
*   **XOR (Exclusive-OR):** Represents \"inequality\" or \"difference\". Output is 1 if inputs are different. $Z = X \oplus Y = X'Y + XY'$.
*   **XNOR (Exclusive-NOR):** Represents \"equality\" or \"coincidence\". Output is 1 if inputs are the same. $Z = \overline{X \oplus Y} = XY + X'Y'$.

## 2. Boolean Algebra

Boolean algebra provides the mathematical foundation for digital logic design, dealing with binary variables and logic operators (AND, OR, NOT).

### Axioms and Theorems
*   **Identity:** $X + 0 = X$ ; $X \cdot 1 = X$
*   **Null (Dominance):** $X + 1 = 1$ ; $X \cdot 0 = 0$
*   **Idempotency:** $X + X = X$ ; $X \cdot X = X$
*   **Involution:** $(X')' = X$
*   **Inverse (Complement):** $X + X' = 1$ ; $X \cdot X' = 0$
*   **Commutative:** $X + Y = Y + X$ ; $X \cdot Y = Y \cdot X$
*   **Associative:** $(X + Y) + Z = X + (Y + Z)$ ; $(X \cdot Y) \cdot Z = X \cdot (Y \cdot Z)$
*   **Distributive:** $X \cdot (Y + Z) = (X \cdot Y) + (X \cdot Z)$ ; $X + (Y \cdot Z) = (X + Y) \cdot (X + Z)$
*   **Uniting Theorem:** $X \cdot Y + X \cdot Y' = X$ ; $(X + Y) \cdot (X + Y') = X$
*   **Absorption:** $X + X \cdot Y = X$ ; $X \cdot (X + Y) = X$
*   **DeMorgan's Theorems:** $\overline{X + Y} = \overline{X} \cdot \overline{Y}$ ; $\overline{X \cdot Y} = \overline{X} + \overline{Y}$

### Proving Equivalence
1.  **Perfect Induction:** Creating a complete truth table to show that all possible input combinations yield the exact same output for two different expressions.
2.  **Rewriting:** Applying Boolean axioms algebraically to transform one expression into another.

## 3. Canonical Forms and Truth Tables

A truth table is the unique algebraic signature of a Boolean function. A function with $n$ inputs has $2^n$ entries.

### Sum of Products (SOP)
*   Also known as **Disjunctive Normal Form** or **Minterm Expansion**.
*   A **minterm** is a product of literals where every variable appears exactly once (e.g., $m_3 = A'BC$). It represents an input combination where the function evaluates to 1.
*   Constructed by OR-ing all minterms for which the output is 1.
*   Notation: $F(A,B,C) = \Sigma m(1, 3, 5, 6, 7)$

### Product of Sums (POS)
*   Also known as **Conjunctive Normal Form** or **Maxterm Expansion**.
*   A **maxterm** is a sum of literals where every variable appears exactly once. It represents an input combination where the function evaluates to 0. Maxterms are the inverse of minterms.
*   Constructed by AND-ing all maxterms for which the output is 0.
*   Notation: $F(A,B,C) = \Pi M(0, 2, 4)$

### Incompletely Specified Functions (Don't Cares)
Some systems do not require every input combination to be specified (e.g., BCD logic where inputs 1010 to 1111 never occur). These are marked as 'X' or 'd' (don't care) in the truth table and can be treated as either 1 or 0 during minimization to yield the simplest hardware.
*   $F = \Sigma m(0, 2) + d(7, 10, 13)$

## 4. Karnaugh Maps (K-Maps) and Minimization

K-Maps are a visual representation of a truth table structured around Boolean subcubes, enabling the easy application of the Uniting Theorem ($XY + XY' = X$) via visual adjacencies.

*   **Structure:** Cells are arranged using Gray-code order (00, 01, 11, 10) so that adjacent cells differ by exactly one bit. Adjacencies wrap around the edges (top/bottom, left/right, and corners).
*   **Implicant:** A single 1 or a valid grouping of 1s (and don't cares). Group sizes must be powers of 2 (1, 2, 4, 8, 16).
*   **Prime Implicant (PI):** An implicant that cannot be combined into a larger group.
*   **Essential Prime Implicant (EPI):** A prime implicant that covers at least one '1' that is not covered by *any* other prime implicant. EPIs MUST be included in the final expression.

### Algorithm for Two-Level Simplification (MSP)
1.  Identify all prime implicants (find the largest possible power-of-2 rectangles).
2.  Identify all essential prime implicants. Add them to the final expression.
3.  If there are remaining uncovered 1s, select the minimal number of non-essential prime implicants needed to cover them.
4.  *Note:* To find the complement of a function ($F'$), group the 0s instead of the 1s.

## 5. Standard Combinational Hardware

### Adders
*   **Half Adder:** Adds two 1-bit inputs (A, B).
    *   $Sum = A \oplus B$
    *   $CarryOut = A \cdot B$
*   **Full Adder:** Adds two 1-bit inputs and a Carry-In ($C_{in}$).
    *   $Sum = A \oplus B \oplus C_{in}$
    *   $C_{out} = AB + AC_{in} + BC_{in}$

### Decoders
A logic block that takes an $n$-bit input and asserts exactly one of its $2^n$ outputs based on the input combination. For example, a 3-to-8 decoder will assert $Out_5$ if the input is 101. It can be used to implement generic Boolean functions by generating all minterms.

### Multiplexers (MUX)
A selector block that takes $2^n$ data inputs and $n$ selection (control) lines to output exactly one of the data inputs. 

### Programmable Logic Arrays (PLA)
A structured grid implementation of Sum of Products logic. It consists of a programmable AND array (to generate product terms) feeding into a programmable OR array (to combine them into final outputs).

## 6. Logic Design Procedure

The standard hardware design process is iterative:
1.  **Define:** Understand inputs, outputs, and system behavior.
2.  **Truth Table:** Construct a truth table mapping all inputs to desired outputs.
3.  **Specify:** Fill in 1s, 0s, and Don't Cares (X) for unreachable states.
4.  **K-Map:** Map each output column to its own Karnaugh Map.
5.  **Minimize:** Use Prime Implicants and Essential Prime Implicants to find the minimal SOP (or POS).
6.  **Equations:** Extract the minimized Boolean equations.
7.  **Gate Diagram:** Draw the physical logic gate network based on the equations, sharing gates where applicable (multi-level realization vs two-level realization) to reduce transistor count or delay.