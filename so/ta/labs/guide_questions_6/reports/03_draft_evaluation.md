# Evaluation of Initial Draft Answers (`guide_questions_draft.md`)

## 1. Overview
This document evaluates the TA's initial draft against the ground truth derived from `practice6.c`, previous answer keys, and the professor's explicit instructions in `prof_email.txt`.

The guiding directive is:
> *Draft a refinement which is factually accurate, follows my distinctive writing style, & is in line with the previous answer keys provided. Attempt to keep as much as my original source text as possible, only edit where absolutely necessary.*

---

## 2. Question-by-Question Evaluation

### Question 1: Capacity vs. Logical Size & Calling `print_array(nums, 100)`
- **Original Draft**:
  ```markdown
  1.Capacity is the total amount of objects that can be held within the array.
   The variable 'n' is the current number of objects held within the array.
  Capacity is how _much_ the array can hold while size is how much _it's actually holding_.
  If the 'print_array' function were called with the value of 'n' as 100, there would be 95 zeros output after the contents of the array.
  ```
- **Strengths**:
  - The intuitive explanation (*"how much the array can hold while size is how much it's actually holding"*) is concise and captures the student-friendly voice.
  - Correctly recognizes that 95 zeros will be printed after the array contents due to zero-initialization of remaining elements.
- **Deficiencies & Corrections Needed**:
  - **Terminology**: The professor explicitly requires using the terms **"capacity"** (physical size upon declaration) and **"logical size"** (elements currently stored). The draft refers to "objects" (which sounds like OOP/Java/C++ rather than C) and doesn't explicitly pair $n$ with the term **logical size**.
  - **Clarity on the function call**: The prompt asks *"What would happen if print_array(nums, 100) were called?"* The draft states *"with the value of 'n' as 100"*, but $n$ remains 5; 100 is passed directly as the `size` argument. It should state that the first 5 elements (`50 20 10 30 40`) are printed followed by 95 zeros, all separated by spaces on a single line.
- **Refinement Strategy**: Preserve the author's exact sentences and italic emphasis, adjust "objects" to "elements", explicitly introduce "logical size", and refine the phrasing on `print_array`.

---

### Question 2: Scope and Parameter Passing (`n` vs. `size`)
- **Original Draft**:
  ```markdown
  2. The variable 'n' is a global variable within the main function, while 'size' is a local parameter of the functions utilized throughout the program.
  As 'size' resides as a parameter within the scope of a function, it can be passed any arbitrary value. 
  They are two different variables, occupying different areas within memory, with two different names.
  ```
- **Strengths**:
  - Correctly points out that they are two different variables residing in different areas of memory with distinct scopes.
- **Critical Factual Errors**:
  - **CRITICAL**: Stating *"'n' is a global variable within the main function"* is factually incorrect in C.
    1. Variables declared inside `main()` have **block scope / local scope** to `main()`. There is no such thing as a "global variable within the main function".
    2. The assignment instructions explicitly state: *"Do not use global variables."* Calling `n` a global variable will confuse students.
  - **Missing Core Mechanism**: The explanation should clearly state that in C, arguments are passed **by value**—meaning the *value* of `n` (5) is copied into the parameter `size`.
- **Refinement Strategy**: Correct "global variable within the main function" to "local variable declared in `main()`", explain pass-by-value, and preserve the rest of the author's text.

---

### Question 3: Purpose of `const` in Array Parameters
- **Original Draft**:
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
- **Strengths**:
  - Outstanding conceptual rationale, correctly citing the **Principle of Least Privilege**.
  - Clearly differentiates read-only functions from mutating functions.
  - Matches the professor's note about intentional use of `const`.
- **Minor Errors & Typos**:
  - Typos: "key word" -> "keyword", "posses" -> "possess", "know as" -> "known as", fragmented sentence ("Printing them...").
  - Precision: "do not require the 'const' keyword" -> they *cannot* have `const`, because marking them `const` would cause compiler errors when attempting to swap/sort elements.
- **Refinement Strategy**: Retain virtually all text, fix typos and sentence fragmentation, and ensure technical precision.

---

### Question 4: Return Values of `find_min_index`
- **Original Draft**:
  ```markdown
  4.  The function 'find_min_index(const int arr[], int start, int size)' searches the array 'arr' on the range 'start+1' to 'size-1'.
      - The function call 'find_min_index(nums, 0, 5)' would return the value '10'.
      The function searches the values within the array 1 to 4. 
      It finds the minimum element across {20, 10, 30, 40}, with '10' as the minimum.

      - The function call 'find_min_index(nums, 2, 5)' would return the value '30'.
      The function searches the values within the array 3 to 4. 
      It finds the minimum element across {30, 40}, with '30' as the minimum.
  ```
- **Critical Factual Errors**:
  - **CRITICAL 1**: The draft states that the functions return the **values** `'10'` and `'30'`.
    - **Reality**: The function returns the **index**, NOT the value!
    - For `find_min_index(nums, 0, 5)`: The minimum element is 10 at **index 2**. It returns **`2`**.
    - For `find_min_index(nums, 2, 5)`: It returns **`2`**!
  - **CRITICAL 2**: Misunderstanding the search range.
    - The draft claims `find_min_index` searches `start+1` to `size-1` and ignores `start`.
    - In reality, `int min_idx = start;` initializes the minimum to the element at `start`. The loop from `start + 1` to `size - 1` compares each subsequent element against `arr[min_idx]`. Thus, the search range is **from `start` to `size - 1`, inclusive**!
    - In `find_min_index(nums, 2, 5)`:
      - `start = 2`, so `min_idx` starts at 2 (`nums[2] = 10`).
      - It checks index 3 (`30`) and index 4 (`40`). Neither is smaller than 10.
      - Therefore, the minimum element in `{10, 30, 40}` is `10` at index `2`.
      - It returns **`2`**, NOT `30`!
- **Refinement Strategy**: Completely correct the return values to `2` for both calls, correct the explanation to show that the range includes `start` (indices `start` to `size - 1`), emphasize that the function returns the **index** rather than the element value, while keeping the author's bullet-point and set notation format.

---

### Question 5: Why `swap()` Affects the Original Array in `main()`
- **Original Draft**:
  ```markdown
  5. The 'swap' function does not utilize the 'const' keyword within the function prototype.
  As a result the 'arr' parameter inside of the 'swap' function is a mutable reference to the original array which allows all operations performed onto the parameter to affect the variable, even though it is technically outside the scope of the function.
  ```
- **Strengths**:
  - Recognizes that `arr` allows mutation of the caller's array.
- **Deficiencies**:
  - Not having `const` is merely a permission, not the underlying *mechanism*.
  - In C, the mechanism is **array decay to a pointer**: when an array is passed to a function, C passes the base address (a pointer to the first element, `&arr[0]`).
  - C does not have pass-by-reference language syntax like C++; passing an array passes a pointer by value, which allows the function to dereference and directly mutate the caller's memory.
- **Refinement Strategy**: Keep the author's structure, explain that passing an array passes the base memory address (array decay to a pointer), allowing direct modification of the original elements in `main()`.

---

### Question 6: State of the Beginning of the Array After Each Pass
- **Original Draft**:
  ```markdown
  6. The element at the beginning of an array undergoing selection sort reside in their proper, sorted position.
  ```
- **Strengths**:
  - Captures the basic concept.
- **Deficiencies**:
  - Grammatical disagreement ("The element ... reside").
  - Under-specified: It should state that after pass $i$, the first $i + 1$ elements are in their final, sorted positions, and they are also guaranteed to be less than or equal to all elements in the remaining unsorted portion.
- **Refinement Strategy**: Polish grammar, preserve the author's sentence, and add the full invariant.

---

### Question 7: Behavior with Duplicate Values
- **Original Draft**:
  ```markdown
  7. If the array contained duplicate values then the function 'find_min_index' would return the next first instance of the duplicated value.
  Upon the next iteration of the 'find_min_index' function within the parent 'selection_sort' the function would return the next occurrence of the number, with this pattern continuing until all duplicate values are exhausted.

  For example, here is the output for a scenario where the following array is undergoing a selection sort.
  {1, 0, 4, 5, 4} -> [0, 1, 4, 4, 5]
  ```
- **Strengths**:
  - Great intuitive description and concrete example trace.
- **Deficiencies**:
  - Needs to explain the underlying code mechanism: `if (arr[i] < arr[min_idx])` uses a strict inequality (`<`). When an identical value is found, the condition is false, so `min_idx` retains the index of the *first* occurrence in the unsorted range.
  - Explicitly confirm that the final result of `selection_sort()` is unaffected in correctness—it still successfully sorts the entire array in ascending order.
- **Refinement Strategy**: Retain the author's text and example almost verbatim, adding the brief note on the strict `<` check and confirming that sorting succeeds.
