1. Capacity is the physical size of the array when declared (the total number of elements that can be held within the array, here 100).
The variable 'n' represents the logical size, which is the current number of elements actively stored within the array (here 5).
Capacity is how _much_ the array can hold while logical size is how much _it's actually holding_.
If the 'print_array' function were called with 100 passed for 'size', there would be 95 zeros output after the contents of the array (since in C, uninitialized elements in a partially initialized array default to 0), all separated by spaces on a single line.

2. In C, scalar arguments are passed by value: when 'n' is passed to a function, its value (5) is evaluated and copied into the parameter 'size'.
The variable 'n' is a local variable declared within the 'main' function, while 'size' is a local parameter of the functions utilized throughout the program.
As 'size' resides as a parameter within the scope of a function, it can be passed any arbitrary value. 
They are two different variables, occupying different areas within memory, with two different names.

3. The 'const' keyword ensures that the array elements referenced by the parameter cannot be altered from within a function.
The 'print_array' and 'find_min_index' functions do not mutate the array provided to them.
Instead, they simply perform read-only operations over the values held within the array—printing them and repeatedly comparing them, respectively.
In contrast, the 'swap' and 'selection_sort' functions actually do mutate their arrays. 
Thus they cannot use the 'const' keyword within their function prototypes, as doing so would cause a compiler error and prevent them from performing their function.
In programming, applications must follow strict design principles to ensure correct functionality throughout the lifespan of a project.
A function must not possess the ability to alter areas within memory outside of their immediate scope, unless strictly necessary.
This is known as _The Principle of Least Privilege_.

4. The function 'find_min_index(const int arr[], int start, int size)' searches the array 'arr' across indices 'start' to 'size-1' inclusive, and returns the **index** of the smallest element in that range (not the value itself).
    - The function call 'find_min_index(nums, 0, 5)' returns the index '2'.
    The function searches the values within the array from index 0 to 4: {50, 20, 10, 30, 40}. 
    It finds the minimum element is 10, which resides at index 2.

    - The function call 'find_min_index(nums, 2, 5)' returns the index '2'.
    The function searches the values within the array from index 2 to 4: {10, 30, 40}. 
    It initializes 'min_idx' to 2 (value 10) and compares it with indices 3 and 4 (values 30 and 40). Because 10 is already the minimum element across {10, 30, 40}, 'min_idx' remains 2.

5. In C, when an array is passed as an argument to a function, it decays into a pointer to its first element (passing the memory address of the original array by value).
Because the 'swap' function does not utilize the 'const' keyword within the function prototype, the 'arr' parameter is a mutable pointer to the original array.
As a result, all operations performed onto 'arr' directly affect the original array declared in 'main', allowing changes to persist even though it is technically outside the scope of the function.

6. After each pass 'i' of selection sort, the elements at the beginning of the array (from index 0 through index 'i') reside in their proper, final sorted positions.
Additionally, each of these sorted elements is guaranteed to be less than or equal to all elements remaining in the unsorted portion of the array.

7. If the array contained duplicate values, the condition 'arr[i] < arr[min_idx]' in 'find_min_index' strictly requires a smaller value to update the index. Because equal values do not satisfy this condition, 'find_min_index' will always return the index of the first instance of the duplicate minimum value in the unsorted range.
Upon the next iteration of the 'find_min_index' function within the parent 'selection_sort', the search begins past the already sorted element, allowing the function to return the next occurrence of the number, with this pattern continuing until all duplicate values are exhausted.
Ultimately, duplicate values do not affect the final result of 'selection_sort' and the array will still be correctly sorted in ascending order with duplicate values positioned consecutively.

For example, here is the output for a scenario where the following array is undergoing a selection sort:
{1, 0, 4, 5, 4} -> [0, 1, 4, 4, 5]
