# CODE_GUIDELINES.md - Style Replication Rules

To ensure the code appears hand-written by the user, all implementation must adhere to these strict rules:

## 1. Documentation & Comments
- **NO COMMENTS:** Zero internal comments. No "FIX", "TODO", or explanatory notes.
- **NO CITATIONS:** Do not cite logic sources, PDFs, or AI assistance.
- **HEADER ONLY:** Only the mandatory authorship comment at the top of the file is allowed.

## 2. Logic & Structure
- **VERBOSE LOGIC:** Prefer manual loops and explicit steps over succinct expressions. 
    - *Example:* When removing an item from an array, manually loop and shift elements instead of using `memmove`.
- **DECOUPLED RETURNS:** Never call a function or perform math inside a `return` statement.
    - *Bad:* `return compute_key(c);`
    - *Good:* `double val = compute_key(c); return val;`
- **EXPLICIT ALLOCATION:** Always follow the `buff` -> `strlen` -> `malloc` -> `strcpy` pattern for strings.
- **VARIABLE NAMES:** Use `tmp`, `buff`, `amt`, `val`, `cur`, `ptr`, `n`, `i`, `x`, `y`.

## 3. Formatting
- **Standard Spacing:** Use standard indentation and single spaces around operators.
- **No Refactoring:** Keep the logic "flat." Do not try to be overly clever with macros or bitwise operations unless the user specifically did so in examples.
