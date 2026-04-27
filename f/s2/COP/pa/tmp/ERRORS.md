# ERRORS.md - PA6 Plan Evaluation

The following errors and misconceptions were identified in `@pa6_Plan.md` during the architectural review.

## 1. Heap Logic & Structure
- **Invalid Swapping:** `swapIndex` attempts to swap `int` values instead of `Cat *` pointers, which will lead to memory corruption or crashes.
- **Incorrect Parent Index:** `percolate_up` uses `(index/2)-1`. The correct formula for a 0-indexed array-based binary heap is `(index - 1) / 2`.
- **Missing Tie-Breakers:** The plan ignores the required tie-breakers: "lexicographically smaller name, then smaller arrival_id".
- **OOB Error:** `remove_from_heap` accesses `S->heap->arr[S->heap->size]`, which is out of bounds after decrementing the size. It should use `S->heap->arr[S->heap->size-1]`.
- **Heapify Direction:** `recompute_all_keys_and_build` should perform a bottom-up heapify (starting from the last non-leaf node) to be $O(n)$.

## 2. Mathematical Inaccuracies
- **Triage Key:** The plan uses `(100 - c->health) * (2 + max(0, (c->age - 12))) * (1 - (0.05 * c->friendliness))`. The PDF specifies additions/subtractions: `(100 - health) * 2.0 + max(0, age - 12) * 1.0 - 0.05 * friendliness`.
- **Adoption Key:** 
    - The plan applies the `mult` to the `arrival_id` penalty. The PDF formula is `(base * mult) + (-10^-6 * arrival_id)`.
    - `10e-6` is used, which is $10 \times 10^{-6}$ ($10^{-5}$). The PDF requires $10^{-6}$.
- **Featured Breed:** For the "NONE" case, `alpha` should be reset to `1.0`, not `0`.

## 3. Command Logic Errors
- **`cmd_serve` (Adoption):** The while loop lacks a break after serving the first eligible cat. It would attempt to adopt every non-quarantined cat in one call.
- **`cmd_print`:** 
    - The plan clones the `Shelter` pointer but not the underlying heap data, making the operation destructive to the main heap.
    - It leaks memory by not freeing the temporary heap.
- **`cmd_mode`:** Uses `strcpy` for string comparison instead of `strcmp`.
- **`cmd_update`:** Recomputes *all* keys ($O(n)$) when only one cat's key needs to be updated and its position restored ($O(\log n)$).

## 4. Requirement Deviations
- **String Handling:** The plan doesn't account for the requirement to read names/breeds into a temporary buffer before `malloc` and `strcpy`.
- **Prototypes:** Several helper functions (like `swapIndex`) use `Shelter *S` instead of the specified `CatHeap *` or `Cat *` where appropriate.
- **Global State:** The `Shelter` struct in the plan is treated as a pointer that needs allocation, whereas the PDF implies it contains the `CatHeap` struct directly.
