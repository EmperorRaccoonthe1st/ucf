# Topic: C Review & Dynamic Memory Allocation

## 1. Theoretical Core
### Core Concepts
* **Pointers**: A variable that stores a memory address as its value. Pointers allow direct manipulation of memory, efficient data sharing between functions (pass by reference), and referring to large data structures compactly. The `&` operator (address-of) retrieves the memory address of a variable, and the `*` operator (dereference) accesses or manipulates the value stored at that location.
* **Structs**: A custom data type defined using the `struct` keyword that allows grouping related variables (members/fields) of different data types into a single unit. It is often used alongside `typedef` to create aliases for easier reference.
* **Dynamic Memory Allocation (DMA)**: Allocating memory at runtime from the heap space when the required size is unknown at compile time.
    * `malloc()`: Allocates a specified number of bytes on the heap and returns a void pointer to it. The allocated memory is uninitialized.
    * `calloc()`: Allocates memory for an array of elements and initializes all bytes to zero.
    * `realloc()`: Resizes a previously allocated memory block, preserving its content up to the minimum of the old and new sizes.
    * `free()`: Deallocates dynamically allocated memory, releasing it back to the heap to prevent memory leaks.

## 2. Algorithmic Tracing
### Dynamically Allocating a 2D Array
1. Determine the number of rows and columns needed.
2. Define a double pointer variable (e.g., `int **arr`).
3. Call `malloc()` to allocate an array of pointers (one for each row) and assign the result to the double pointer: `arr = malloc(rows * sizeof(int *));`.
4. Iterate over each row pointer (`i` from 0 to `rows - 1`).
5. Inside the loop, call `malloc()` to allocate memory for the columns and assign it to the current row pointer: `arr[i] = malloc(cols * sizeof(int));`.

### Freeing a 2D Array
1. Iterate over each row pointer (`i` from 0 to `rows - 1`).
2. Call `free()` on each row array: `free(arr[i]);`.
3. Finally, call `free()` on the array of pointers itself: `free(arr);`.

## 3. Code Implementation
The following snippet, inspired by `pa1.c` and `lab1.c`, demonstrates dynamic memory allocation (including a 2D array) and the correct usage of struct member access operators:

```c
// Struct definitions demonstrating the dot (.) and arrow (->) operators
typedef struct Song_s {
    int song_id;
    char title[101];
} Song;

typedef struct Cat_s {
    char *name;         // Dynamically allocated string
    int age;
} Cat;

void allocate_and_access() {
    // Dot operator (.) usage with a struct instance
    Song s;
    s.song_id = 101;

    // Arrow operator (->) usage with a pointer to a struct
    Cat *cat = malloc(sizeof(Cat));
    cat->age = 5;
    
    // Remember to free dynamically allocated struct instances
    free(cat);
}

// 2D Array Dynamic Allocation & Deallocation
void manage_2d_array(int rows, int cols) {
    // 1. Allocation
    int **matrix = malloc(rows * sizeof(int *));
    for (int i = 0; i < rows; i++) {
        matrix[i] = malloc(cols * sizeof(int));
    }
    
    // 2. Deallocation
    for (int i = 0; i < rows; i++) {
        free(matrix[i]); // Free each row
    }
    free(matrix); // Free the array of pointers
}
```

## 4. Skills & Pitfalls
### Must-Know Skills
* **Arrow vs. Dot Operator**: Use the dot operator (`.`) to access members of a struct variable (e.g., `list.count`). Use the arrow operator (`->`) to access members when you have a pointer to a struct (e.g., `list->count`), which is shorthand for `(*list).count`.
* **Pointer Arithmetic**: Understand the precedence of pointer arithmetic. `*(arr + i)` correctly dereferences the `i`-th element, whereas `*arr + i` dereferences the first element and adds `i` to its value.
* **Constructors and Destructors**: Modularize code by defining helper functions to handle the allocation (e.g., `createStore`) and deallocation (e.g., `freeStore`) of complex dynamic structures to reduce the risk of memory leaks.

### Common Mistakes (Pitfalls)
* **Memory Leaks**: Occur when dynamically allocated memory is no longer needed but is not released using `free()`. Every `malloc()` should have a corresponding `free()`.
* **Dangling Pointers**: Continuing to use a pointer after the memory it points to has been freed.
* **Segmentation Faults**: Run-time errors caused by memory access violations, such as dereferencing an invalid memory location or an uninitialized pointer. Always initialize pointers to `NULL` and check them defensively (e.g., `if (ptr != NULL)`) before dereferencing.
