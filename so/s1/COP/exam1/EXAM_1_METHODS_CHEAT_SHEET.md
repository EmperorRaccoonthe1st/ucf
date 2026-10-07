# COP 3330 — Exam 1 (Midterm) Required Methods & Functions Cheat Sheet

This reference document compiles every standard library class, constructor, and method covered in Lectures 01–11 and the Midterm Study Guide for **COP 3330: Object-Oriented Programming** (UCF / Dr. Bacanli).

---

## Quick Navigation Index

1. [java.util.Scanner](#1-javautilscanner)
2. [java.lang.String](#2-javalangstring)
3. [java.util.ArrayList<E>](#3-javautilarrayliste)
4. [Array Operations (Fixed 1D & 2D)](#4-array-operations-fixed-1d--2d)
5. [java.util.Random](#5-javautilrandom)
6. [java.lang.Math](#6-javalangmath)
7. [java.util.StringTokenizer](#7-javautilstringtokenizer)
8. [Primitive Wrapper Classes (Parsing)](#8-primitive-wrapper-classes-parsing)
9. [Character Utility Methods](#9-javalangcharacter)
10. [System.out Printing & Formatting](#10-systemout-printing--formatting)
11. [Standard Object Overrides](#11-standard-object-overrides)
12. [Critical Exam Traps & Rules](#12-critical-exam-traps--rules)

---

## 1. `java.util.Scanner`
**Import:** `import java.util.Scanner;`  
**Instantiation:** `Scanner scan = new Scanner(System.in);`

| Method Signature | Return Type | Description | Traps & Notes |
| :--- | :--- | :--- | :--- |
| `scan.nextInt()` | `int` | Reads the next integer token. | Leaves trailing `\n` in buffer! |
| `scan.nextDouble()` | `double` | Reads the next double token. | Leaves trailing `\n` in buffer! |
| `scan.nextBoolean()` | `boolean` | Reads `"true"` or `"false"`. | Case-insensitive token match. |
| `scan.next()` | `String` | Reads the next word (delimiters = whitespace). | Stops at whitespace; leaves remainder. |
| `scan.nextLine()` | `String` | Reads everything up to the next `\n`, discards newline. | **Trap:** After `nextInt()`, consumes empty newline! |
| `scan.hasNext()` | `boolean` | Returns `true` if another token exists. | Useful in EOF / file loops. |
| `scan.hasNextInt()` | `boolean` | Checks if the next token can parse to an `int`. | Prevents `InputMismatchException`. |
| `scan.hasNextDouble()` | `boolean` | Checks if the next token can parse to a `double`. | Validation before reading. |
| `scan.hasNextLine()` | `boolean` | Checks if another line of input exists. | Standard while condition. |
| `scan.close()` | `void` | Closes the underlying stream. | Best practice at end of program. |

---

## 2. `java.lang.String`
**Import:** None (`java.lang` is imported automatically). Strings are **immutable**.

| Method Signature | Return Type | Description | Traps & Notes |
| :--- | :--- | :--- | :--- |
| `str.length()` | `int` | Number of characters in the string. | **Trap:** Requires parentheses! Array `.length` does not. |
| `str.charAt(int index)` | `char` | Character at 0-based index. | Throws `StringIndexOutOfBoundsException`. |
| `str.equals(Object other)` | `boolean` | Compares character content equality. | **Never** use `==` for String contents! |
| `str.equalsIgnoreCase(String other)` | `boolean` | Compares content ignoring case differences. | E.g., `"single".equalsIgnoreCase("Single")`. |
| `str.compareTo(String other)` | `int` | Lexicographical order (`<0`, `==0`, `>0`). | Based on ASCII/Unicode value subtraction. |
| `str.substring(int beginIndex)` | `String` | Substring from `beginIndex` to end of string. | 0-indexed inclusive. |
| `str.substring(int begin, int end)` | `String` | Substring from `begin` to `end - 1`. | Length is `end - begin`. |
| `str.indexOf(String str)` | `int` | Index of first match; `-1` if not found. | Can also take a `char`. |
| `str.indexOf(String str, int fromIndex)` | `int` | Searches for match starting at `fromIndex`. | Useful for repeated search. |
| `str.toLowerCase()` | `String` | Returns new lowercase string copy. | Original string is unchanged (immutable). |
| `str.toUpperCase()` | `String` | Returns new uppercase string copy. | Must assign result: `s = s.toUpperCase();` |
| `str.trim()` | `String` | Strips leading and trailing whitespace. | Useful for sanitizing user inputs. |
| `str.contains(CharSequence s)` | `boolean` | Returns `true` if substring exists. | Case-sensitive. |
| `str.startsWith(String prefix)` | `boolean` | Checks if string begins with prefix. | Returns boolean. |
| `str.endsWith(String suffix)` | `boolean` | Checks if string ends with suffix. | Returns boolean. |
| `str.toCharArray()` | `char[]` | Converts string into a new character array. | Allows index-based char mutation. |
| `String.valueOf(anyPrimitive)` | `String` | **Static method:** Converts primitive/object to String. | E.g., `String.valueOf(42)` -> `"42"`. |

---

## 3. `java.util.ArrayList<E>`
**Import:** `import java.util.ArrayList;`  
**Instantiation:** `ArrayList<Room> hotel = new ArrayList<Room>();` or `ArrayList<Room> hotel = new ArrayList<>();`

| Method Signature | Return Type | Description | Traps & Notes |
| :--- | :--- | :--- | :--- |
| `list.add(E element)` | `boolean` | Appends element to the end of the list. | Increases size by 1. |
| `list.add(int index, E element)` | `void` | Inserts element at `index`, shifting elements right. | Valid indices: `0` to `list.size()`. |
| `list.get(int index)` | `E` | Retrieves the element at `index`. | Throws `IndexOutOfBoundsException` if invalid. |
| `list.set(int index, E element)` | `E` | Replaces element at `index`; returns old element. | Does **not** change list size! |
| `list.remove(int index)` | `E` | Deletes element at `index`, shifts left, returns item. | Decreases size by 1. |
| `list.remove(Object o)` | `boolean` | Removes first matching object; returns `true` if found. | Relies on `.equals()`. |
| `list.size()` | `int` | Returns current element count. | **Trap:** Method call with parentheses: `.size()`! |
| `list.clear()` | `void` | Removes all elements from list. | Sets size to 0. |
| `list.isEmpty()` | `boolean` | Returns `true` if `list.size() == 0`. | Cleaner than `list.size() == 0`. |
| `list.contains(Object o)` | `boolean` | Returns `true` if element exists. | Uses `.equals()`. |

---

## 4. Array Operations (Fixed 1D & 2D)
Arrays are built into Java. No imports required.

| Expression / Operation | Type / Return | Description | Traps & Notes |
| :--- | :--- | :--- | :--- |
| `arr.length` | `int` | Length of 1D array. | **FIELD, NOT A METHOD!** No parentheses (`arr.length`). |
| `arr[i]` | Element Type | Index access / lookup (0 to `arr.length - 1`). | Throws `ArrayIndexOutOfBoundsException`. |
| `arr[i] = value;` | `void` | Element assignment. | Replaces value at index. |
| `matrix.length` | `int` | Number of rows in 2D array. | Top-level row count. |
| `matrix[r].length` | `int` | Number of columns in row `r`. | Useful for ragged or rectangular grids. |
| `for (Type item : arr)` | N/A | Enhanced for-each loop (read-only traversal). | Cannot modify array elements directly. |

---

## 5. `java.util.Random`
**Import:** `import java.util.Random;`  
**Instantiation:** `Random rand = new Random();`

| Method Signature | Return Type | Description | Range / Formula |
| :--- | :--- | :--- | :--- |
| `rand.nextInt()` | `int` | Random integer across entire range. | $-2^{31}$ to $2^{31}-1$. |
| `rand.nextInt(int bound)` | `int` | Random integer from 0 (inclusive) to bound (exclusive). | `[0, bound - 1]`. |
| `rand.nextDouble()` | `double` | Random double in `[0.0, 1.0)`. | Useful for probabilities. |
| `rand.nextBoolean()` | `boolean` | Random `true` or `false` (50/50). | Coin flip. |

### Essential Random Range Formulas:
* **Range `[0, N-1]`:** `rand.nextInt(N)`
* **Range `[min, max]` inclusive:** `rand.nextInt(max - min + 1) + min`
* **Range `[100, 1000)` (Sample Exam Room Number):** `rand.nextInt(1000 - 100) + 100` $\rightarrow$ `rand.nextInt(900) + 100`

---

## 6. `java.lang.Math`
**Import:** **DO NOT IMPORT.** (`java.lang` is auto-imported).  
**Rules:** All members are `static`. Always prefix with `Math.`. **Do NOT use `import static`!**

| Method / Constant | Return Type | Description |
| :--- | :--- | :--- |
| `Math.random()` | `double` | Returns random floating point in `[0.0, 1.0)`. |
| `Math.sqrt(double a)` | `double` | Square root of `a`. |
| `Math.pow(double a, double b)` | `double` | Computes $a^b$. |
| `Math.abs(int a)` / `Math.abs(double a)` | `int` / `double` | Absolute value of `a`. |
| `Math.max(a, b)` / `Math.min(a, b)` | Same as inputs | Returns higher / lower of two values. |
| `Math.round(double a)` | `long` | Rounds floating-point to nearest whole number. |
| `Math.floor(double a)` | `double` | Rounds down towards $-\infty$. |
| `Math.ceil(double a)` | `double` | Rounds up towards $+\infty$. |
| `Math.PI` | `double` | Constant $\pi \approx 3.141592653589793$. |
| `Math.E` | `double` | Constant $e \approx 2.718281828459045$. |

---

## 7. `java.util.StringTokenizer`
**Import:** `import java.util.StringTokenizer;`  
**Instantiation:**
* Default whitespace delimiters: `StringTokenizer st = new StringTokenizer(sentence);`
* Custom delimiter (e.g. comma): `StringTokenizer st = new StringTokenizer(sentence, ",");`

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `st.hasMoreTokens()` | `boolean` | Returns `true` if there is at least one token remaining. |
| `st.nextToken()` | `String` | Returns the next token string. |
| `st.countTokens()` | `int` | Returns count of tokens remaining to be parsed. |

### Canonical Tokenizer Loop Pattern:
```java
StringTokenizer st = new StringTokenizer(line, ",");
while (st.hasMoreTokens()) {
    String token = st.nextToken().trim();
    // process token...
}
```

---

## 8. Primitive Wrapper Classes (Parsing)
**Import:** None (`java.lang`).

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `Integer.parseInt(String s)` | `int` | Parses string to primitive `int`. Throws `NumberFormatException`. |
| `Double.parseDouble(String s)` | `double` | Parses string to primitive `double`. |
| `Boolean.parseBoolean(String s)` | `boolean` | Returns `true` if string equals `"true"` (case-insensitive). |

---

## 9. `java.lang.Character`
**Import:** None (`java.lang`). All methods are static.

| Method Signature | Return Type | Description |
| :--- | :--- | :--- |
| `Character.isDigit(char ch)` | `boolean` | Checks if `ch` is `'0'`–`'9'`. |
| `Character.isLetter(char ch)` | `boolean` | Checks if `ch` is a letter. |
| `Character.isWhitespace(char ch)` | `boolean` | Checks if `ch` is space, tab, or newline. |
| `Character.toUpperCase(char ch)` | `char` | Returns uppercase char. |
| `Character.toLowerCase(char ch)` | `char` | Returns lowercase char. |

---

## 10. `System.out` Printing & Formatting
* `System.out.print(val)`: Prints `val` without trailing newline.
* `System.out.println(val)`: Prints `val` followed by a newline. Calls `val.toString()` automatically on objects.
* `System.out.printf(String format, Object... args)`: Formatted string printing.
  * `%d` : Decimal integer
  * `%f` / `%.2f` : Floating point / rounded to 2 decimal places
  * `%s` : String
  * `%c` : Single character
  * `%b` : Boolean
  * `%n` : Platform-independent newline

---

## 11. Standard Object Overrides
Every class you write for Exam 1 inherits from `Object` and should override:

```java
@Override
public String toString() {
    return "number " + roomNumber + (isOccupied() ? " is occupied" : " is vacant");
}
```
* **Auto-call rule:** `System.out.println(myObject)` automatically resolves to `System.out.println(myObject.toString())`.

---

## 12. Critical Exam Traps & Size / Length Comparison

| Structure | How to get size/length | Example |
| :--- | :--- | :--- |
| **Array** | Public property `.length` (NO parentheses) | `hotel.length` |
| **String** | Method `.length()` (WITH parentheses) | `str.length()` |
| **ArrayList** | Method `.size()` (WITH parentheses) | `list.size()` |
| **StringTokenizer** | Method `.countTokens()` | `st.countTokens()` |

### Top 4 Dr. Bacanli Exam Traps:
1. **The Scanner Buffer Bug:**
   ```java
   int age = scan.nextInt(); // Leaves '\n' in buffer!
   scan.nextLine();          // MUST consume leftover newline!
   String name = scan.nextLine(); // Now correctly waits for user input
   ```
2. **String Equality:**
   * `str1 == str2` $\rightarrow$ Checks reference identity (memory address). **WRONG!**
   * `str1.equals(str2)` $\rightarrow$ Checks character contents. **CORRECT!**
3. **No Static Imports:**
   * NEVER write `import static java.lang.Math.*;`. Write `Math.sqrt(...)` directly.
4. **Static vs. Instance Scope:**
   * Static methods (`Room.isValidRoomNo(x)`, `Room.getCount()`) cannot access `this` or non-static fields (`roomNumber`, `occupied`).
