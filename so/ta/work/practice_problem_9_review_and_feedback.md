# Editorial Review and Pedagogical Audit: Practice Problem 9 Guide Questions

- **Reviewed Document**: `/home/owen/ucf/so/ta/work/practice_problem_9_guided_question_answers.md`
- **Source Specification**: `11 COP3223 Practice Problem 9.pdf` (`practice9.c`)
- **Course Corpus References**: Practice Problems 2 through 8 Guide Questions, Lab Guidelines, Lecture Conventions
- **Evaluation Purpose**: Editorial feedback and technical validation for lab session delivery, Google Docs compilation, and PDF export.

---

## 1. Executive Summary & Audit Scorecard

The draft provides strong conceptual intuition, particularly regarding Luhn's algorithm indexing, the Principle of Least Privilege with `const`, pass-by-value stack dynamics, and the necessity of multi-field date validation.

However, a strict technical audit reveals several critical C-specific inaccuracies that must be addressed before presenting this to COP3223 students:
1. **Integer Overflow & Data Representation (Q1)**: Omits the primary architectural reason a 16-digit card number cannot be an `int` in C (32-bit integer overflow) and the loss of leading zeros.
2. **Storage Duration Misconception (Q2)**: Repeatedly terms regular local variables and pass-by-value parameters as "_statically allocated_". In C, `CreditCard c;` inside `main` is an **automatic variable** allocated on the stack frame. "Static allocation" in C refers strictly to variables with static storage duration (`static` keyword or global scope).
3. **Struct Member Data Type Error (Q2 & Q7)**: Identifies `number` as an "`int` array `number[]`" and "number integer array". The struct explicitly defines it as a character array: `char number[17]`.
4. **ASCII Arithmetic Inaccuracy (Q6)**: States `'7':7 - '0':0 = 7`. In ASCII, `'0'` is decimal 48 (not 0) and `'7'` is decimal 55 (not 7). ASCII 0 is the null character `'\0'`. This is a classic beginner misconception.
5. **Array Decay and Pointer Phrasing (Q7)**: Mentions that `c.number` is "a point to the first element". It should be phrased as array decay into a pointer to its first element (`&c.number[0]`).
6. **Context Alignment (Q5)**: Uses a sample date with days (`7-09-2026`) instead of grounding the example in the lab's predefined macro constants (`CURRENT_MONTH 11`, `CURRENT_YEAR 2026`).

### Audit Scorecard

| Question | Corpus Alignment | Technical Validity | Phrasing & Clarity | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Q1: String vs. Int** | [WARN] Partial | [WARN] Incomplete | [OK] Strong intuition | Needs overflow & leading zero context |
| **Q2: Member Access** | [WARN] Missing prompts | [FAIL] Factual errors | [WARN] Misleading terms | Fix "static allocation" and "int array" |
| **Q3: Pass-by-Value** | [PASS] Aligned | [PASS] Accurate | [WARN] Minor typo | Fix "effect" -> "affect" |
| **Q4: Const Struct** | [PASS] Aligned | [PASS] Accurate | [OK] Good analysis | Elaborate on embedded array constness |
| **Q5: Expiration Logic** | [PASS] Aligned | [OK] Accurate logic | [WARN] Date mismatch | Ground in CURRENT_MONTH/YEAR macros |
| **Q6: Character Math** | [PASS] Aligned | [FAIL] Major ASCII bug | [WARN] Misconception | Correct ASCII values (55 - 48 = 7) |
| **Q7: Address-of & Arrays** | [PASS] Aligned | [FAIL] Data type bug | [WARN] Minor typos | Correct "integer array" to "char array" |

---

## 2. Markdown Formatting Audit & Applied Fixes

In accordance with your explicit directive, the source file `practice_problem_9_guided_question_answers.md` has been modified **strictly for Markdown formatting standards**, leaving 100% of the textual content untouched.

### Applied Formatting Fixes
1. **Trailing Whitespace Removal**:
   - Stripped invisible trailing spaces from line 1, line 24, and line 53.
2. **List Separation & Spacing**:
   - Inserted a blank line preceding the bullet list in Question 5 (`For example with the following values:\n\n- Current Date...`). In standard CommonMark/GFM parsers and Google Docs markdown import, omitting this blank line can cause bullet points to render as broken inline text.
3. **Google Docs / PDF Readiness**:
   - When importing or pasting this document into Google Docs, ensure that code snippets maintain a fixed-width font (e.g., Roboto Mono or Courier New) and that list numbering does not auto-restart unpredictably.

---

## 3. Course Corpus & Pedagogical Comparison

### Consistency with Previous Answer Keys (PP2 through PP8)
- **Question Prompts**: Past answer keys (e.g., Practice Problems 4, 5, 7, and 8) consistently print the **full question prompt** directly above the explanation. Including the prompts makes the final PDF self-contained and significantly easier for students to follow during lab discussions.
- **Concrete Numeric Traces**: When explaining arithmetic or data representation, the course corpus favors step-by-step numeric traces (e.g., PP4 Q2: `'a' - 'a' = 0`, PP5 Q2: `1234 % 10 = 4`, PP8 Q1: null terminators and capacity). Grounding Q1, Q5, and Q6 in explicit numbers directly mirrors this established teaching style.
- **Terminology Precision**: As emphasized in prior labs and the professor's notes, technical terms (e.g., logical size vs. capacity, block scope, array decay, automatic storage) must be used with exactitude to avoid confusing students ahead of exams.

---

## 4. Question-by-Question Detailed Review & Editorial Recommendations

### Question 1: String vs. Integer for Card Numbers

#### Original Prompt
> Why is the card number stored as a string rather than an integer? How does this make it easier to process individual digits when applying Luhn's algorithm?

#### Current Draft Text
```text
1. We store the number within the _Credit Card_ struct as a string rather than an integer to allow for ease of access for single digits within the card. 
Luhn's algorithm requires repeated access of an arbitrary single digit, a process when implemented on an integer uses a series of verbose mathematical manipulations.
It is significantly simpler to store the number as a string & access each digit using an index, completely bypassing the mathematical manipulations required of the former solution.
```

#### Technical Validity & Accuracy Audit
- **Critical Omission (Data Range & Overflow)**:
  - In C, a standard signed `int` is 32 bits, holding a maximum value of `2,147,483,647` (at most 10 digits). A 16-digit credit card number (e.g., `5555555555554444`) exceeds this capacity and causes an immediate integer overflow.
  - Even if a 64-bit integer (`long long`) were used, storing the number as an integer strips **leading zeros** (e.g., a card beginning with `0` would lose its prefix, altering the digit count and invalidating the checksum).
  - Practice Problem 5 Question 6 explicitly taught students about integer overflow and data limits. Connecting Q1 back to that principle reinforces the course curriculum.
- **Luhn Processing Accuracy**:
  - The draft correctly notes that indexing an array (`card.number[i]`) is far simpler than repeatedly extracting digits mathematically via `% 10` and `/ 10`.

#### Technical Phrasing & Accessibility
- "verbose mathematical manipulations" is expressive, but in COP3223, specifying "repeated modulo (`% 10`) and division (`/ 10`)" anchors it to the exact operations students implemented in Practice Problems 2 and 5.
- Name the typedef properly: `CreditCard` rather than `Credit Card`.

#### Proposed Editorial Refinement
```markdown
1. Why is the card number stored as a string rather than an integer? How does this make it easier to process individual digits when applying Luhn's algorithm?

There are two primary reasons for storing the card number as a string:
- **Integer Overflow and Leading Zeros**: A 16-digit card number far exceeds the maximum limit of a standard 32-bit `int` in C (which maxes out at 2,147,483,647, or 10 digits). Attempting to store a 16-digit number as an `int` causes integer overflow. Additionally, an integer data type automatically discards leading zeros, which would corrupt any card number beginning with '0'.
- **Direct Digit Access**: Luhn's algorithm requires processing individual digits from left to right. If the number were stored as an integer, accessing an arbitrary digit would require repeated mathematical operations (modulo `% 10` and integer division `/ 10`). Storing the card number as a string allows us to access any digit directly in constant time via array indexing (`card.number[i]`), completely bypassing arithmetic manipulations.
```

---

### Question 2: Accessing Members of `card`

#### Original Prompt
> How do you access the number, month, and year members of a CreditCard variable named card?

#### Current Draft Text
```text
2. The variable described named `card` is a `CreditCard` struct saved in memory.
This struct has three members: an `int` month, an `int` year, & and `int` array number[].
The assignment instructs us to _statically allocate_ each struct and insert the information from a file into it, and within each function the struct is _passed by value_.
Thus when implementing each function, and in the `main` function, we are accessing a _statically allocated_ struct.

To access the contents of a _statically allocated_ struct we use the _dot operator_ (`.`), like so:
```c
card.number;
card.month;
card.year;
```

If we were to instead access the struct through a pointer we would utilize the _arrow operator_ (`->`).
```

#### Technical Validity & Accuracy Audit
- **CRITICAL FLAW (Storage Duration)**:
  - Calling `card` a "_statically allocated_ struct" is factually incorrect in C.
  - A variable declared inside `main` (like `CreditCard c;`) or received as a parameter has **automatic storage duration** (allocated on the runtime stack frame).
  - In C, "static allocation" specifically denotes static storage duration (variables declared with the `static` keyword or globals declared outside functions), which persist in data/BSS memory for the lifetime of the program.
  - The dot operator (`.`) is used because `card` is a **direct structure variable / instance**, not because of where or how it was allocated.
- **CRITICAL FLAW (Data Type)**:
  - Line 6 states: `& and `int` array number[]`.
  - The member `number` is a **character array** (`char number[17]`), NOT an `int` array.
- **Grammar/Typo**:
  - `& and `int` array` contains an accidental duplication of the conjunction.

#### Technical Phrasing & Accessibility
- Keep the distinction simple for students: use the **dot operator (`.`)** when operating directly on a structure variable. Use the **arrow operator (`->`)** when accessing members through a structure pointer (`ptr->member`, shorthand for `(*ptr).member`).

#### Proposed Editorial Refinement
```markdown
2. How do you access the number, month, and year members of a CreditCard variable named card?

Because `card` is a direct structure variable (not a pointer), we access its members using the **dot operator** (`.`):
```c
card.number;
card.month;
card.year;
```

The `CreditCard` structure contains three members: two scalar integers (`int month`, `int year`) and one character array (`char number[17]`). 

If `card` were instead a pointer to a structure (e.g., `CreditCard *card`), we would dereference and access its members using the **arrow operator** (`->`), such as `card->number`.
```

---

### Question 3: Pass-by-Value and Struct Mutation

#### Original Prompt
> Each required function receives a structure by value. If a function changes card.month, does that change the original variable passed by main()? Explain.

#### Current Draft Text
```text
3. To _pass a structure by value_ C creates a copy of the struct and provides it to the function.
This copy is a completely different object in memory, residing further down in the _function call stack_.
If the function did alter this copy then the change would not effect the original in any capacity.
When the function returns, all memory held within the _function stack frame_ is released, which removes all changes to the copy of the struct which occurred during the execution of the function.
```

#### Technical Validity & Accuracy Audit
- **Validity**: [PASS] The conceptual explanation is accurate. In C, pass-by-value copies the entire structure into the called function's stack frame. Modifications to the copy have no effect on the caller's structure.
- **Direct Answer**: The prompt asks a yes/no question ("does that change the original variable...?"). Adding an explicit **No** at the very beginning makes the answer crisp and easy to grade.
- **Diction Error**:
  - "would not effect the original" -> `effect` is a noun; the correct verb is `affect`.
- **Call Stack Terminology**:
  - "residing further down in the function call stack" depends on architecture (stacks grow downwards on x86, but upwards on some architectures). Saying "residing in the called function's separate stack frame" is universally accurate and standard for COP3223.

#### Proposed Editorial Refinement
```markdown
3. Each required function receives a structure by value. If a function changes card.month, does that change the original variable passed by main()? Explain.

**No**, it does not change the original variable in `main()`.

When a structure is passed by value, C makes a complete, independent copy of the entire structure and places it in the called function's stack frame. Any modifications made to `card.month` inside the function affect only this local copy. 

Because the original variable in `main()` occupies a completely separate location in memory, it remains unchanged. When the function returns, its stack frame is deallocated, discarding the local copy and any changes made to it.
```

---

### Question 4: Const-Qualified Structure Parameters

#### Original Prompt
> If is_valid_number() declares its parameter as const CreditCard card in the function definition, can it assign a new value to card.month or change a character in card.number?

#### Current Draft Text
```text
4. **No**, it cannot. 
The function receives the struct through _pass-by-value_ in the standard manner, but if the `const` keyword is applied to the parameter the copied struct becomes immutable.
As the local copy of the struct within the _function stack frame_ is now immutable, each member within the struct is now immutable as well.
You are unable to reassign nor alter an variable that is immutable, and attempting to do so will result in a compilation error.
```

#### Technical Validity & Accuracy Audit
- **Validity**: [PASS] The answer is fundamentally correct.
- **Important Technical Nuance**:
  - The question explicitly asks about both `card.month` (a scalar) and `card.number` (an array).
  - Why is modifying `card.number[i]` prevented? Because `number` is an **embedded array** inside the struct (`char number[17]`), not a pointer. In C, marking a struct `const` makes every byte within the struct const-qualified. Thus, `card.number` becomes an array of `const char`. Attempting to modify `card.number[i]` or assign to `card.month` results in a compilation error.
- **Grammar & Phrasing**:
  - "an variable" -> "a variable".
  - "unable to reassign nor alter" -> "unable to reassign or alter".

#### Proposed Editorial Refinement
```markdown
4. If is_valid_number() declares its parameter as const CreditCard card in the function definition, can it assign a new value to card.month or change a character in card.number?

**No**, it can do neither.

Applying the `const` keyword to the parameter makes the entire structure instance read-only within the function. Because all members of a const-qualified structure inherit this read-only status:
- Assigning a new value to `card.month` (e.g., `card.month = 12;`) is prohibited.
- Modifying any character within `card.number` (e.g., `card.number[0] = '4';`) is also prohibited because `number` is an embedded array within the struct, making its elements `const char`.

Attempting to mutate either member will cause a compilation error.
```

---

### Question 5: Multi-Field Expiration Validation

#### Original Prompt
> Why must the expiration check consider both the month and the year? Give an example in which comparing only the month would produce an incorrect result.

#### Current Draft Text
```text
5. A credit card expires when the current date is greater than the month and year marked on the back of the card.
To check a date in this manner requires comparing both the month and the year to the one listed.
Only checking a single value would result in an incomplete comparison.
For example with the following values:

- Current Date: 7-09-2026
- Expiration: 8-2025

Only checking the month in this scenario would result in a false positive.
Even though the expiration month is greater than the current month, it's actually an entire year behind and the card has been expired **for a whole year**.
```

#### Technical Validity & Accuracy Audit
- **Corpus & Assignment Alignment**:
  - The assignment defines fixed reference constants:
    `#define CURRENT_MONTH 11`
    `#define CURRENT_YEAR 2026`
  - The draft introduces an arbitrary current date (`7-09-2026`) with a day field (`09`). Credit cards only have month and year. Grounding the example directly in `11/2026` reinforces the student's code.
- **Completeness of Error Modes**:
  - Comparing only the month can produce two types of errors:
    1. **False Positive**: An expired card appears valid (e.g., Expiration `12/2025` has month `12 > 11`, but expired last year).
    2. **False Negative**: A valid card appears expired (e.g., Expiration `05/2027` has month `5 < 11`, but is valid next year).
  - Highlighting this demonstrates why the comparison must be hierarchical: year first, then month only if years match.

#### Proposed Editorial Refinement
```markdown
5. Why must the expiration check consider both the month and the year? Give an example in which comparing only the month would produce an incorrect result.

An expiration date is a hierarchical two-dimensional value: the year represents the primary time interval, and the month represents the secondary sub-interval. Because the 12-month calendar cycle repeats every year, comparing only the month completely ignores the passage of years.

Using the program's reference date (**November 2026**, where `CURRENT_MONTH = 11` and `CURRENT_YEAR = 2026`):
- **False Positive Example**: Suppose a card expired in **December 2025** (`12/2025`).
  - If we compare only months, `12 >= 11` evaluates to true, incorrectly classifying the card as valid.
  - In reality, the card expired an entire year ago.
- **False Negative Example**: Suppose a card expires in **March 2027** (`03/2027`).
  - If we compare only months, `3 < 11` evaluates to false, incorrectly classifying the card as expired even though it remains valid for months to come.

Therefore, the check must evaluate the year first. The month is only compared when the card's expiration year matches `CURRENT_YEAR`.
```

---

### Question 6: Character Arithmetic (`'7' - '0'`)

#### Original Prompt
> Why does '7' - '0' produce the integer 7?

#### Current Draft Text
```text
6. This calculation functions identically to the familiar `alpha - 'a'` equation that we use to find the offset of characters within the alphabet.
Each numeric character utilizes an _ASCII Code_ when represented as `char`.
The series of numeric characters begins with '0' and runs until the character '9', so the first character '0' has an offset of 0 and every following numeric character increases their offset by 1.
In this manner, each character has an offset that directly maps to their numeric value.

When attempting to find the offset, or numeric value, of the character '7' we find the difference between that 'char' and the first object in the sequence, '0'.
Thus the calculation '7':7 - '0':0 = 7, when _typecasted_ to `int`.
```

#### Technical Validity & Accuracy Audit
- **CRITICAL FACTUAL ERROR (ASCII Values)**:
  - Line 46 states: `Thus the calculation '7':7 - '0':0 = 7, when _typecasted_ to `int`.`
  - In ASCII:
    - `'0'` does NOT have the value `0`. Its ASCII code is **48**.
    - `'7'` does NOT have the value `7`. Its ASCII code is **55**.
    - The null character `'\0'` has the value `0`.
  - Stating `'0':0` reinforces the exact beginner misconception this question was designed to dispel!
  - The expression `'7' - '0'` performs `55 - 48 = 7`.
- **C Standard Guarantee**:
  - The C Standard (§5.2.1) explicitly guarantees that the decimal digits `'0'` through `'9'` are contiguous and sequential. Because `'0'` is the base, subtracting `'0'` yields the true numerical value.
- **Typecasting Misconception**:
  - In C, character constants like `'7'` and `'0'` already have type `int` (character constants are `int` literals in C, not `char`). No "typecasting" takes place.

#### Proposed Editorial Refinement
```markdown
6. Why does '7' - '0' produce the integer 7?

In C, characters are represented internally by their integer ASCII values. In the ASCII character set:
- The character `'0'` has an ASCII value of **48**.
- The character `'7'` has an ASCII value of **55**.

The C standard guarantees that the numeric characters `'0'` through `'9'` are arranged contiguously and sequentially in memory. When we subtract `'0'` from `'7'`, the compiler evaluates the difference between their underlying ASCII values:
```text
'7' - '0'  ==>  55 - 48  ==>  7
```

Because `'0'` is the baseline digit, subtracting `'0'` yields the exact zero-indexed offset of any digit character, cleanly converting the `char` digit into its corresponding `int` value.
```

---

### Question 7: Use of `&` with Struct Members in `fscanf()`

#### Original Prompt
> When reading the struct members using fscanf(), why do the integer members require &, while the character array member does not?

#### Current Draft Text
```text
7. The _dot_ operator accesses the value of a member in a certain struct, it does not return the address of that member in memory.
As `fscanf()` requires addresses to locations in memory to store file input, the members receiving data must utilize the _address-of_ operator to conform the requirements of the function.

In our program we attempt to place two integers from the input file into the members `c.month` and `c.year`, both of these evaluate to their integer value when accessed through the _dot_ operator and thus require the use of the _address-of_ operator.

Within `fscanf()` the `c.number` member also evaluates to the value stored in memory, which is a point to the first element of the number integer array.
As the value of the `c.number` member is already a pointer there is no need to utilize the _address-of_ operator when placing attempting to place input into it.
```

#### Technical Validity & Accuracy Audit
- **CRITICAL FACTUAL ERROR (Data Type)**:
  - Line 53 states: `"number integer array"`.
  - As in Question 2, `number` is a **character array** (`char number[17]`), not an integer array.
- **Typo**:
  - Line 53: `"which is a point to the first element"` -> should be `"a pointer"`.
  - Line 54: `"when placing attempting to place"` -> repeated words / stutter.
- **Array Decay Mechanics**:
  - The explanation should explicitly mention **array decay**: in C, when an array expression (like `c.number`) is passed to a function, it automatically decays into a pointer to its first element (`&c.number[0]`). Because it already evaluates to a memory address, prefixing it with `&` is unnecessary.
  - In contrast, `c.month` and `c.year` are scalar `int` variables. Without `&`, their current values would be passed by value, leading to undefined behavior or segmentation faults when `fscanf` attempts to dereference them as memory addresses.

#### Proposed Editorial Refinement
```markdown
7. When reading the struct members using fscanf(), why do the integer members require &, while the character array member does not?

The `fscanf()` function requires memory addresses as arguments so it knows where to store the data read from the input file.

- **Integer Members (`&c.month`, `&c.year`)**:
  `c.month` and `c.year` are scalar `int` variables. When accessed with the dot operator, the expression `c.month` evaluates to the integer value stored inside that variable. To give `fscanf()` the location in memory where the new value should be written, we must explicitly apply the **address-of operator** (`&`).

- **Character Array Member (`c.number`)**:
  `c.number` is an array of characters (`char number[17]`). In C, an array name used in an expression automatically **decays into a pointer to its first element** (`&c.number[0]`). Because `c.number` already evaluates to the memory address of the buffer where string characters will be placed, the address-of operator `&` is not needed.
```

---

## 5. Consolidated Clean Version (Ready for Google Docs & PDF Export)

Below is the complete, cohesive answer key incorporating all corrections, matching the tone and formatting of previous lab keys (PP4, PP5, PP7, PP8), and structured for seamless export from Google Docs to PDF.

```markdown
# Practice Problem 9 Guide Questions

1. Why is the card number stored as a string rather than an integer? How does this make it easier to process individual digits when applying Luhn's algorithm?

There are two primary reasons for storing the card number as a string:
- **Integer Overflow and Leading Zeros**: A 16-digit card number far exceeds the maximum limit of a standard 32-bit `int` in C (which maxes out at 2,147,483,647, or 10 digits). Attempting to store a 16-digit number as an `int` causes integer overflow. Additionally, an integer data type automatically discards leading zeros, which would corrupt any card number beginning with '0'.
- **Direct Digit Access**: Luhn's algorithm requires processing individual digits from left to right. If the number were stored as an integer, accessing an arbitrary digit would require repeated mathematical operations (modulo `% 10` and integer division `/ 10`). Storing the card number as a string allows us to access any digit directly in constant time via array indexing (`card.number[i]`), completely bypassing arithmetic manipulations.

2. How do you access the number, month, and year members of a CreditCard variable named card?

Because `card` is a direct structure variable (not a pointer), we access its members using the **dot operator** (`.`):
```c
card.number;
card.month;
card.year;
```

The `CreditCard` structure contains three members: two scalar integers (`int month`, `int year`) and one character array (`char number[17]`). 

If `card` were instead a pointer to a structure (e.g., `CreditCard *card`), we would dereference and access its members using the **arrow operator** (`->`), such as `card->number`.

3. Each required function receives a structure by value. If a function changes card.month, does that change the original variable passed by main()? Explain.

**No**, it does not change the original variable in `main()`.

When a structure is passed by value, C makes a complete, independent copy of the entire structure and places it in the called function's stack frame. Any modifications made to `card.month` inside the function affect only this local copy. 

Because the original variable in `main()` occupies a completely separate location in memory, it remains unchanged. When the function returns, its stack frame is deallocated, discarding the local copy and any changes made to it.

4. If is_valid_number() declares its parameter as const CreditCard card in the function definition, can it assign a new value to card.month or change a character in card.number?

**No**, it can do neither.

Applying the `const` keyword to the parameter makes the entire structure instance read-only within the function. Because all members of a const-qualified structure inherit this read-only status:
- Assigning a new value to `card.month` (e.g., `card.month = 12;`) is prohibited.
- Modifying any character within `card.number` (e.g., `card.number[0] = '4';`) is also prohibited because `number` is an embedded array within the struct, making its elements `const char`.

Attempting to mutate either member will cause a compilation error.

5. Why must the expiration check consider both the month and the year? Give an example in which comparing only the month would produce an incorrect result.

An expiration date is a hierarchical two-dimensional value: the year represents the primary time interval, and the month represents the secondary sub-interval. Because the 12-month calendar cycle repeats every year, comparing only the month completely ignores the passage of years.

Using the program's reference date (**November 2026**, where `CURRENT_MONTH = 11` and `CURRENT_YEAR = 2026`):
- **False Positive Example**: Suppose a card expired in **December 2025** (`12/2025`).
  - If we compare only months, `12 >= 11` evaluates to true, incorrectly classifying the card as valid.
  - In reality, the card expired an entire year ago.
- **False Negative Example**: Suppose a card expires in **March 2027** (`03/2027`).
  - If we compare only months, `3 < 11` evaluates to false, incorrectly classifying the card as expired even though it remains valid for months to come.

Therefore, the check must evaluate the year first. The month is only compared when the card's expiration year matches `CURRENT_YEAR`.

6. Why does '7' - '0' produce the integer 7?

In C, characters are represented internally by their integer ASCII values. In the ASCII character set:
- The character `'0'` has an ASCII value of **48**.
- The character `'7'` has an ASCII value of **55**.

The C standard guarantees that the numeric characters `'0'` through `'9'` are arranged contiguously and sequentially in memory. When we subtract `'0'` from `'7'`, the compiler evaluates the difference between their underlying ASCII values:
```text
'7' - '0'  ==>  55 - 48  ==>  7
```

Because `'0'` is the baseline digit, subtracting `'0'` yields the exact zero-indexed offset of any digit character, cleanly converting the `char` digit into its corresponding `int` value.

7. When reading the struct members using fscanf(), why do the integer members require &, while the character array member does not?

The `fscanf()` function requires memory addresses as arguments so it knows where to store the data read from the input file.

- **Integer Members (`&c.month`, `&c.year`)**:
  `c.month` and `c.year` are scalar `int` variables. When accessed with the dot operator, the expression `c.month` evaluates to the integer value stored inside that variable. To give `fscanf()` the location in memory where the new value should be written, we must explicitly apply the **address-of operator** (`&`).

- **Character Array Member (`c.number`)**:
  `c.number` is an array of characters (`char number[17]`). In C, an array name used in an expression automatically **decays into a pointer to its first element** (`&c.number[0]`). Because `c.number` already evaluates to the memory address of the buffer where string characters will be placed, the address-of operator `&` is not needed.
```
