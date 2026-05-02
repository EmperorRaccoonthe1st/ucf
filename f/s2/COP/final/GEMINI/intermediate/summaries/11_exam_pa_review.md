# Phase 1 Extraction: Comprehensive Exam & PA Review

## 1. High-Frequency Exam Topics
Based on the analysis of Exam 1, Exam 2, and Final Exams (A & B) solutions, the Foundation Exam heavily tests the following theoretical and applied concepts:

### Mathematical & Algorithmic Analysis
*   **Recurrence Relations:** Deriving Big-O bounds using the Master Theorem and solving relations using the Iteration Technique (e.g., expanding $T(n) = 8T(n/2) + cn^2$).
*   **Summations:** Proving closed-form solutions for summations and manipulating summations algebraically.
*   **Runtime Analysis:** Determining Big-O/Big-Omega for nested loops, recursive functions, and standard operations on data structures (e.g., Heap remove-min is $O(\log n)$, Floodfill is $O(rc)$).
*   **Constant Factor Solving:** Solving for constants in $T(n)$ equations given specific runtimes in seconds/microseconds.

### Data Structure Operations & Tracing
*   **Sorting Algorithms:** Step-by-step tracing of Insertion Sort, Selection Sort, Merge Sort, and Quick Sort (Partition algorithm). Understanding when Quick Sort is preferred over Merge Sort (in-place vs. auxiliary array).
*   **Binary Trees & BSTs:** Writing recursive functions to traverse trees (e.g., summing path lengths, finding lower bounds).
*   **Binary Heaps:** Tracing insertions into an array-based heap and maintaining the heap property.
*   **Tries:** Recursive traversal to count words or specific node types.
*   **Linked Lists:** Iterative and recursive manipulation, particularly operations like adding/incrementing large numbers represented digit-by-digit.

### Memory & Pointer Management
*   **Dynamic Memory Allocation (DMA):** Allocating 2D arrays, arrays of pointers to structs, and deep copying strings without memory leaks.
*   **Recursion & Backtracking:** Evaluating permutations, combinations (e.g., combinations of signs), and graph traversal (e.g., Floodfill, Knight's Tour).

---

## 2. Programming Assignment Core Logic & "Tricks"

Each Programming Assignment (PA) focuses on mastering a specific data structure and introduces a unique algorithmic "trick."

*   **PA1 (Dynamic Memory & Structs):** 
    *   *Core Logic:* Managing complex, nested dynamically allocated memory (e.g., arrays of pointers to structs, 2D arrays for capacities).
    *   *The Trick:* Processing queries that require resizing arrays and moving struct pointers between different owners (kennels) while maintaining a separate dynamic dictionary to avoid string duplication.
*   **PA2 (Recursion & Backtracking):**
    *   *Core Logic:* Generating permutations using the recursive `is_used` array technique.
    *   *The Trick:* Permuting *indices* rather than the heavy structs themselves. Evaluating complex floating-point scoring logic (synergies, rival penalties) across every generated permutation to find the absolute maximum score.
*   **PA3 (Linked Lists & Queues):**
    *   *Core Logic:* Simulating a discrete-time system (minute-by-minute loop) using a singly linked list as a waiting queue.
    *   *The Trick:* Maintaining a chronologically ordered linked list via ordered insertion (without using built-in sorts) and utilizing pointer reassignment to assign nodes (cats) to stateful objects (doctors) within time constraints.
*   **PA4 (Sorting Algorithms):**
    *   *Core Logic:* Implementing Merge Sort and Quick Sort with custom `compareTo` wrapper functions for flexible sorting by multiple keys.
    *   *The Trick:* Building a *hybrid* sorting algorithm. The algorithms must track subarray sizes and switch to an $O(n^2)$ Insertion Sort base case when the size drops below a threshold (e.g., 30) for optimization.
*   **PA5 (Binary Search Trees):**
    *   *Core Logic:* Implementing a BST with standard insertion, search, and the three-case deletion method.
    *   *The Trick:* Augmenting the BST into an Order Statistic Tree by maintaining a `subtree_size` at each node. This allows for an efficient $O(h)$ implementation of the "k-th smallest element" query.
*   **PA6 (Binary Heaps & Priority Queues):**
    *   *Core Logic:* Implementing an array-based binary heap.
    *   *The Trick:* A mode-dependent comparator. The heap must dynamically switch between acting as a Max-Heap (Adoption Mode) and a Min-Heap (Triage Mode). This requires an $O(n)$ bottom-up heapify to recompute keys and rebuild the heap whenever the mode changes, alongside linear searches for name-based `O(\log n)` updates.

---

## 3. Foundation Exam Prep: Core Patterns

To excel on the Foundation Exam, mastery of the following algorithmic patterns is essential:

1.  **The Recursive Traversal Pattern:** Whether it's a BST, a Trie, or a Graph (floodfill), you must be able to confidently write a recursive function that includes:
    *   A base case (e.g., `if (root == NULL) return 0;`).
    *   A recursive step that aggregates data from children (`res += recursiveCall(child);`).
    *   A return statement that passes the aggregated data up the call stack.
2.  **The Array/Pointer Reassignment Pattern:** Commonly tested in Linked List and DMA questions. You must be able to visually trace and write code that inserts, deletes, or shifts elements without dropping the pointer chain (e.g., maintaining `prev` and `curr` pointers in a list).
3.  **The Master Theorem & Iteration:** Memorize the Master Theorem cases. Practice the iteration technique until you can seamlessly substitute $T(n/2)$ into the equation, identify the pattern for the $k$-th iteration, and set $k = \log_2(n)$ to solve for the final Big-O bound.
4.  **Sorting Algorithm Mechanics:** Do not just memorize the code. Memorize the *state* of the array after $k$ passes of Selection Sort, or the state of the partitions after a Quick Sort pivot. Exams frequently test algorithmic tracing over raw coding for these topics.
5.  **Bitwise Fundamentals:** Understand how to use shifts (`<<`, `>>`) and masks (`&`, `|`, `^`) to isolate specific bits, count set bits, or represent small sets, as these frequently appear in algorithmic analysis and short-coding questions.
