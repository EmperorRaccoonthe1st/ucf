# Phase 1 Extraction: Sorting Algorithms

## 1. Theoretical Core

### Elementary Sorting Algorithms
*   **Selection Sort:** Divides the array into sorted and unsorted regions. Repeatedly searches the unsorted region for the minimum element and swaps it into the correct location, growing the sorted region from left to right.
*   **Insertion Sort:** Assumes the first element is sorted. For each subsequent element, it finds its correct location in the sorted area by shifting larger elements to the right and inserting the current element.
*   **Bubble Sort:** Pushes (bubbles) the "heaviest" (largest) element of the unsorted region toward the end by repeatedly swapping adjacent elements that are out of order.

### Divide and Conquer Sorting Algorithms
*   **Merge Sort:** A strategy that recursively divides the array in half until sub-arrays are of size 1. Then, it conquers the sub-problems by merging the sorted sub-arrays back together.
*   **Quick Sort:** Chooses a **pivot** element (e.g., the last element) and partitions the array such that all elements less than or equal to the pivot are on its left, and all greater are on its right. It then recursively sorts the left and right partitions. No explicit combine step is needed.

## 2. Time & Space Complexities and Stability

| Sorting Algorithm | Best-Case Time | Average Time | Worst-Case Time | Space Complexity | Is Stable? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Selection Sort** | O(n²) | O(n²) | O(n²) | O(1) | No |
| **Insertion Sort** | O(n) | O(n²) | O(n²) | O(1) | Yes |
| **Bubble Sort** | O(n²) / O(n)* | O(n²) | O(n²) | O(1) | Yes |
| **Merge Sort** | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| **Quick Sort** | O(n log n) | O(n log n) | O(n²) | O(log n)** | No |

*\* O(n) best-case for an enhanced Bubble Sort that stops if no swaps occur.*
*\*\* O(log n) average space for recursion stack; O(n) worst-case.*

## 3. Algorithmic Tracing

### Merge Sort Trace
**Initial Array:** `[38, 27, 43, 3, 9, 82, 10]`
1.  **Divide:** `[38, 27, 43, 3]` and `[9, 82, 10]`
2.  **Divide:** `[38, 27]`, `[43, 3]`, `[9, 82]`, `[10]`
3.  **Divide:** down to individual elements.
4.  **Merge:** `[27, 38]` and `[3, 43]` -> `[3, 27, 38, 43]`
5.  **Merge:** `[9, 82]` and `[10]` -> `[9, 10, 82]`
6.  **Final Merge:** `[3, 27, 38, 43]` and `[9, 10, 82]` -> `[3, 9, 10, 27, 38, 43, 82]`

### Quick Sort Trace (Partitioning)
**Initial Array:** `[8, 3, 1, 7, 0, 10, 2]`
*   **Pivot:** `2` (last element)
*   **i = 0:** `8 > 2` (No swap)
*   **i = 1:** `3 > 2` (No swap)
*   **i = 2:** `1 <= 2` (Swap `arr[0]` and `arr[2]`) -> `[1, 3, 8, 7, 0, 10, 2]`
*   **i = 3:** `7 > 2` (No swap)
*   **i = 4:** `0 <= 2` (Swap `arr[1]` and `arr[4]`) -> `[1, 0, 8, 7, 3, 10, 2]`
*   **i = 5:** `10 > 2` (No swap)
*   **End loop:** Swap pivot `arr[6]` with `arr[2]` (first element > pivot).
*   **Result:** `[1, 0, 2, 7, 3, 10, 8]`
*   **Partitions:** Left `[1, 0]`, Pivot `2`, Right `[7, 3, 10, 8]`.

## 4. Code Implementation

### Merge Sort: Merge Step
*Adapted from `pa4.c`*
```c
void merge(int arr[], int low, int mid, int high) {
    int size = high - low + 1;
    int *tmp = malloc(size * sizeof(int));
    
    int i = low;
    int j = mid; // In this specific implementation, 'mid' acts as start of right half
    int p = 0;

    // Compare and merge
    while (i < mid && j <= high) {
        if (arr[i] <= arr[j]) {
            tmp[p++] = arr[i++];
        } else {
            tmp[p++] = arr[j++];
        }
    }

    // Fill remaining elements
    while (i < mid) tmp[p++] = arr[i++];
    while (j <= high) tmp[p++] = arr[j++];

    // Copy back to original array
    for (int x = low, pos = 0; x <= high; x++, pos++) {
        arr[x] = tmp[pos];
    }
    
    free(tmp);
}
```

### Quick Sort: Partition Step
*Adapted from `pa4.c`*
```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // Choosing the last element as pivot
    int j = low - 1; // Index of the smaller element
    
    for (int i = low; i <= high - 1; i++) {
        if (arr[i] <= pivot) {
            j++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    } 

    // Swap pivot to its final correct position
    int temp = arr[j + 1];
    arr[j + 1] = arr[high];
    arr[high] = temp;
    
    return j + 1; // Return the partition index
}
```

## 5. Skills & Pitfalls

*   **Common Mistake: Quick Sort Worst-Case Scenario:** A major pitfall is triggering the O(n²) worst-case running time. This occurs when the chosen pivot results in extremely unbalanced partitions (e.g., repeatedly picking the maximum or minimum element). This commonly happens when using the last element as the pivot on an already sorted or reverse-sorted array. Randomizing the pivot or using "median of three" helps avoid this.
*   **Common Mistake: Merge Sort's Extra Space:** A frequent pitfall is forgetting that Merge Sort requires O(n) auxiliary space for the `tmp` array during the combine step. Because it is not an in-place sorting algorithm, it can cause memory overhead compared to Quick Sort.
*   **Must-Know Skill: Partition Tracing:** Understanding the two-pointer approach (often `i` and `j`) in Quick Sort's partition is a critical exam skill. You must be prepared to trace exactly which elements are swapped at each step during an iteration.