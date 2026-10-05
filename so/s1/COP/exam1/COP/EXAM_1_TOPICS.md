# COP 3330 - Exam 1 (Midterm) Topics & Material Index

This document provides a comprehensive breakdown of every topic covered on the first exam (**Midterm Exam**, 20% of total course grade) for **COP 3330: Object-Oriented Programming** at the University of Central Florida, along with the directory of mapped study materials located in `Exam_1_Topics/`.

---

## Exam 1 Overview

* **Exam Title:** Midterm Exam
* **Grade Weight:** 20% of final grade
* **Scope:** Lecture Slides 01 through 11, supplementary scanner buffer lessons, and the Midterm Study Guide / Hotel Room Management System problem suite.
* **Topics Covered:** Java basics, control structures, methods, strings, arrays, ArrayLists, object-oriented programming fundamentals, constructors, encapsulation, static fields/methods, and core standard library utilities (`Scanner`, `Random`, `Math`, `StringTokenizer`).

---

## Detailed Topic Breakdown

### 1. Java Program Structure & Compilation
* **Core Concepts:**
  * Java source code (`.java`) compilation into bytecode (`.class`) by the Java compiler (`javac`).
  * Execution by the Java Virtual Machine (JVM).
  * Structure of classes, class declarations, and the entry-point method:
    * `public static void main(String[] args)`
  * Package declarations and organizational namespaces.
* **Primary Material:** `01_Java_Intro_and_Program_Structure__Lecture_Slides.pdf`

### 2. Primitive Types, Variables & Operators
* **Core Concepts:**
  * Primitive data types: `byte`, `short`, `int`, `long`, `float`, `double`, `char`, `boolean`.
  * Arithmetic operators (`+`, `-`, `*`, `/`, `%`), unary operators (`++`, `--`), and compound assignment operators.
  * Integer division vs floating-point division; modulus calculations.
  * Relational operators (`==`, `!=`, `<`, `>`, `<=`, `>=`) and logical operators (`&&`, `\|\|`, `!`).
  * Explicit casting and implicit type widening.
* **Primary Material:** `02_Data_Types_Variables_and_Operators__Lecture_Slides.pdf`

### 3. Control Flow, Loops & Scanner Input
* **Core Concepts:**
  * Branching constructs: `if`, `else if`, `else`, nested conditionals, and `switch` statements.
  * Loop structures: `while`, `do-while`, and standard counter-controlled `for` loops.
  * Reading interactive console input using `java.util.Scanner`:
    * Instantiation: `Scanner scan = new Scanner(System.in);`
    * Primitive input methods: `scan.nextInt()`, `scan.nextDouble()`, `scan.nextBoolean()`, `scan.next()`.
* **Primary Material:** `03_Control_Flow_Loops_and_Scanner__Lecture_Slides.pdf`

### 4. Scanner Buffer Management
* **Core Concepts:**
  * The Java `Scanner` newline buffer pitfall: token-reading methods (`nextInt()`, `nextDouble()`, `next()`) leave trailing newline (`\n`) characters in the input buffer.
  * When `nextLine()` is called immediately following `nextInt()`, it consumes the leftover newline and returns an empty string rather than blocking for new user input.
  * Resolution strategies:
    1. Consuming the leftover newline by inserting a dummy `scan.nextLine()` right after `nextInt()`.
    2. Reading all input uniformly via `scan.nextLine()` and parsing with `Integer.parseInt(acquired)`.
* **Primary Material:** `04_Scanner_Buffer_Management__Lecture_Slides.pdf`

### 5. Methods, Parameters & Scope
* **Core Concepts:**
  * Method signatures: access specifiers, return types, method identifiers, and parameter lists.
  * Java pass-by-value semantics: arguments are passed by copying values (primitives pass copied values; object variables pass copied references).
  * Method overloading: defining multiple methods with identical names but differing parameter counts or types.
  * Variable scope: block scope, local variables, method parameters, and shadowing.
* **Primary Material:** `05_Methods_Parameters_and_Overloading__Lecture_Slides.pdf`

### 6. Strings & String Tokenization
* **Core Concepts:**
  * String immutability in Java and string pool mechanisms.
  * Equality comparison: always using `.equals()` (or `.equalsIgnoreCase()`) for content comparison rather than `==` (which compares reference memory addresses).
  * Common String operations: `.length()`, `.charAt()`, `.substring()`, `.indexOf()`, `.toLowerCase()`, `.toUpperCase()`, `.trim()`.
  * Parsing delimited text with `java.util.StringTokenizer`:
    * Instantiation: `StringTokenizer st = new StringTokenizer(sentence, ".");`
    * Traversal with `st.hasMoreTokens()` and `st.nextToken()`.
* **Primary Material:** `06_Strings_and_StringTokenizer__Lecture_Slides.pdf`

### 7. Arrays (1D & 2D Fixed Arrays)
* **Core Concepts:**
  * Fixed-size array allocation: `Room[] hotel = new Room[5];`
  * Array indexing, boundaries (`0` to `array.length - 1`), and `ArrayIndexOutOfBoundsException`.
  * Public `length` property (field, not a method: `arr.length`).
  * Iteration patterns:
    * Standard indexing loops.
    * Reverse traversal (e.g., finding the last non-null element: `for (int i = arr.length - 1; i >= 0; i--)`).
    * Enhanced for-each loops: `for (Room myRoom : arr)`.
  * Handling default values (`0`, `false`, `null`) and guarding against `NullPointerException`.
* **Primary Material:** `07_Arrays_1D_and_2D__Lecture_Slides.pdf`

### 8. ArrayList & Dynamic Collections
* **Core Concepts:**
  * Dynamic resizing vs fixed-length arrays.
  * Generics syntax: `ArrayList<Room> hotel = new ArrayList<Room>();`
  * Fundamental operations:
    * `add(element)`: appends element to the end.
    * `get(index)`: retrieves element at index.
    * `set(index, element)`: replaces element at index.
    * `size()`: returns total count of elements.
    * `remove(index)`: deletes element and shifts subsequent elements.
  * Forward and reverse iteration over dynamic lists.
  * Allowing and handling `null` references within collections.
* **Primary Material:** `08_ArrayList_and_Dynamic_Collections__Lecture_Slides.pdf`

### 9. Object-Oriented Programming & Encapsulation
* **Core Concepts:**
  * Classes as blueprints vs objects as runtime instances.
  * Information hiding and encapsulation principles.
  * Access modifiers: `private` for internal instance state; `public` for interface contracts.
  * Getter (accessor) and setter (mutator) methods.
  * Embedding validation logic inside mutators (e.g., checking room number ranges or valid room types).
* **Primary Material:** `09_OOP_Concepts_and_Encapsulation__Lecture_Slides.pdf`

### 10. Constructors, State & Object References
* **Core Concepts:**
  * Default (no-arg) and parameterized constructors.
  * Constructor chaining using `this(...)` as the first statement in a constructor.
  * The `this` self-reference keyword for resolving variable shadowing.
  * Object lifecycle, heap allocation via `new`, and reference assignment semantics.
* **Primary Material:** `10_Constructors_and_Object_References__Lecture_Slides.pdf`

### 11. Static Members, Scope & Utility Classes
* **Core Concepts:**
  * `static` class variables: shared across all instances of a class (e.g., `count` to track total objects created).
  * `static` methods: invoked via class name without instantiating an object (e.g., `Room.isValidRoomNo(num)`, `Room.getCount()`).
  * Constraints on static methods: cannot access instance variables or `this`.
  * Using standard utility classes:
    * `java.lang.Math`: `Math.random()`, `Math.sqrt()`, `Math.PI` (no imports required).
    * `java.util.Random`: instantiation, `rand.nextInt(bound)`, and pseudo-random generation.
* **Primary Material:** `11_Static_Members_and_Class_Scope__Lecture_Slides.pdf`

### 12. Midterm OOP Review & Common Traps
* **Core Concepts:**
  * Primitive types vs reference objects.
  * Object reference passing mechanics: references are passed by value; method can modify the object's fields, but cannot nullify the caller's reference.
  * Automatic `toString()` resolution: `System.out.println(myObject)` automatically invokes `myObject.toString()`.
  * Package statements and import rules:
    * `java.lang.*` is imported by default.
    * Static imports (`import static ...`) are explicitly discouraged and penalized in grading.
* **Primary Material:** `12_Midterm_OOP_Review_and_Confessions__Lecture_Slides.pdf`

### 13. Practical Problem: Hotel Room Management Suite
* **Core Concepts:**
  * The official Midterm Study Guide model implementation.
  * `Room`: class modeling room number, type (`single`, `double`, `suite`), occupancy status, and total room counter.
  * `RoomTester`: ArrayList-based driver performing batch room creation, random filtering, null checks, reverse search, and display formatting.
  * `RoomTesterArray`: Array-based driver performing identical operations using a fixed-size `Room[5]` array.
* **Primary Materials:**
  * `13_Hotel_Room_Management_Midterm__Practice_Exam.pdf`
  * `14_Room_Model_Class__Java_Source.java` / `14_Room_Model_Class__Printable_PDF.pdf`
  * `15_Room_ArrayList_Tester__Java_Source.java` / `15_Room_ArrayList_Tester__Printable_PDF.pdf`
  * `16_Room_Array_Tester__Java_Source.java` / `16_Room_Array_Tester__Printable_PDF.pdf`

---

## Index of Exam 1 Symlinks

All study materials are mapped directly in the `Exam_1_Topics/` directory:

| Symlink Name | Target Path | Material Type |
| --- | --- | --- |
| `00_Course_Grading_and_Exam_Policy__Syllabus_Slides.pdf` | `01_Syllabus/COP3330_syllabus_slides.pdf` | Syllabus Slides |
| `01_Java_Intro_and_Program_Structure__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide01_JavaIntro.pdf` | Lecture Slides |
| `02_Data_Types_Variables_and_Operators__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide02_JavaBasics.pdf` | Lecture Slides |
| `03_Control_Flow_Loops_and_Scanner__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide03_JavaBasics2.pdf` | Lecture Slides |
| `04_Scanner_Buffer_Management__Lecture_Slides.pdf` | `02_Lecture_Slides/bufferProblem.pdf` | Lecture Slides |
| `05_Methods_Parameters_and_Overloading__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide04_Methods.pdf` | Lecture Slides |
| `06_Strings_and_StringTokenizer__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide05_Strings.pdf` | Lecture Slides |
| `07_Arrays_1D_and_2D__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide06_ArraysInJava.pdf` | Lecture Slides |
| `08_ArrayList_and_Dynamic_Collections__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide07_ArrayLists.pdf` | Lecture Slides |
| `09_OOP_Concepts_and_Encapsulation__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide08_OOP.pdf` | Lecture Slides |
| `10_Constructors_and_Object_References__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide09_Objects2.pdf` | Lecture Slides |
| `11_Static_Members_and_Class_Scope__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide10_Objects3.pdf` | Lecture Slides |
| `12_Midterm_OOP_Review_and_Confessions__Lecture_Slides.pdf` | `02_Lecture_Slides/Slide11_Review_After_OOP.pdf` | Lecture Slides |
| `13_Hotel_Room_Management_Midterm__Practice_Exam.pdf` | `05_Sample_Exams/sampleMidtermExam.pdf` | Practice Exam |
| `14_Room_Model_Class__Java_Source.java` | `05_Sample_Exams/rooms/Room.java` | Java Source |
| `14_Room_Model_Class__Printable_PDF.pdf` | `05_Sample_Exams/rooms/Room.pdf` | Code PDF |
| `15_Room_ArrayList_Tester__Java_Source.java` | `05_Sample_Exams/rooms/RoomTester.java` | Java Source |
| `15_Room_ArrayList_Tester__Printable_PDF.pdf` | `05_Sample_Exams/rooms/RoomTester.pdf` | Code PDF |
| `16_Room_Array_Tester__Java_Source.java` | `05_Sample_Exams/rooms/RoomTesterArray.java` | Java Source |
| `16_Room_Array_Tester__Printable_PDF.pdf` | `05_Sample_Exams/rooms/RoomTesterArray.pdf` | Code PDF |

---

## Topics NOT on Exam 1 (Post-Midterm / Final Exam Scope)

The following advanced topics from Slides 12 through 24 and lecture notes are covered **after** Exam 1 and appear on the Final Exam:

* Inheritance (`extends`, superclass constructors, overriding methods) - Slides 12 & 13
* Interfaces (`implements`, interface contracts) - Slide 14
* Polymorphism (upcasting, dynamic method dispatch) - Slide 15
* Java File I/O (`BufferedReader`, `BufferedWriter`, `FileWriter`) - Slide 16 & `FileTester`
* JVM Memory Analysis (Stack vs Heap mechanics) - Slide 17
* Asymptotic Runtime Analysis (Big-O notation) - Slide 18
* Data Structures: Linked Lists, Stacks, and Queues - Slides 19, 20, 21 & Lecture Notes
* Exception Handling (`try-catch-finally`, custom exceptions) - Slide 22
* Java Collections Framework (`HashSet`, `HashMap`, `TreeSet`) - Slide 23
* Iterators and Enumerations - Slide 24

---

> **Note:** To inspect this study guide in the terminal, run:
> ```bash
> glow EXAM_1_TOPICS.md
> ```
