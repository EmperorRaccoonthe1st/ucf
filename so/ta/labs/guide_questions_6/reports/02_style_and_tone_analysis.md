# Past Guide Questions & Teaching Style Analysis

## 1. Overview of Artifacts Analyzed
- `src/prof_email.txt`: Direct instructions from the course professor regarding Lab 6, terminology, and coding philosophy.
- `src/00 Readme.pdf`: Lab leader general guidelines (session structure, consistency, answering guide questions).
- `src/Practice Problem 2 Guide Questions.pdf`: Math library linking, ASCII manipulation, digit extraction, bounds checking.
- `src/Practice Problem 3 Guide Questions.pdf`: Input buffering, `scanf` formatting, accumulator pattern, reusable variables, control flow ladders.
- `src/Practice Problem 4 Guide Questions.pdf`: ASCII validation, alphabet math, loop bounds variations, `scanf` multi-character input, loop transformations (`for` vs. `while`).
- `src/Practice Problem 5 Guide Questions.pdf`: Modular decomposition, arithmetic operators (`%`, `/`), number reversal algorithm, boundary conditions, integer overflow and type limits, block scope.

---

## 2. Key Pedagogical Tone & Style Attributes

### 2.1 Tone
- **Instructive & Direct**: Written from the perspective of a TA/lab leader guiding students during active lab sessions. Clear, confident, and explanatory.
- **Concept-Oriented**: Answers rarely provide just a raw value or code snippet; they anchor the answer in broader programming concepts (e.g., "accumulator pattern", "reusable variable", "block scope rules", "Principle of Least Privilege").
- **Student-Misconception Focused**: Answers preempt common introductory pitfalls (garbage values, uninitialized variables, integer overflow, 0-indexing, leftover newlines).

### 2.2 Content & Scope
- **Level of Abstraction**: Tailored to introductory C programming (COP3223). Avoids introducing concepts that haven't been taught yet (e.g., in PP5: *"Arrays or strings could give effectively more storage, but these haven't been taught yet"*).
- **Step-by-step Tracing**: Shows brief arithmetic demonstrations or concrete transformations when helpful:
  - PP4 Q2: `'a' - 'a' = 0 (first letter of the alphabet)`
  - PP5 Q2: `1234 % 10 = 4`, `1234 / 10 = 123`
  - PP5 Q3: `reverse = reverse * 10 + digit`
- **Exhaustive coverage of question subparts**: If a question has two parts ("What is the difference? What would happen if...?"), both parts are answered explicitly and clearly.

### 2.3 Syntax & Formatting
- **Numbering**: Matches the original numbering of the guide questions (1 through 7).
- **Structure**:
  - In PP2 & PP3, questions are numbered items with concise answers.
  - In PP4 & PP5, each question prompt is listed in bold/plain text, immediately followed by the answer explanation.
  - In the TA's draft (`guide_questions_draft.md`), numbered answers are provided directly.
- **Code Notation**:
  - Function names, variable names, and keywords are demarcated cleanly (e.g., `'print_array'`, `'n'`, `'const'`, or backticks in markdown).
  - Code snippets and list rewrites are clean, concise blocks without unnecessary boilerplate.

---

## 3. Professor's Explicit Guidance (from `prof_email.txt`)

1. **Terminology Distinction (Mandatory)**:
   - **Logical size**: How many elements are currently stored in the array.
   - **Capacity**: The physical size of the array when declared.
   - *Quote*: *"Please be consistent in using the terminology."*

2. **Function Ordering**:
   - Order of prototypes: `print_array`, `find_min_index`, `swap`, `selection_sort`.

3. **`const` Keyword Design Choice**:
   - Arrays in formal parameters of non-modifying functions must use `const` so the function does not alter the array.
   - *Quote*: *"The reason behind this one is that I do not want the function to modify the array. That is one design choice that you might notice throughout the course."*

4. **Consistency**:
   - *"You must use the answers I provided when discussing the solution to the problem. Do not deviate because I want to ensure consistency among all sections."*
