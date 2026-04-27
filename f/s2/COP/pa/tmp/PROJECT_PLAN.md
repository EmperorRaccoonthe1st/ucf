# PROJECT_PLAN.md - PA6 Implementation Blueprint

## 1. Data Structures & Initialization
- **Enum `Mode`**: `MODE_ADOPTION = 0`, `MODE_TRIAGE = 1`.
- **Struct `Cat`**: Includes `name`, `breed`, `age`, `friendliness`, `health`, `arrival_id`, `quarantine`, and `key`.
- **Struct `CatHeap`**: Array of `Cat*`, `size`, `capacity`, and `mode`.
- **Struct `Shelter`**: Global state containing `mode`, `featured_breed` (string), `alpha`, `next_arrival_id`, and a `CatHeap`.
- **Initialization**: 
    - Read $q$ commands.
    - Initialize `Shelter` with default `MODE_ADOPTION`, `featured_breed = NULL`, `alpha = 1.0`, `next_arrival_id = 0`.
    - Initialize `CatHeap` with an initial capacity (e.g., 10) and grow using `realloc` as needed.

## 2. Core Logic & Formulae
### 2.1 Comparison Logic (The "Better" Cat)
Implement a unified `compareCats(Cat* a, Cat* b, Mode mode)` function:
- **ADOPTION (Max-Heap)**: Higher key is better.
- **TRIAGE (Min-Heap)**: Lower key is better.
- **Tie-Breakers**: 
    1. Lexicographically smaller name (`strcmp(a->name, b->name) < 0`).
    2. Smaller `arrival_id`.

### 2.2 Key Calculations
- **Adoption Key**:
    - `base = 1.6 * friendliness + 1.1 * health - 0.7 * age`
    - `mult = (strcmp(breed, featured) == 0) ? alpha : 1.0`
    - `key = (base * mult) - (1e-6 * arrival_id)`
- **Triage Key**:
    - `key = (100 - health) * 2.0 + max(0, age - 12) * 1.0 - 0.05 * friendliness`

## 3. Heap Operations
- **`percolate_up(CatHeap *h, int idx)`**: Compare with parent at `(idx - 1) / 2`.
- **`percolate_down(CatHeap *h, int idx)`**: Compare with children at `2*idx + 1` and `2*idx + 2`.
- **`insert(CatHeap *h, Cat *c)`**: Add to end, `percolate_up`.
- **`remove_at(CatHeap *h, int idx)`**: Swap with last, decrement size, then `percolate_down` AND `percolate_up` to restore order.
- **`build_heap(CatHeap *h)`**: Bottom-up heapify starting from `(size/2) - 1` down to 0.

## 4. Command Handlers
- **ADD**: Check duplicates ($O(n)$), `malloc` Cat, `strdup` strings, calculate key, `insert`.
- **UPDATE**: Find index ($O(n)$), update field. If field affects key, recompute and restore heap position ($O(\log n)$).
- **REMOVE**: Find index ($O(n)$), `remove_at`, `free` strings and struct.
- **PEEK**: Print `h->arr[0]` or "No cats available".
- **SERVE**:
    - **ADOPTION**: Extract roots until a non-quarantined cat is found. Temporarily store quarantined cats, then re-insert them.
    - **TRIAGE**: Extract and free the root cat.
- **MODE**: Update `S->mode` and `h->mode`, recompute all keys, `build_heap`.
- **FEATURED**: Update `S->featured_breed` and `S->alpha`, recompute all keys, `build_heap`.
- **PRINT k**: 
    - Create a temporary `CatHeap`.
    - Copy the pointer array (not the Cat objects).
    - Extract root $k$ times ($O(k \log n)$).
    - Free temporary pointer array.
- **QUIT**: Free all cats, strings, and the heap array.

## 5. Memory & Formatting
- **Strings**: Read into `char buffer[256]`, then `malloc(strlen(buffer) + 1)` and `strcpy`.
- **Output**: Use `%.2f` for keys and alpha. Ensure strict spacing and case sensitivity as per PDF.
- **Memory**: No leaks. Every `ADD` must be matched by a `free` (either via `REMOVE`, `SERVE`, or `QUIT`).
