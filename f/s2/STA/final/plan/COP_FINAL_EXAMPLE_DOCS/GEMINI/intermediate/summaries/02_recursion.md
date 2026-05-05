# 02. Recursion & Recursive Solutions

## 1. Theoretical Core Concepts
* **Recursion**: Defining a problem in terms of a simpler version of itself.
* **Base Case (Stopping Condition)**: The condition where the problem is small enough to be solved directly. It is required to prevent infinite recursion.
* **Recursive Step (Reduction Step)**: Breaking the big problem into smaller subproblems by having the function call itself.
* **Stack Frames**: Each function call creates its own copy of all local variables, conceptually like stacking "Post-it notes". A return expression must be evaluated to a single value before control is passed back to the caller. 
* **Tail Recursion vs. Head Recursion**: Tail recursion is where the recursive call is the last operation. Head recursion is where the recursive call happens before any other operations.

## 2. Algorithmic Tracing
**Tracing `factorial(4)`**:
Given the logic `return n * factorial(n - 1);` with base case `if (n <= 1) return 1;`
1. `main()` calls `factorial(4)`
2. Frame `f(4)`: evaluates `4 * f(3)`. Calls `f(3)`.
3. Frame `f(3)`: evaluates `3 * f(2)`. Calls `f(2)`.
4. Frame `f(2)`: evaluates `2 * f(1)`. Calls `f(1)`.
5. Frame `f(1)`: hits base case `n <= 1`, returns `1`.
6. Frame `f(2)`: receives `1`, evaluates `2 * 1 = 2`, returns `2`.
7. Frame `f(3)`: receives `2`, evaluates `3 * 2 = 6`, returns `6`.
8. Frame `f(4)`: receives `6`, evaluates `4 * 6 = 24`, returns `24` to `main()`.

## 3. Code Implementation

### Towers of Hanoi
```c
void towerOfHanoi(int n, char source, char dest, char aux) {
    if (n == 1) {
        printf("Move disk 1 from pole %c to pole %c\n", source, dest);
        return;
    }
    // Move n-1 disks from source to aux, using dest as auxiliary
    towerOfHanoi(n - 1, source, aux, dest);
    // Move the nth disk from source to dest
    printf("Move disk %d from pole %c to pole %c\n", n, source, dest);
    // Move the n-1 disks from aux to dest, using source as auxiliary
    towerOfHanoi(n - 1, aux, dest, source);
}
```

### Permutations (Brute Force)
```c
void permutation_fill(Song *solution, int size, int pos, const Song *actual, int *is_used) {
    // Base Case: If the solution array is completely filled
    if (pos == size) {
        permutation_print(solution, size); 
        return;
    }    

    // Recursive Case: Fill the current slot and recursively fill remaining slots
    for (int x = 0; x < size; x++) {
        if (is_used[x] == 0) {
            solution[pos] = actual[x];
            is_used[x] = 1; // Mark element as used
            permutation_fill(solution, size, pos + 1, actual, is_used);
            is_used[x] = 0; // Backtrack (unmark)
        }
    }
}
```

## 4. Skills & Pitfalls
* **Common Mistakes**:
  * **Infinite Recursion / Stack Overflow**: Forgetting a base case or passing parameters that do not progress toward the base case, eventually resulting in a Segmentation Fault.
  * **Incorrect Order of Operations**: Putting operations after the recursive call when they should be before it (or vice versa), breaking intended logic.
* **Must-Know Skills**:
  * **Brute Force Enumeration Framework**: Using recursion to systematically check all candidates for a solution (e.g., subsets, permutations). A `pos` index tracks depth, and a loop handles the choices at each index.
  * **Tracking State**: Maintaining an `is_used` array when generating permutations to ensure elements are not reused in the same candidate solution.
  * **Understanding Overhead**: Recognizing that recursion tends to be less efficient than its iterative counterpart due to function call overhead. Some recursive algorithms (like basic Fibonacci) can do massive amounts of redundant work.
