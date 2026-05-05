# Math Foundations: Summations & Recurrences

## 1. Theoretical Core & Formulas

### Summations
The process of adding things together, often represented by the capital Greek letter Sigma ($\Sigma$). To perform Big-O analysis, we seek a **closed-form** mathematical expression of the summation.

**Core Formulas:**
*   **Constant Series:** $\sum_{i=1}^n c = c \cdot n$
*   **Arithmetic Series (Sum of $i$):** $\sum_{i=1}^n i = \frac{n(n+1)}{2} = O(n^2)$
*   **Sum of Squares (Sum of $i^2$):** $\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6} = O(n^3)$
*   **Sum of Cubes:** $\sum_{i=1}^n i^3 = \frac{n^2(n+1)^2}{4} = O(n^4)$
*   **Geometric Series:** $\sum_{i=0}^{n-1} a r^i = \frac{a(r^n - 1)}{r - 1}$
    *   Infinite Geometric Series (where $|x| < 1$): $\sum_{i=0}^\infty x^i = \frac{1}{1-x}$

### Recurrences
A recurrence relation models the running time $T(n)$ of a recursive function by describing how to calculate a term based on previous terms in the sequence.

*   **Divide and Conquer General Form:** $T(n) = aT(n/b) + D(n) + C(n)$
    *   $a$ is the number of subproblems.
    *   $b$ is the factor by which the input size is divided.
    *   $D(n)$ is the divide time, and $C(n)$ is the combine time.

## 2. Techniques

### Master Theorem
Used to quickly determine the Big-O running time of divide-and-conquer algorithms matching the form $T(n) = aT(n/b) + f(n)$. It compares the work done in splitting/combining $f(n)$ to the work done in the recursive calls $O(n^{\log_b a})$. 

### Iteration Method (Substitution Method)
A step-by-step technique to unroll a recurrence relation into a summation, which can then be reduced to a closed form.
1.  **Expand** the recurrence step by step for at least 3 iterations.
2.  **Notice the pattern** that emerges and write a generalized equation in terms of $k$.
3.  **Determine the base case** to find the value of $k$ that terminates the recurrence.
4.  **Derive a closed-form solution** by substituting $k$ back into the generalized equation and simplifying any summations.

## 3. Algorithmic Tracing: Iteration Method Example

**Problem:** Solve $T(n) = 2T(n-1) + 5$, with base case $T(1) = 1$.

**Step 1: Expand (Unroll)**
*   $k=1: T(n) = 2T(n-1) + 5$
*   $k=2: T(n) = 2[2T(n-2) + 5] + 5 = 2^2T(n-2) + 2(5) + 5$
*   $k=3: T(n) = 2^2[2T(n-3) + 5] + 2(5) + 5 = 2^3T(n-3) + 2^2(5) + 2(5) + 5$

**Step 2: Generalize Pattern**
*   $k$: $T(n) = 2^k T(n-k) + \sum_{i=0}^{k-1} 5 \cdot 2^i$

**Step 3: Determine Base Case**
*   We hit the base case when $n - k = 1$.
*   Solving for $k$, we get $k = n - 1$.

**Step 4: Substitute and Solve (Closed-Form)**
*   Substitute $k = n - 1$ into the generalized equation:
    $T(n) = 2^{n-1}T(1) + 5 \sum_{i=0}^{(n-1)-1} 2^i$
*   Knowing $T(1) = 1$, we get:
    $T(n) = 2^{n-1}(1) + 5 \sum_{i=0}^{n-2} 2^i$
*   Apply the Geometric Series formula to the summation:
    $T(n) = 2^{n-1} + 5 \left( \frac{2^{n-1} - 1}{2 - 1} \right)$
*   Simplify:
    $T(n) = 2^{n-1} + 5(2^{n-1} - 1)$
    $T(n) = 6(2^{n-1}) - 5$
    $T(n) = 3 \cdot 2^n - 5$
*   **Result:** $O(2^n)$

## 4. Skills & Pitfalls

*   **Pitfall: Off-by-one errors in summation indices.** Known closed-form formulas usually assume the index starts at 1 (or 0 for geometric series). If a summation begins at a different value (e.g., $\sum_{i=10}^n i$), you must shift the summation or subtract the missing prefix (e.g., $\sum_{i=1}^n i - \sum_{i=1}^9 i$) before applying the formula.
*   **Pitfall: Misapplying the Master Theorem cases.** Ensure the recurrence exactly matches the required form $T(n) = aT(n/b) + f(n)$ and carefully determine whether $f(n)$ is polynomially smaller, larger, or equal to $O(n^{\log_b a})$.
*   **Must-Know Skill: Index Manipulation.** The ability to algebraically manipulate limits (e.g. changing limits from $1 \dots n$ to $0 \dots n-1$) or split summations (e.g., $\sum c \cdot a_k = c \sum a_k$ and $\sum (a_k + b_k) = \sum a_k + \sum b_k$) is critical.
*   **Must-Know Skill: Logarithm Properties.** When evaluating base cases for divide and conquer algorithms (e.g., $n/2^k = 1 \implies k = \log_2 n$), exponent and logarithm properties are heavily utilized to simplify $a^{\log_b n}$.