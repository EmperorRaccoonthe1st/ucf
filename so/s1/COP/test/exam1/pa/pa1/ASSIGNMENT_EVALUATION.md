# Programming Assignment 1 Evaluation Report

**Document Evaluated:** `Programming_Assignment_1_Receipt_Generator.pdf`  
**Source Code Evaluated:** `src/main/java/assignment1/Lopez_Owen.java`  
**Current Evaluation Status:** **100 / 100 pts** `[PASS]`

---

## 1. Updated Rubric Scorecard

| Rubric Item | Score | Status |
| --- | --- | --- |
| Package Name (`assignment1`) | 10 / 10 | `[PASS]` |
| Receipt Number Generation | 10 / 10 | `[PASS]` |
| Date Generation Function | 10 / 10 | `[PASS]` |
| Code Quality & Comments | 10 / 10 | `[PASS]` |
| Test Case 1 (Empty / DONE) | 20 / 20 | `[PASS]` |
| Test Case 2 (Taxed Item) | 20 / 20 | `[PASS]` |
| Test Case 3 (Multiple & Exempt) | 20 / 20 | `[PASS]` |
| **Total Score** | **100 / 100** | **`[PASS]` Ready for Submission** |

---

## 2. Verification of Applied Corrections

### 1. Item Name Capitalization (`[PASS]`)
* **Change Applied:**
  ```java
  System.out.print(" " + s.substring(0, 1).toUpperCase() + s.substring(1) + " ");
  ```
* **Test Verification:**
  * Input `food` -> prints `Food`
  * Input `shoe` -> prints `Shoe`
  * Input `T-shirt` -> prints `T-shirt`
  * Matches Test Case 3 expected output.

### 2. Store Header Asterisk Count (`[PASS]`)
* **Change Applied:** Updated right side of line 2 to 15 asterisks:
  ```java
  ****** S store ***************
  ```
* **Test Verification:**
  * Left: `******` (6 asterisks)
  * Middle: ` S store ` (9 characters with spaces)
  * Right: `***************` (15 asterisks)
  * Total width: exactly 30 characters, aligning with line 1 and line 3.

### 3. Blank Line Elimination (`[PASS]`)
* **Change Applied:** Converted multi-line text blocks from `println` to `print`:
  ```java
  System.out.print("""
  ******************************
  ****** S store ***************
  ******************************
  """);
  ```
* **Test Verification:** Receipt number appears immediately below the top asterisks with no extraneous blank line; footer asterisks appear directly below the total line.

### 4. Header Comment Compliance (`[PASS]`)
* **Change Applied:** Explicitly added `Assignment 1` to the file header block.
* **Content:** Name, PID, NID, course, year, assignment identifier, and functional summary are all present.

---

## 3. Submission Readiness Checklist

* `[PASS]` Exactly one `.java` source file (`Lopez_Owen.java`).
* `[PASS]` Package declaration is `package assignment1;`.
* `[PASS]` No Java Collections framework imports (`ArrayList`, `HashMap`, etc.).
* `[PASS]` No third-party libraries.
* `[PASS]` Compiles cleanly with `./gradlew compileJava`.
