# Algorithm Analysis & Algorithm Design

## 1. Theoretical Core: Big-O, Omega, and Theta
*   **Big-O ($O$):** Represents the asymptotic upper bound of an algorithm's runtime or space. It describes the worst-case scenario, guaranteeing the algorithm will take no more than a certain amount of time for sufficiently large inputs.
*   **Omega ($\Omega$):** Represents the asymptotic lower bound. It describes the best-case scenario, guaranteeing the algorithm will take at least a certain amount of time.
*   **Theta ($\Theta$):** Represents the asymptotically tight bound. It is used when an algorithm is bounded both above and below by the same function (i.e., both Big-O and Omega are the same).

## 2. Common Time Complexities
*   **$O(1)$ - Constant Time:** Runtime is independent of the input size. Example: Array index access.
*   **$O(\log n)$ - Logarithmic Time:** Runtime grows logarithmically. Example: Binary search on a sorted list.
*   **$O(n)$ - Linear Time:** Runtime grows proportionally with the input size. Example: Linear search through an array.
*   **$O(n \log n)$ - Linearithmic Time:** Typical of optimal comparison-based sorts. Example: Merge sort or the binary search intersection strategy.
*   **$O(n^2)$ - Quadratic Time:** Runtime grows with the square of the input size. Example: Comparing all pairs in an array or a nested loop linear search intersection strategy.

## 3. Analyzing Loops and Nested Loops
*   **Single Loops:** The runtime correlates to the number of iterations times the work done inside the loop. For $n$ iterations doing constant work, the time is $O(n)$.
*   **Nested Loops:** Evaluated by multiplying the number of executions of the inner loop by the outer loop (when independent). For example, an outer loop running $n$ times and an inner loop running $m$ times results in $O(n \times m)$ time. 
*   **Algorithmic Tracing (Sorted Array Matching):** When counting common elements in two sorted arrays of sizes $n$ and $m$:
    *   *Strategy 1 (Linear Search):* An outer loop over $n$ elements and an inner loop over $m$ elements yields $O(n \times m)$.
    *   *Strategy 2 (Binary Search):* A loop over $n$ elements performing a binary search in $m$ elements yields $O(n \log m)$.
    *   *Strategy 3 (Two Pointers):* Iterating both arrays simultaneously using two index variables yields an efficient $O(n + m)$.

## 4. Code Implementation
*Two-Pointer Strategy for Sorted Array Intersection in $O(n + m)$ time:*

```c
#include <stdio.h>

// Returns the number of common elements between two sorted arrays
int count_common(int arr1[], int n, int arr2[], int m) {
    int i = 0, j = 0;
    int count = 0;

    // Advance the index of the smaller value, count when equal
    while (i < n && j < m) {
        if (arr1[i] == arr2[j]) {
            count++;
            i++;
            j++;
        } else if (arr1[i] < arr2[j]) {
            i++;
        } else {
            j++;
        }
    }
    return count;
}
```

## 5. Skills & Pitfalls
*   **Must-Know Skills:**
    *   **Empirical Runtime Calculation:** Using experimental elapsed times to find the theoretical constant $C$. Given $T(n) = C \cdot f(n)$, we can calculate $C = T(n) / f(n)$. This enables the prediction of runtimes for arbitrary input sizes (e.g., calculating expected runtime for $N=10,000$ when the time for $N=5,000$ is known).
    *   **Solving Constraints:** Re-arranging empirical equations to find the maximum allowed input size $N$ for a given constraint $T$.
*   **Common Mistakes (Pitfalls):**
    *   **Ignoring Constant Factors:** While $O(N)$ ignores constants theoretically, in practice (empirical runtime), the constant factor dictates performance for realistic input sizes.
    *   **Misidentifying the Bottleneck:** Failing to recognize which loop or operation dominates the overall runtime (e.g., misidentifying the bottleneck as a single $O(N)$ loop when a hidden $O(N^2)$ operation is executed).
    *   **Assuming Equal Lengths:** Assuming inputs (like two arrays) always have the same length $N$, ignoring edge case runtimes like $O(M \times N)$ or $O(M \log N)$.
