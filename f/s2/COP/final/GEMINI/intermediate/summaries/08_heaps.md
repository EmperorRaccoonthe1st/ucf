# Topic: Heaps

## 1. Theoretical Core

**Definitions & Properties:**
- **Binary Heap:** A complete binary tree that strictly follows a specific heap property. A complete binary tree has all levels fully populated except possibly the last, where leaves are placed as far left as possible.
- **Min-Heap Property:** The value of an arbitrary node must be less than or equal to the value of its children. The root inherently contains the smallest element in the tree.
- **Max-Heap Property:** The value of an arbitrary node must be greater than or equal to the value of its children. The root contains the largest element.

**Array Representation (0-Indexed):**
Binary heaps are efficiently implemented using 0-indexed arrays without using linked pointers.
Given a node at index `i`:
- **Index of Left Child:** `2 * i + 1`
- **Index of Right Child:** `2 * i + 2`
- **Index of Parent:** `(i - 1) / 2` (integer division, taking the floor)
*Note: Child node indices must be strictly validated as `< size`, while parent indices must be `>= 0`.*

**Key Operations & Time Complexity:**
- **Heapify / Percolate Down:** Pushes a node down the tree to its correct position to maintain the heap property. Used during deletion (Extract-Min) or when building a heap. Time Complexity: **O(log n)** in the worst case (height of the tree).
- **Percolate Up / Heapify Up:** Pushes a newly inserted or decreased node up the tree. Used during insertion or decrease-key operations. Time Complexity: **O(log n)**.
- **Build-Heap (Floyd's Method):** A bottom-up approach to build a heap from an unsorted array by calling `Heapify` on all internal nodes. Precise Time Complexity: **O(n)**.
- **Heap Insertion:** Elements are placed at the next available slot (end of the array) and percolated up. Time Complexity: **O(log n)**.

## 2. Mathematical Proof: O(n) Build-Heap

The `BuildHeap` operation takes **O(n)** time in the worst case. This can be proven by summing the effort of calling `Heapify` on all internal nodes.

Let $n$ be the number of nodes in the heap, and $h = \lfloor \lg n \rfloor$ be the height of the tree. 
We focus our analysis on the internal nodes at levels $0, 1, \dots, k$, where $k = h - 1$. The leaf nodes (at level $h$) require zero effort because they have no children.
At any given level $i$, there are $2^i$ nodes. The effort for `Heapify` at level $i$ depends on the height of the node, which is $h - i$ (the maximum number of swaps to reach a leaf).

The total effort $S$ is represented by the following summation:
$$S = \sum_{i=0}^{k} 2^i (h - i)$$
Where:
- $2^i$ is the number of nodes at level $i$.
- $(h - i)$ is the worst-case effort (number of swaps) for a node at level $i$.
- $k = h - 1$ is the deepest level of internal nodes.

**Deriving the Closed-Form:**
Expand the summation:
$$S = 2^0(h) + 2^1(h-1) + 2^2(h-2) + \dots + 2^{k-1}(2) + 2^k(1)$$

Multiply $S$ by 2:
$$2S = 2^1(h) + 2^2(h-1) + 2^3(h-2) + \dots + 2^k(2) + 2^{k+1}(1)$$

Subtract $S$ from $2S$, aligning the powers of 2:
$$2S - S = -h + 2^1(1) + 2^2(1) + 2^3(1) + \dots + 2^k(1) + 2^{k+1}(1)$$
$$S = -h + \sum_{i=1}^{k+1} 2^i$$

Adjust the summation to start at $i=0$:
$$S = -h + \left( \sum_{i=0}^{k+1} 2^i \right) - 2^0$$
$$S = -h + \left( \sum_{i=0}^{k+1} 2^i \right) - 1$$

The closed-form for the geometric series $\sum_{i=0}^{k+1} 2^i$ is $2^{k+2} - 1$. Substituting this in:
$$S = -h + (2^{k+2} - 1) - 1 = -h + 2^{k+2} - 2$$

Substitute $k = h - 1$:
$$S = -h + 2^{(h-1)+2} - 2 = -h + 2^{h+1} - 2$$

Since $h = \lfloor \lg n \rfloor$, we substitute $h$ back in using $\lg n$:
$$S = -\lg n + 2^{\lg n + 1} - 2$$

Using the properties of exponents and logarithms ($2^{\lg n} = n$):
$$S = -\lg n + (2^{\lg n} \cdot 2^1) - 2$$
$$S = -\lg n + 2n - 2$$

In the resulting expression $2n - \lg n - 2$, the dominant term is $2n$. Thus, doing an informal Big-O analysis, the `BuildHeap` operation runs in **O(n)** time in the worst case.

## 3. Algorithmic Tracing

**Trace: Building a Min-Heap using Floyd's Method (O(n))**
Given an unsorted array: `[4, 1, 9, 2, 16, 5, 10, 14, 3, 7]` with a `size = 10`.

1. **Identify the last internal node:** The parent of the last node (`size - 1 = 9`). Its index is `(9 - 1) / 2 = 4`. The value at index 4 is `16`.
2. **Level-wise backward Heapify (from index 4 down to 0):**
   - **`i = 4` (value 16):** Left child `7` (idx 9). `7 < 16`, so swap. Array becomes: `[4, 1, 9, 2, 7, 5, 10, 14, 3, 16]`.
   - **`i = 3` (value 2):** Children `14` (idx 7), `3` (idx 8). `2` is already the minimum. No swap.
   - **`i = 2` (value 9):** Children `5` (idx 5), `10` (idx 6). Minimum is `5`. `5 < 9`, so swap. Array: `[4, 1, 5, 2, 7, 9, 10, 14, 3, 16]`.
   - **`i = 1` (value 1):** Children `2` (idx 3), `7` (idx 4). `1` is the minimum. No swap.
   - **`i = 0` (value 4):** Children `1` (idx 1), `5` (idx 2). Minimum is `1`. `1 < 4`, so swap. Array: `[1, 4, 5, 2, 7, 9, 10, 14, 3, 16]`.
     - *Recursively Heapify the swapped node `4` at `idx = 1`:* Children `2` (idx 3), `7` (idx 4). Min is `2`. Swap. Array: `[1, 2, 5, 4, 7, 9, 10, 14, 3, 16]`.
     - *Recursively Heapify `4` at `idx = 3`:* Children `14` (idx 7), `3` (idx 8). Min is `3`. Swap. Final Array: `[1, 2, 5, 3, 7, 9, 10, 14, 4, 16]`.

The array now perfectly conforms to the Min-Heap property.

## 4. Code Implementation

```c
// Heapify Down (Percolate Down) for a Min-Heap
void percolateDown(int *arr, int size, int idx) {
    int min = idx;
    int left_idx = 2 * idx + 1;
    int right_idx = 2 * idx + 2;

    // Check if left child exists and is strictly less than current min
    if (left_idx < size && arr[left_idx] < arr[min]) {
        min = left_idx;
    }
    // Check if right child exists and is strictly less than current min
    if (right_idx < size && arr[right_idx] < arr[min]) {
        min = right_idx;
    }

    // If the minimum is not the current node, swap and recurse down
    if (min != idx) {
        int tmp = arr[idx];
        arr[idx] = arr[min];
        arr[min] = tmp;
        
        percolateDown(arr, size, min);
    }
}

// Insertion into a Min-Heap (Heapify Up / Percolate Up)
void insert(int *arr, int *size, int capacity, int val) {
    // Prevent overflow
    if (*size >= capacity) {
        return; 
    }
    
    // Step 1: Insert element at the end of the array (last slot)
    int idx = *size;
    arr[idx] = val;
    (*size)++;
    
    // Step 2: Percolate Up
    int parent_idx = (idx - 1) / 2;
    // Swap with parent while the heap property is violated
    while (idx > 0 && arr[idx] < arr[parent_idx]) {
        // Swap values
        int tmp = arr[idx];
        arr[idx] = arr[parent_idx];
        arr[parent_idx] = tmp;
        
        // Move pointers up the tree
        idx = parent_idx;
        parent_idx = (idx - 1) / 2;
    }
}
```

## 5. Skills & Pitfalls

**Must-Know Skills:**
- Understanding the difference between `Heapify Up` (used for insertions/decreasing keys) and `Heapify Down` (used for deletion/extract-min and building a heap).
- Converting smoothly between the logical tree structure and its flat array representation.

**Common Mistakes (Pitfalls):**
- **Off-by-one errors in Index Math:** Mixing up 0-indexed formulas (`2i + 1`, `(i-1)/2`) with 1-indexed formulas (`2i`, `i/2`). In a 0-indexed heap, calculating the parent as `i/2` instead of `(i-1)/2` is a fatal logic error.
- **Out of Bounds Errors:** Failing to check if child indices (`2i + 1` or `2i + 2`) are strictly `< size` during a percolate-down operation.
- **Big-O Confusion:** Confusing the optimal **O(n)** time complexity of `Build-Heap` (using Floyd's bottom-up method) with the naive **O(n log n)** time complexity of building a heap by repeatedly inserting items one by one.
- **Heap Sort Array Output:** Forgetting that performing `extract-min` on a min-heap to repeatedly put elements at the end of the array results in a *descending* sorted array. An extra reverse pass is needed for an ascending array (or use a Max-Heap instead).