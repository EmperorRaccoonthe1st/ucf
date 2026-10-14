# Practice Problem 6: Ground Truth Analysis & Reference Answers

## 1. Overview of Practice Problem 6
- **Assignment**: Lab Practice Problem 6 (`practice6.c`)
- **Core Algorithm**: Selection Sort on a 1D array of integers in ascending order.
- **Key Concepts Tested**:
  - Array capacity vs. logical size.
  - Pass-by-value of scalars (`size`) vs. passing arrays (array decay to pointers).
  - Scope of local variables in `main()` vs. function parameters.
  - Function modularity (`print_array`, `find_min_index`, `swap`, `selection_sort`).
  - Const-correctness and the Principle of Least Privilege.
  - Array indexing, search ranges, and return values (index vs. element value).
  - In-place mutation and sorting invariants.
  - Handling duplicates and algorithm stability/correctness.

---

## 2. Code Breakdown & Invariants

### 2.1 State in `main()`
```c
int nums[100] = {50, 20, 10, 30, 40};
int n = 5;
```
- **Capacity**: 100 elements (physical allocated size).
- **Logical Size**: 5 elements (`n`), representing the elements currently processed/populated.
- **Uninitialized elements**: Indices `5` to `99`. Under C99/C11 §6.7.9, when an aggregate has an initializer list shorter than its size, all remaining elements are implicitly initialized to zero (`0`).

---

### 2.2 Function Specifications & Signatures

#### `void print_array(const int arr[], int size)`
```c
void print_array(const int arr[], int size) {
    for(int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
```
- **Parameters**: `const int arr[]` (read-only), `int size`.
- **Behavior**: Prints `arr[0]` to `arr[size - 1]` followed by space, terminated by newline.
- If called with `size = 100`, prints:
  `50 20 10 30 40 0 0 0 ... 0\n` (5 original elements followed by 95 zeros).

#### `int find_min_index(const int arr[], int start, int size)`
```c
int find_min_index(const int arr[], int start, int size) {
    int min_idx = start;
    for(int i = start + 1; i < size; i++) {
        if(arr[i] < arr[min_idx]) {
            min_idx = i;
        }
    }
    return min_idx;
}
```
- **Parameters**: `const int arr[]`, `int start`, `int size`.
- **Return Value**: The **index** (not the value) of the minimum element in `arr[start ... size - 1]`.
- **Comparison**: Strictly less than (`<`). If `arr[i] == arr[min_idx]`, `min_idx` does not update. Thus, it finds the **first** occurrence of the minimum value in the range.

#### `void swap(int arr[], int i, int j)`
```c
void swap(int arr[], int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}
```
- **Parameters**: `int arr[]` (mutable), `int i`, `int j`.
- **Behavior**: Exchanges elements at index `i` and index `j` in place.
- **Mechanism**: Modifies the caller's array directly because `arr` is passed as a pointer to the array's first element.

#### `void selection_sort(int arr[], int size)`
```c
void selection_sort(int arr[], int size) {
    for(int i = 0; i < size - 1; i++) {
        int min_idx = find_min_index(arr, i, size);
        if(min_idx != i) {
            swap(arr, i, min_idx);
        }
    }
}
```
- **Outer Loop**: Runs from `i = 0` to `size - 2` ($size - 1$ passes).
- **Invariant**: After pass `i`, elements `0` through `i` are in their final, sorted positions and are less than or equal to all elements in `i + 1` through `size - 1`.

---

## 3. Ground Truth Answers for Guide Questions

### Question 1
**Prompt**: The array `nums` has a capacity of 100 elements, but `n` is 5. What is the difference between these two values? What would happen if `print_array(nums, 100)` were called?
- **Capacity (100)**: The physical size / total allocated storage of the array in memory as declared (`nums[100]`).
- **Logical size (`n = 5`)**: The number of elements currently stored and actively in use by the program.
- **Effect of `print_array(nums, 100)`**: In C, when an array is partially initialized, the remaining elements are automatically initialized to `0`. Calling `print_array(nums, 100)` would print the first 5 elements (`50 20 10 30 40`) followed by 95 zeros (`0`), each separated by a space.

### Question 2
**Prompt**: The variable `n` in `main()` is passed to functions with a parameter named `size`. Why does this work even though the names are different?
- **Pass-by-value**: In C, scalar arguments (like `int`) are passed by value. The calling expression evaluates `n` (which is `5`) and copies that value into the function's parameter `size`.
- **Scope & Independence**: `n` is a local variable scoped to `main()`, while `size` is a local parameter scoped to the function. Parameter names are internal identifiers for the function's implementation; their names do not need to match the variable names used in the caller.

### Question 3
**Prompt**: Why is `const` used in the array parameters of `print_array()` and `find_min_index()`, but not in `swap()` and `selection_sort()`?
- **Read-only vs. Mutable**: `print_array()` only reads and displays the elements, and `find_min_index()` only reads and compares elements. Neither function should modify the array, so declaring `const int arr[]` enforces read-only access and prevents accidental changes.
- **Mutation Required**: `swap()` and `selection_sort()` exist specifically to modify the contents and reorder the array in place. If `const` were applied, the compiler would prevent assignments to `arr[i]`.
- **Design Principle**: This adheres to the **Principle of Least Privilege** (a function should only have access and permissions strictly necessary to perform its task) and provides compile-time safety.

### Question 4
**Prompt**: Given the initial array values, what will the following function calls return? Explain your answers.
`find_min_index(nums, 0, 5)`
`find_min_index(nums, 2, 5)`
- **Array contents**: `nums = {50, 20, 10, 30, 40}`
  - Index 0: 50
  - Index 1: 20
  - Index 2: 10
  - Index 3: 30
  - Index 4: 40
- **`find_min_index(nums, 0, 5)`**:
  - Search range: indices `0` to `4` (elements `50, 20, 10, 30, 40`).
  - Smallest element is `10`, which is located at index `2`.
  - **Returns `2`** (the function returns the index, not the value).
- **`find_min_index(nums, 2, 5)`**:
  - Search range: indices `2` to `4` (elements `10, 30, 40`).
  - The function assumes `min_idx = 2` (`nums[2] = 10`), then compares with index 3 (`30`) and index 4 (`40`).
  - Neither is smaller than `10`, so `min_idx` remains `2`.
  - Smallest element is `10`, located at index `2`.
  - **Returns `2`** (returns the index, not the value).

### Question 5
**Prompt**: Why do changes made to the array inside `swap()` also affect the original array in `main()`?
- **Array decay / Pointer passing**: In C, when an array is passed as an argument to a function, it decays into a pointer to its first element (`&arr[0]`).
- The function receives the memory address of the original array rather than a duplicate copy.
- Therefore, when `swap()` modifies `arr[i]` and `arr[j]`, it writes directly to the memory locations of `nums` in `main()`.

### Question 6
**Prompt**: After each pass of selection sort, what can you conclude about the elements at the beginning of the array?
- After pass $i$, the first $i + 1$ elements (indices `0` through `i`) are placed in their final, sorted positions.
- In addition, every element in this sorted prefix is less than or equal to all elements in the remaining unsorted portion of the array (indices $i + 1$ to $size - 1$).

### Question 7
**Prompt**: Suppose the array contains duplicate values. How would this affect the behavior of `find_min_index()` and the final result of `selection_sort()`?
- **Behavior of `find_min_index()`**: Because the function uses the strict comparison `if (arr[i] < arr[min_idx])`, encountering an element equal to the current minimum does not update `min_idx`. Therefore, it returns the index of the **first** occurrence of the minimum value within the search range.
- **Behavior of `selection_sort()`**: In the next iteration, the search range starts one index higher, allowing subsequent occurrences to be found and placed in turn.
- **Final result**: `selection_sort()` still correctly sorts the entire array in ascending order, placing identical values consecutively.
