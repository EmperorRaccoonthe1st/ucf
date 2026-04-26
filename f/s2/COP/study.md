# Sorting Algorithms

## Insertion Sort - **"Swap Left"**

### Pseudo-Code

1. Take first item as sorted.
2. Take `i` item and compare with the sorted part of array, heading left <-.
3. If `i` item is less/greater than `x` card then swap them.
4. Insert once correct position is found.

### Running Time

- Worst Case: O(n^2)
- Best Case: O(n)

### Code

```c
void insertion_sort(int *array, size_t size) {
    if (array == NULL || size < 2)
        return;

    for (size_t i = 1; i < size; i++) {
        int key = array[i];
        int j = (int)i - 1;

        /* Move elements of array[0..i-1] that are greater than key
           to one position ahead of their current position */
        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j--;
        }
        array[j + 1] = key;
    }
}
```

## Selection Sort - **"Switch Right"**

### Pseudo-Code

1. Start at 0
2. Find min/max & swap with `j`
3. Increment `j`

### Running Time

- Worst Case: O(n^2)
- Best Case: O(n^2)

### Code

```c
void selection_sort(int *array, size_t size) {
    if (array == NULL || size < 2)
        return;

    for (size_t i = 0; i < size - 1; i++) {
        size_t min_idx = i;

        /* Find the minimum element in the unsorted portion */
        for (size_t j = i + 1; j < size; j++) {
            if (array[j] < array[min_idx]) {
                min_idx = j;
            }
        }

        /* Swap the found minimum element with the first unsorted element */
        if (min_idx != i) {
            int temp = array[i];
            array[i] = array[min_idx];
            array[min_idx] = temp;
        }
    }
}
```

## Bubble Sort - **"Swap Right"**

### Pseudo-Code

1. Look at the first two elements and sort.
2. Move right and sort pairs.
3. Repeat `n` times.
3. Decrement `n` and repeat.

### Running Time

- Worst Case: O(n^2)
- Best Case: O(n)

### Code

```c
void bubble_sort(int *array, size_t size) {
    if (array == NULL || size < 2)
        return;

    bool swapped;
    for (size_t i = 0; i < size - 1; i++) {
        swapped = false;

        /* Inner loop for comparisons; 'size - i - 1' because 
           the last 'i' elements are already sorted */
        for (size_t j = 0; j < size - i - 1; j++) {
            if (array[j] > array[j + 1]) {
                /* Swap elements */
                int temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swapped = true;
            }
        }

        /* If no two elements were swapped by inner loop, then break */
        if (swapped == false)
            break;
    }
}
```

## Merge Sort - **"Binary Split"**

### Pseudo-Code

1. Divide arr into 2.
2. Keep dividing until many arr's of 1.
3. Merge arr's next to each other.
4. When merging place smaller object out of the two.

### Running Time

- Worst Case: O(nlgn)
- Best Case: O(nlgn)

### Code

```c
void merge(int *array, int left, int mid, int right) {
    int i, j, k;
    int n1 = mid - left + 1;
    int n2 = right - mid;

    /* Create temporary arrays */
    int *L = malloc(n1 * sizeof(int));
    int *R = malloc(n2 * sizeof(int));

    /* Copy data to temp arrays L[] and R[] */
    for (i = 0; i < n1; i++)
        L[i] = array[left + i];
    for (j = 0; j < n2; j++)
        R[j] = array[mid + 1 + j];

    /* Merge the temp arrays back into array[left..right] */
    i = 0; // Initial index of first subarray
    j = 0; // Initial index of second subarray
    k = left; // Initial index of merged subarray
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            array[k] = L[i];
            i++;
        } else {
            array[k] = R[j];
            j++;
        }
        k++;
    }
```

## Quick Sort - **"Pivot Split"**

### Pseudo-Code

1. Pick a pivot.
2. Place elements smaller to left and larger to the right.
3. Repeat for each side of the pivot

### Running Time

- Worst Case: O(nlogn)
- Best Case: O(n^2)

### Code

```c
void quick_sort(int *array, int low, int high) {
    if (low < high) {
        /* pi is partitioning index, array[pi] is now at right place */
        int pi = partition(array, low, high);

        /* Separately sort elements before and after partition */
        quick_sort(array, low, pi - 1);
        quick_sort(array, pi + 1, high);
    }
}
```

