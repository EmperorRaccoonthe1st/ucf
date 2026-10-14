# Refinement Changelog & Rationales

This document details every specific edit made to the TA's draft (`guide_questions_draft.md`), tracking changes against the original text and providing pedagogical, technical, and stylistic rationales.

---

## Question 1
### Original Draft
```markdown
1.Capacity is the total amount of objects that can be held within the array.
 The variable 'n' is the current number of objects held within the array.
Capacity is how _much_ the array can hold while size is how much _it's actually holding_.
If the 'print_array' function were called with the value of 'n' as 100, there would be 95 zeros output after the contents of the array.
```

### Refined Text
```markdown
1. Capacity is the physical size of the array when declared (the total number of elements that can be held within the array, here 100).
The variable 'n' represents the logical size, which is the current number of elements actively stored within the array (here 5).
Capacity is how _much_ the array can hold while logical size is how much _it's actually holding_.
If the 'print_array(nums, 100)' function call were executed, it would print the 5 initialized elements followed by 95 zeros (since uninitialized elements in a partially initialized array default to 0 in C), all separated by spaces on a single line.
```

### Rationale
- **Terminology Alignment**: Aligned directly with the professor's explicit directive in `prof_email.txt`: *"Logical size basically just means how many elements are currently stored in the array, while capacity is the physical size of the array when we declared it. Please be consistent in using the terminology."*
- **Vocabulary**: Replaced "objects" with "elements" (appropriate for C arrays).
- **Function Call Specifics**: Clarified that calling `print_array(nums, 100)` prints the 5 initialized numbers followed by 95 zeros due to C partial-initialization rules.
- **Preservation**: Retained the author's distinctive sentence *"Capacity is how _much_... while [logical] size is how much _it's actually holding_"*.

---

## Question 2
### Original Draft
```markdown
2. The variable 'n' is a global variable within the main function, while 'size' is a local parameter of the functions utilized throughout the program.
As 'size' resides as a parameter within the scope of a function, it can be passed any arbitrary value. 
They are two different variables, occupying different areas within memory, with two different names.
```

### Refined Text
```markdown
2. In C, arguments are passed by value: when 'n' is passed to a function, its value (5) is copied into the function's parameter 'size'.
The variable 'n' is a local variable declared in the 'main' function, while 'size' is a local parameter scoped specifically to the function being called.
As 'size' resides as a parameter within the scope of its own function, it can be passed any arbitrary value.
They are two different variables, occupying different areas within memory, with two different names.
```

### Rationale
- **Correction of Critical Factual Error**: Variables declared inside `main()` are **local** variables, not "global variables within the main function". Furthermore, the assignment instructions explicitly mandate: *"Do not use global variables."* Calling `n` global would introduce severe misconceptions for students.
- **Core Principle Added**: Explicitly identified **pass-by-value**, explaining why having different names works.
- **Preservation**: Preserved the entire second and third sentences of the author's original explanation verbatim.

---

## Question 3
### Original Draft
```markdown
3. The 'const' key word ensures that the object referenced by the parameter cannot be altered from within a function.
The 'print_array' and 'find_min_index' functions do not mutate the array provided to them, rather they simply perform simple operations over the values held within the array.
 Printing them and repeatedly comparing them respectively.
In  contrast, the 'swap' and 'selection_sort' functions actually do mutate their arrays. 
Thus they do not require the 'const' keyword within their function prototype as it would actively hinder their ability to perform their function.
In programming, the applications must follow strict design principles to ensure correct functionality throughout the lifespan of a project.
A function must not posses the ability to alter areas within memory outside of their immediate scope, unless strictly necessary.
This is know as _The Principle of Least Privilege_.
```

### Refined Text
```markdown
3. The 'const' keyword ensures that the array elements referenced by the parameter cannot be altered from within a function.
The 'print_array' and 'find_min_index' functions do not mutate the array provided to them; rather, they simply perform read-only operations over the values held within the array—printing them and repeatedly comparing them, respectively.
In contrast, the 'swap' and 'selection_sort' functions actually must mutate the array to reorder elements.
Thus, they cannot use the 'const' keyword in their function prototypes, as doing so would cause compiler errors when attempting to modify array elements.
In programming, applications must follow strict design principles to ensure correct functionality throughout the lifespan of a project.
A function must not possess the ability to alter areas within memory outside of its immediate scope unless strictly necessary.
This is known as _The Principle of Least Privilege_.
```

### Rationale
- **Grammar & Typos**: Fixed "key word" -> "keyword", "posses" -> "possess", "know as" -> "known as", and repaired the sentence fragment ("Printing them...").
- **Technical Accuracy**: "do not require the 'const' keyword" was changed to "cannot use the 'const' keyword", because attempting to mutate a const array results in a compilation failure.
- **Preservation**: Kept virtually the entire text, the architectural tone, and the citation of *The Principle of Least Privilege*.

---

## Question 4
### Original Draft
```markdown
4.  The function 'find_min_index(const int arr[], int start, int size)' searches the array 'arr' on the range 'start+1' to 'size-1'.
    - The function call 'find_min_index(nums, 0, 5)' would return the value '10'.
    The function searches the values within the array 1 to 4. 
    It finds the minimum element across {20, 10, 30, 40}, with '10' as the minimum.

    - The function call 'find_min_index(nums, 2, 5)' would return the value '30'.
    The function searches the values within the array 3 to 4. 
    It finds the minimum element across {30, 40}, with '30' as the minimum.
```

### Refined Text
```markdown
4. The function 'find_min_index(const int arr[], int start, int size)' searches the array 'arr' over the range of indices from 'start' to 'size - 1' inclusive, and returns the **index** of the smallest element in that range (not the value itself).
    - The function call 'find_min_index(nums, 0, 5)' returns the index '2'.
    The function evaluates elements from index 0 to 4: {50, 20, 10, 30, 40}.
    The smallest value in this range is 10, which is located at index 2.

    - The function call 'find_min_index(nums, 2, 5)' returns the index '2'.
    The function evaluates elements from index 2 to 4: {10, 30, 40}.
    It initializes 'min_idx' to index 2 (value 10) and compares it with indices 3 and 4 (values 30 and 40).
    Because 10 is already the smallest value in this range, 'min_idx' remains unchanged, returning index 2.
```

### Rationale
- **Correction of Critical Factual Errors**:
  1. The function returns the **index**, not the element value. Returning '10' and '30' is incorrect; both calls return index **`2`**.
  2. The search range includes `start` (from `start` to `size - 1`). The loop begins at `start + 1` only because `min_idx` is already initialized to `start`.
  3. In `find_min_index(nums, 2, 5)`, `nums[2] = 10` is part of the range. The elements evaluated are `{10, 30, 40}`, so the minimum is 10 at index 2 (not 30).
- **Preservation**: Preserved the sub-bullet format, code set representations (`{50, 20, 10, 30, 40}`), and structural cadence.

---

## Question 5
### Original Draft
```markdown
5. The 'swap' function does not utilize the 'const' keyword within the function prototype.
As a result the 'arr' parameter inside of the 'swap' function is a mutable reference to the original array which allows all operations performed onto the parameter to affect the variable, even though it is technically outside the scope of the function.
```

### Refined Text
```markdown
5. In C, when an array is passed as an argument to a function, it decays into a pointer to its first element (passing the memory address of the original array by value).
Because 'swap' does not use the 'const' keyword, the 'arr' parameter is a mutable pointer to the original array in 'main'.
All operations performed using 'arr[i]' and 'arr[j]' directly modify the underlying memory locations of 'nums', allowing the changes to persist outside the scope of the function.
```

### Rationale
- **Technical Accuracy**: "Mutable reference" is C++ terminology; in C, arrays decay into pointers to their first elements (`&arr[0]`). Incorporating the pointer/memory address mechanism explains *why* the changes affect `nums` in `main()`.
- **Preservation**: Retained the original argument connecting the lack of `const` with the ability to mutate memory outside the function's scope.

---

## Question 6
### Original Draft
```markdown
6. The element at the beginning of an array undergoing selection sort reside in their proper, sorted position.
```

### Refined Text
```markdown
6. After each pass 'i' of selection sort, the elements at the beginning of the array (from index 0 up to index 'i') reside in their final, sorted positions.
Additionally, each of these elements is guaranteed to be less than or equal to all elements remaining in the unsorted portion of the array.
```

### Rationale
- **Grammar**: Fixed subject-verb disagreement ("The element... reside" -> "the elements... reside").
- **Completeness**: Added the full loop invariant: not only are indices $0$ to $i$ sorted, but they are also $\le$ all elements in the remaining unsorted portion.
- **Preservation**: Built directly upon the author's exact phrase: *"reside in their proper, sorted position"*.

---

## Question 7
### Original Draft
```markdown
7. If the array contained duplicate values then the function 'find_min_index' would return the next first instance of the duplicated value.
Upon the next iteration of the 'find_min_index' function within the parent 'selection_sort' the function would return the next occurrence of the number, with this pattern continuing until all duplicate values are exhausted.

For example, here is the output for a scenario where the following array is undergoing a selection sort.
{1, 0, 4, 5, 4} -> [0, 1, 4, 4, 5]
```

### Refined Text
```markdown
7. If the array contains duplicate values, the condition 'arr[i] < arr[min_idx]' in 'find_min_index' strictly requires a smaller value to update the index. Because equal values do not satisfy this condition, 'find_min_index' always returns the index of the first occurrence of the minimum value within the search range.
Upon subsequent passes of 'selection_sort', the 'start' index increments past previously placed elements, allowing the function to find and place the next occurrence of the duplicate value.
Ultimately, duplicate values do not affect the correctness of 'selection_sort'—the array will still be properly sorted in ascending order with identical values placed consecutively.

For example, here is the output for a scenario where an array with duplicates undergoes selection sort:
{1, 0, 4, 5, 4} -> {0, 1, 4, 4, 5}
```

### Rationale
- **Code Grounding**: Clarified the role of the strict inequality (`<`) in `find_min_index`.
- **Completeness**: Explicitly confirmed that `selection_sort()` still achieves full sorting correctness.
- **Preservation**: Preserved the author's explanation of sequential passes exhausting duplicates and kept the concrete example trace verbatim.
