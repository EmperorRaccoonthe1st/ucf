# Sorting Algorithms

## Insertion Sort

### Pseudo-Code

1. Take first item as sorted.
2. Take `i` item and compare with the sorted part of array, heading left <-.
3. If `i` item is less/greater than `x` card then swap them.
4. Insert once correct position is found.

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

### Running Time

- Worst Case: O(n^2)
- Best Case: O(n)

## Selection Sort

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

## Bubble Sort

### Pseudo-Code

1. 

### Running Time

- Worst Case: O()
- Best Case: O()

### Code

```c

```

## Merge Sort

### Pseudo-Code

1. 

### Running Time

- Worst Case: O()
- Best Case: O()

### Code

```c

```

## Quick Sort

### Pseudo-Code

1. 

### Running Time

- Worst Case: O()
- Best Case: O()

### Code

```c

```

