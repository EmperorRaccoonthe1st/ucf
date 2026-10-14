# Programming Assignment 2: Dice Roll Simulation — Code Review & Evaluation

**Course:** COP 3330 (Object-Oriented Programming)  
**Review Target:** `Die.java`, `Dice.java`, `DiceTester.java`  
**Reference Document:** `Programming_Assignment_2_Dice_Histogram.pdf`  

---

## 1. Executive Summary & Estimated Grade

| Evaluation Criterion | Max Points | Estimated Draft Score | Deductions / Rationale |
| :--- | :---: | :---: | :--- |
| **Proper Indentation** | 10 | 7 / 10 | Inconsistent single-line method definitions, stray blank lines, and trailing whitespaces. |
| **Header Comments, Package & Descriptive Comments** | 10 | 2 / 10 | Missing file header comments (author, course, date) across all files; minimal descriptive comments. |
| **Histogram Output (Spacing & Structure)** | 40 | 28 / 40 | Used underscores (`_`) instead of dashes (`-`); off-by-one comparison (`>` instead of `>=`); trailing whitespace on x-axis and graph rows. |
| **Encapsulation & Access Modifiers** | 10 | 10 / 10 | All instance variables are `private`, all required methods are `public`. |
| **Die Class Implementation** | 15 | 14 / 15 | Correct methods, but reinstantiates `new Random()` on every single roll (code smell / anti-pattern). |
| **Dice Class Implementation** | 15 | 15 / 15 | Correctly wraps two `Die` objects and calculates sum. |
| **Total Estimated Score** | **100** | **76 / 100** | **~24 points at risk under rubric grading.** |

*Note on Penalties:* An unused `import java.util.ArrayList;` in `DiceTester.java` risks violating the strict rule *"Do not use Java Collections or any third-party libraries"*. Submitting folders or the Gradle build structure instead of flat `.java` files incurs an automatic **-20 pt penalty**.

---

## 2. Identified Errors & Issues

### A. Critical Output & Logic Errors

1. **Histogram Divider Uses Underscores Instead of Hyphens** (`DiceTester.java`, line 48)
   - **Current code:**
     ```java
     for (int i = 0; i <= 15; i++) {
         System.out.print("__");
     }
     ```
     Prints 32 underscores: `________________________________`.
   - **Assignment specification:** The sample output explicitly specifies 32 hyphens: `--------------------------------`.
   - **Impact:** Autograders using diff comparison will flag this line as a 100% mismatch.

2. **Off-by-One Threshold Comparison in Histogram** (`DiceTester.java`, line 36)
   - **Current code:**
     ```java
     if (rolls[j] > (175 - (i * 25)))
     ```
   - **Problem:** If a sum's count lands exactly on a threshold (e.g. 25, 50, 75, 100, 125, 150), `>` will evaluate to `false` and omit the asterisk. For instance, a count of 25 would fail to show a bar at the `25|` line.
   - **Fix:** Change `>` to `>=`:
     ```java
     if (rolls[sum] >= (175 - (i * 25)))
     ```

3. **Trailing Space on X-Axis Numbers** (`DiceTester.java`, line 54)
   - **Current code:**
     ```java
     for (int i = 2; i <= 12; i++) {
         System.out.print(Integer.toString(i) + ((i > 9)? " " : "  "));
     }
     ```
   - **Problem:** At `i = 12`, this prints `"12 "` (with a trailing space). The prompt explicitly says: *"If the x axis number has 2 digits there is one space between the number and the next number."* Since there is no number after 12, the line should end immediately after `12` (length 35, matching `'    2  3  4  5  6  7  8  9 10 11 12'`).

4. **Trailing Whitespace on Histogram Rows** (`DiceTester.java`, lines 35–41)
   - **Problem:** Because every column always prints either `"*  "` or `"   "`, rows with few or no asterisks print dozens of trailing spaces:
     - Row 175 prints `"175|                                 "` (33 trailing spaces) instead of `"175|"`.
     - Row 150 prints 18 trailing spaces after the star at sum 7.
   - **Fix:** Build each line in a string/StringBuilder and call `.stripTrailing()` prior to printing, or omit trailing padding once the rightmost asterisk is passed.

---

### B. Rubric & Style Deductions

1. **Missing Header Comments & Descriptive Comments (10 pts)**
   - Neither `Die.java`, `Dice.java`, nor `DiceTester.java` contain header comments.
   - In COP 3330, each source file must start with a descriptive header block:
     ```java
     /*
      * Assignment: Programming Assignment 2 (Dice Roll Simulation)
      * Course: COP 3330
      * Author: [Your Name]
      * Description: [Class purpose]
      */
     ```
   - Methods should have brief descriptive comments explaining their function.

2. **Prohibited Java Collections Import (`DiceTester.java`, line 3)**
   - **Current code:**
     ```java
     import java.util.ArrayList;
     ```
   - **Problem:** `ArrayList` is unused, but the submission guidelines state: *"Do not use Java Collections or any third-party libraries."* Automated graders that check imports via regular expressions or AST parsing may penalize this. Delete the import.

3. **Inconsistent Indentation and Method Formatting (10 pts)**
   - In `Die.java` and `Dice.java`, getters and setters are compressed onto a single line while other methods are multi-line.
   - Extra empty lines and trailing spaces exist throughout the files.
   - Format all methods using standard Java conventions (opening brace, indented body, closing brace on a new line).

---

### C. Design & Code Quality Improvements

1. **Repeated `new Random()` Allocation in `Die.roll()`** (`Die.java`, line 19)
   - **Current code:**
     ```java
     public void roll() {
         Random r = new Random();
         setFaceValue(r.nextInt(6) + 1);
     }
     ```
   - **Problem:** When rolling 1,000 times (2,000 calls to `roll()`), allocating a new `Random` object every call creates unnecessary object churn and is considered a beginner anti-pattern.
   - **Recommendation:** Either:
     - Use standard `Math.random()`:
       ```java
       this.faceValue = (int)(Math.random() * 6) + 1;
       ```
       *(This requires no new fields or object allocations, keeping `faceValue` as the only instance variable as specified by the prompt)*.
     - Or declare a `private Random rand = new Random();` instance variable if permitted.

2. **Array Indexing Ergonomics** (`DiceTester.java`, lines 12–21)
   - Using `new int[12]` with offset `rolls[d.getFaceValue() - 1]` leaves index 0 unused and requires `rolls[i - 1]` and `rolls[j]` loops with conflicting indexing.
   - Sizing the array to 13 (`new int[13]`) allows direct natural indexing:
     ```java
     rolls[d.getFaceValue()]++;
     ```
     Sum 2 maps to `rolls[2]`, sum 12 maps to `rolls[12]`.

---

## 3. Submission Guidelines Checklist

- [x] Package declaration is `package assignment2;`.
- [x] Does not use the default package.
- [x] Only `DiceTester` has a `main` method (other classes do not).
- [ ] **WARNING — Folder Structure:** Current workspace is a Gradle project (`src/main/java/assignment2/...`). When submitting, submit **only the 3 flat `.java` files** (`Die.java`, `Dice.java`, `DiceTester.java`) with **NO folder structure and NO zip file**, or you will lose **20 points**.
- [ ] Remove `import java.util.ArrayList;`.
- [x] Does not use `printf`.
- [x] Separate files per class (no concatenated classes).
- [x] All instance variables private, all methods public.

---

## 4. Suggested Refactored Code

### `Die.java`
```java
/*
 * Programming Assignment 2: Dice Roll Simulation
 * Course: COP 3330
 * Class: Die
 * Author: [Your Name]
 * Description: Represents a single six-sided die with rolling and face value tracking.
 */
package assignment2;

public class Die {

    // Private instance variable for die face value (1 to 6)
    private int faceValue;

    // No-argument constructor initializes faceValue to 1
    public Die() {
        this.faceValue = 1;
    }

    // Sets the face value of the die
    public void setFaceValue(int val) {
        this.faceValue = val;
    }

    // Returns the current face value of the die
    public int getFaceValue() {
        return this.faceValue;
    }

    // Rolls the die to generate a random number between 1 and 6 inclusive
    public void roll() {
        this.faceValue = (int) (Math.random() * 6) + 1;
    }
}
```

### `Dice.java`
```java
/*
 * Programming Assignment 2: Dice Roll Simulation
 * Course: COP 3330
 * Class: Dice
 * Author: [Your Name]
 * Description: Represents a pair of Die objects and calculates their combined roll sum.
 */
package assignment2;

public class Dice {

    // Two private Die objects as instance variables
    private Die die1;
    private Die die2;

    // No-argument constructor initializing both dice (faceValues default to 1)
    public Dice() {
        this.die1 = new Die();
        this.die2 = new Die();
    }

    // Returns the sum of the face values of both dice
    public int getFaceValue() {
        return this.die1.getFaceValue() + this.die2.getFaceValue();
    }

    // Rolls both dice simultaneously
    public void roll() {
        this.die1.roll();
        this.die2.roll();
    }
}
```

### `DiceTester.java`
```java
/*
 * Programming Assignment 2: Dice Roll Simulation
 * Course: COP 3330
 * Class: DiceTester
 * Author: [Your Name]
 * Description: Simulates 1,000 dice rolls, counts sum occurrences, and prints a formatted histogram.
 */
package assignment2;

public class DiceTester {

    public static void main(String[] args) {
        Dice dice = new Dice();

        // Array sized to 13 so roll sum indices 2 through 12 map directly
        int[] rolls = new int[13];

        // Simulate 1,000 dice rolls
        for (int i = 0; i < 1000; i++) {
            dice.roll();
            rolls[dice.getFaceValue()]++;
        }

        // Print frequency counts for sums 2 through 12
        for (int i = 2; i <= 12; i++) {
            System.out.println("Number of " + i + "s are " + rolls[i]);
        }

        // Histogram graph header
        System.out.println();
        System.out.println("Graph");

        // Y-axis starts from 175 and decreases by 25 until 0
        for (int y = 175; y >= 0; y -= 25) {
            String yAxisLabel = String.valueOf(y);
            while (yAxisLabel.length() < 3) {
                yAxisLabel = " " + yAxisLabel;
            }

            StringBuilder row = new StringBuilder();
            row.append(yAxisLabel).append("|");

            for (int sum = 2; sum <= 12; sum++) {
                if (rolls[sum] >= y) {
                    row.append("*  ");
                } else {
                    row.append("   ");
                }
            }

            // Strip trailing padding to match assignment specification exactly
            System.out.println(row.toString().stripTrailing());
        }

        // Horizontal dashed line: 4 leading spaces followed by 32 hyphens
        System.out.print("    ");
        for (int i = 0; i < 32; i++) {
            System.out.print("-");
        }
        System.out.println();

        // X-axis numbers: 4 leading spaces, 2 spaces between 1-digit numbers, 1 space between 2-digit numbers
        System.out.print("    ");
        for (int i = 2; i <= 12; i++) {
            System.out.print(i);
            if (i < 12) {
                System.out.print(i < 9 ? "  " : " ");
            }
        }
        System.out.println();
    }
}
```
