1.Capacity is the total amount of objects that can be held within the array.
 The variable 'n' is the current number of objects held within the array.
Capacity is how _much_ the array can hold while size is how much _it's actually holding_.
If the 'print_array' function were called with the value of 'n' as 100, there would be 95 zeros output after the contents of the array.

2. The variable 'n' is a global variable within the main function, while 'size' is a local parameter of the functions utilized throughout the program.
As 'size' resides as a parameter within the scope of a function, it can be passed any arbitrary value. 
They are two different variables, occupying different areas within memory, with two different names.

3. The 'const' key word ensures that the object referenced by the parameter cannot be altered from within a function.
The 'print_array' and 'find_min_index' functions do not mutate the array provided to them, rather they simply perform simple operations over the values held within the array.
 Printing them and repeatedly comparing them respectively.
In  contrast, the 'swap' and 'selection_sort' functions actually do mutate their arrays. 
Thus they do not require the 'const' keyword within their function prototype as it would actively hinder their ability to perform their function.
In programming, the applications must follow strict design principles to ensure correct functionality throughout the lifespan of a project.
A function must not posses the ability to alter areas within memory outside of their immediate scope, unless strictly necessary.
This is know as _The Principle of Least Privilege_.

4.  The function 'find_min_index(const int arr[], int start, int size)' searches the array 'arr' on the range 'start+1' to 'size-1'.
    - The function call 'find_min_index(nums, 0, 5)' would return the value '10'.
    The function searches the values within the array 1 to 4. 
    It finds the minimum element across {20, 10, 30, 40}, with '10' as the minimum.

    - The function call 'find_min_index(nums, 2, 5)' would return the value '30'.
    The function searches the values within the array 3 to 4. 
    It finds the minimum element across {30, 40}, with '30' as the minimum.

5. The 'swap' function does not utilize the 'const' keyword within the function prototype.
As a result the 'arr' parameter inside of the 'swap' function is a mutable reference to the original array which allows all operations performed onto the parameter to affect the variable, even though it is technically outside the scope of the function.

6. The element at the beginning of an array undergoing selection sort reside in their proper, sorted position.

7. If the array contained duplicate values then the function 'find_min_index' would return the next first instance of the duplicated value.
Upon the next iteration of the 'find_min_index' function within the parent 'selection_sort' the function would return the next occurrence of the number, with this pattern continuing until all duplicate values are exhausted.

For example, here is the output for a scenario where the following array is undergoing a selection sort.
{1, 0, 4, 5, 4} -> [0, 1, 4, 4, 5]
