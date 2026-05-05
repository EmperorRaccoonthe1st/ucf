# Sorting Algorithms

## Insertion Sort - **"Swap Left"**

### Pseudo-Code

for i:1 -> n
    key = arr:i
    j = i--

    while j > -1 & arr:j > key
        arr:j++ = arr:j
        j--

    arr:j++ = key

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

for i -> n
    min = i
    for j:i++ -> n
        if arr:j < arr:min
            min = j

    swap min & i

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

for i -> n--
    for j -> n - i--
        if arr:j > arr:j++
            swap j & j++

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

    if l < r then
    
    m = l + (r-l)/2

    sort(l, m)
    sort(m++, r)

    merge(l, m, r)

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

if (l < h) then

p = partition(l, h)

sort(l, p--)
sort(p++, h)

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

## Partition
p //from some source random/high/low
i = l--

for j:l -> h--
    if arr:j < p
        i++
        swap j & i

swap i++ & h

ret i++


# Recurrence Relations

1. aT(n/b) + C(n) -> func:0
2. n/b -> bod:0
3. Plug bod:0 into func:0 -> bod:1
4. Plug bod:1 into func:0 -> func:2
5. Body of func:2 -> bod:2
6. Plug bod:2 into func:0 -> body:3
7. Plug bod:3 into func:2 -> func:3

8. Find pattern of func:3 -> func:4
9. Solve for k; set function to 0 or 1
10. Plug definition of k back into func:4 -> func:5
11. Find O() of func:5
