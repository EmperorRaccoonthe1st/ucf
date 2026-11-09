# COP 3330: Object-Oriented Programming - Course Compendium & Reference Guide

**Deliverable File:** [COP3330_OOP_Complete_Course_Reference.pdf](file:///home/owen/ucf/so/s1/COP/slides/COP3330_OOP_Complete_Course_Reference.pdf)  
**Compiler Script:** [build_oop_course_pdf.py](file:///home/owen/ucf/so/s1/COP/slides/build_oop_course_pdf.py)  
**Scope:** Complete University of Central Florida COP 3330 Curriculum (All 5 Pillars)  
**Total Pages:** 775 Pages (Normalized 16:9 Widescreen Landscape, 1600 x 900 pt)  
**Layout Architecture:** Side-by-Side Widescreen (Vector Slide Left + Dark Mode Code / Concepts Right)  

---

## Executive Summary

The entire university course archive for **COP 3330: Object-Oriented Programming** has been normalized and combined into a single unified master reference document: `COP3330_OOP_Complete_Course_Reference.pdf`.

This document synthesizes:
1. All 25 core lecture slide decks and supplementary modules (478 slides).
2. All runnable lecture code implementations (`Node.java`, `LinkedList.java`, `Stack.java`, `Queuex.java`, `FileTester.java`).
3. Complete midterm exam specifications, study guides, and the Hotel Room verified solution suite.
4. All 12 Undergraduate Learning Assistant (ULA) review dossiers and practice problem sets.

Every slide page has been normalized into a consistent 16:9 widescreen landscape layout with side-by-side positioning:
* **Left Pane**: The original lecture slide or structural document embedded with 100% vector fidelity via affine transformations, ensuring crisp vector lines, searchable text, and diagram readability.
* **Right Pane**: A dedicated dark-mode IDE editor card (macOS traffic-light window controls, filename tabs, language badges) featuring syntax-highlighted Java code using the Dracula theme, line number gutters, and structured concept notes or technical reference cards.

---

## Document Layout Architecture

The diagram below illustrates the normalized 16:9 side-by-side presentation implemented across all 775 pages:

```text
+--------------------------------------------------------------------------------------------------+
|  COP 3330: OBJECT-ORIENTED PROGRAMMING    |    Module 02: Java Basics I    Slide 4/23 | Page 20  |
+--------------------------------------------------------------------------------------------------+
|                                                   |                                              |
|  +---------------------------------------------+  |  +----------------------------------------+  |
|  | [LECTURE SLIDE]                             |  |  | (o)(o)(o) FirstJavaProgram.java   Java |  |
|  |                                             |  |  +----------------------------------------+  |
|  |                                             |  |  |  1 | package assignment0;              |  |
|  |         Original Vector Slide Content       |  |  |  2 |                                   |  |
|  |        (100% Crisp Vector Preservation,     |  |  |  3 | public class FirstJavaProgram {   |  |
|  |           Searchable & Copyable Text,       |  |  |  4 |   public static void main(...) {  |  |
|  |         High-Resolution Diagram Fidelity)   |  |  |  5 |     System.out.println("Hi!");    |  |
|  |                                             |  |  |  6 |   }                               |  |
|  |                                             |  |  |  7 | }                                 |  |
|  |                                             |  |  +----------------------------------------+  |
|  |                                             |  |  | [Key Invariants & Concept Notes]       |  |
|  |                                             |  |  | * Class name matches filename.         |  |
|  |                                             |  |  | * Main method required for execution.  |  |
|  +---------------------------------------------+  |  +----------------------------------------+  |
|                                                   |                                              |
+--------------------------------------------------------------------------------------------------+
|  University of Central Florida  *  Department of Computer Science  *  Normalized Master Reference |
+--------------------------------------------------------------------------------------------------+
```

---

## Complete Curriculum Structure

The compendium is organized into five numbered parts with interactive PDF bookmark outlines:

### Part I: Course Administration & Syllabus (Pages 1 to 10)
* **Cover Page (Page 1):** Master title spread and curriculum roadmap.
* **Module 00: Syllabus & Course Administration (Pages 2 to 10):**
  * Grading criteria, exam weighting, and academic policies.
  * Office hours, prerequisite requirements, and course communication standards.

### Part II: Core Lecture Slides (Pages 11 to 498)
* **Module 01: Introduction to Java (Pages 11 to 26):**
  * History of Java, "write once, run everywhere" (WORA).
  * JVM vs JRE vs JDK architecture; compilation to bytecode (`javac` -> `.class`).
* **Module 02: Java Basics I - Syntax & Data Types (Pages 27 to 49):**
  * Primitive types (`byte`, `short`, `int`, `long`, `float`, `double`, `boolean`, `char`).
  * Console I/O (`System.out.print`, `println`, `printf`), variable scopes, and `Scanner` basics.
* **Module 03: Java Basics II - Control Flow & Loops (Pages 50 to 71):**
  * Conditionals (`if`, `else if`, `else`), `switch` branching, fall-through rules.
  * Loops (`while`, `do-while`, standard `for`), loop variables, `break` and `continue`.
  * Typecasting, widening conversions, narrowing conversions, and precision loss.
* **Module 03 Supplement: Scanner Buffer Architecture (Pages 72 to 81):**
  * Scanner newline pitfall (`nextInt()` leaving trailing `\n` in buffer).
  * Buffer flushing mechanisms and `nextLine()` sanitization patterns.
* **Module 04: Methods & Parameter Passing (Pages 82 to 102):**
  * Method signatures, return types, pass-by-value semantics for primitives and references.
  * Method overloading, static global variables, and `final` modifier invariants.
* **Module 05: Strings & StringTokenizer (Pages 103 to 126):**
  * String immutability, string pool optimization, `equals()` vs `==`.
  * `compareTo()`, `substring()`, `split()`, `StringBuilder` mutation, and `StringTokenizer`.
* **Module 06: Arrays - 1D & 2D Arrays in Java (Pages 127 to 153):**
  * 1D array declaration, memory instantiation, default zero-initialization, array traversal.
  * Enhanced `for-each` loop, multidimensional arrays, ragged arrays, and `Arrays.copyOf()`.
* **Module 07: ArrayLists & Dynamic Collections (Pages 154 to 174):**
  * Generics syntax (`ArrayList<T>`), wrapper classes (`Integer`, `Double`), autoboxing.
  * Core list operations: `add()`, `get()`, `set()`, `remove()`, `contains()`, `indexOf()`, `clear()`.
* **Module 08: OOP Fundamentals & Encapsulation (Pages 175 to 191):**
  * Class definitions, state (attributes) and behavior (methods).
  * Object instantiation (`new`), memory references, and procedural vs OOP paradigms.
* **Module 09: Objects II - References & Aliasing (Pages 192 to 220):**
  * Reference variables, stack vs heap allocation, reference aliasing side-effects.
  * `null` references, `NullPointerException` avoidance, and explicit `this` keyword scoping.
* **Module 10: Objects III - Constructors & Static Scope (Pages 221 to 238):**
  * Default constructors, parameterized constructors, constructor overloading.
  * Information hiding, `private` access, getter/setter contracts.
  * `static` class variables, `static` utility methods, and class vs instance scope.
* **Module 11: Mid-Course OOP Review & Tracing (Pages 239 to 250):**
  * Comprehensive midterm review, code execution tracing, and memory state diagrams.
* **Module 12: Inheritance Part I - Superclasses & Hierarchy (Pages 251 to 270):**
  * Code reuse via `extends`, `is-a` relationships, superclass vs subclass architecture.
  * Constructor chaining via `super()`, `protected` access modifier rules.
* **Module 13: Inheritance Part II - Method Overriding & Object (Pages 271 to 282):**
  * Method overriding rules, `@Override` annotation, dynamic method dispatch.
  * Root `java.lang.Object` class, overriding `toString()` and `equals()`.
* **Module 14: Interfaces & Multiple Implementation (Pages 283 to 299):**
  * Interface contracts, `implements` keyword, default methods, constants.
  * Multiple interface implementation, decoupling, and the `Comparable<T>` interface.
* **Module 15: Polymorphism & Dynamic Method Binding (Pages 300 to 325):**
  * Polymorphic reference variables, subtype polymorphism.
  * Dynamic (late) method binding at runtime vs compile-time static type checking.
  * Upcasting, downcasting, `ClassCastException`, and `instanceof` guard checks.
* **Module 16: Java File Operations & I/O Streams (Pages 326 to 346):**
  * File streams: `FileReader`, `FileWriter`, `BufferedReader`, `BufferedWriter`.
  * Stream flushing, explicit stream closure, and append mode flags.
* **Module 17: JVM Memory Architecture - Stack & Heap (Pages 347 to 374):**
  * JVM memory segments: Method Area, Call Stack (stack frames, local primitives, references).
  * Garbage Collection (GC), object reachability, mark-and-sweep, memory leaks.
* **Module 18: Asymptotic Runtime & Space Analysis (Big-O) (Pages 375 to 395):**
  * Algorithm analysis, growth functions, worst-case Big-O complexity.
  * Common complexities: `O(1)`, `O(log n)`, `O(n)`, `O(n log n)`, `O(n^2)`.
* **Module 19: Linked Lists Data Structure (Pages 396 to 411):**
  * Singly linked list architecture: `Node` class (payload + reference to next).
  * Traversal, head insertion (`O(1)`), tail insertion, deletion, and boundary conditions.
* **Module 20: Stacks Abstract Data Type (Pages 412 to 419):**
  * LIFO (Last-In, First-Out) protocol: `push()`, `pop()`, `peek()`, `isEmpty()`.
  * Array-based stack vs Linked-list-based stack; call-stack mechanics.
* **Module 21: Queues Abstract Data Type (Pages 420 to 427):**
  * FIFO (First-In, First-Out) protocol: `enqueue()`, `dequeue()`, `peek()`, `isEmpty()`.
  * Circular array queue indexing (`(tail + 1) % capacity`) vs Linked-list queue.
* **Module 22: Exception Handling Architecture (Pages 428 to 447):**
  * Exception hierarchy: `Throwable`, `Error`, `Exception`, `RuntimeException`.
  * Checked exceptions vs Unchecked exceptions; `try`, `catch`, `finally`, `throw`, `throws`.
* **Module 23: Java Collections Framework (Pages 448 to 466):**
  * Collections hierarchy: `Collection<E>`, `List<E>`, `Set<E>`, `Map<K, V>`.
  * Implementations: `ArrayList`, `LinkedList`, `HashSet`, `TreeSet`, `HashMap`, `TreeMap`.
* **Module 24: Iterators & Enumerations (Pages 467 to 488):**
  * `Iterator<E>` interface (`hasNext()`, `next()`, `remove()`).
  * Enhanced `for-each` loop under the hood, type-safe `enum` declarations.

---

### Part III: Lecture Code Implementations & Notes (Pages 489 to 512)
* **Code Suite 01: Singly Linked Lists Implementation (Pages 489 to 500):**
  * Full Java implementation: `Node.java` and `LinkedList.java` (12 pages).
  * Deep copy constructor, head/tail insertion, deletion by value, and traversal.
* **Code Suite 02: Stack Structures & Array/List Variants (Pages 501 to 505):**
  * Full Java implementation: `Node.java`, `Stack.java`, `ArrayStack.java`, `ListStack.java`.
* **Code Suite 03: Queue Structures & FIFO Variants (Pages 506 to 511):**
  * Full Java implementation: `Node.java`, `Queuex.java`, `ArrayQueue.java`, `ListQueue.java`.
* **Code Suite 04: File I/O & Stream Handling Demo (Page 512):**
  * Complete source code for `FileTester.java`: `BufferedReader`, `BufferedWriter`, `StringTokenizer`.

---

### Part IV: Midterm Exam Practice & Hotel Room Solution Suite (Pages 513 to 527)
* **Midterm Exam Practice Guide (Pages 513 to 524):**
  * Complete 12-page study guide and problem prompt for Hotel Room Management System.
* **Room Model Class (`Room.java`) (Page 525):**
  * Encapsulated room model with private fields, dual constructors, and custom `toString()`.
* **Room ArrayList Tester Driver (`RoomTester.java`) (Page 526):**
  * Dynamic list driver testing room allocation, search, and dynamic guest check-out.
* **Room Array Tester Driver (`RoomTesterArray.java`) (Page 527):**
  * Fixed array driver testing array boundary checks, occupancy counts, and traversals.

---

### Part V: ULA Comprehensive Review Guides (Pages 528 to 775)
* **ULA Module 01: Intro to Java & Syntax (Pages 528 to 554)**
* **ULA Module 02: Strings in Java (Pages 555 to 570)**
* **ULA Module 03: Arrays & ArrayLists in Java (Pages 571 to 593)**
* **ULA Module 04: Intro to Objects & References (Pages 594 to 641)**
* **ULA Module 05: The Four Pillars of OOP (Pages 642 to 664)**
* **ULA Module 06: Inheritance & Interfaces (Pages 665 to 688)**
* **ULA Module 07: File I/O & Exception Handling (Pages 689 to 708)**
* **ULA Module 08: Runtime and Space Analysis (Pages 709 to 724)**
* **ULA Module 09: Linked Lists In-Depth (Pages 725 to 747)**
* **ULA Module 10: Stacks & Queues Implementations (Pages 748 to 768)**
* **ULA Module 11: Practice Exam Questions (Pages 769 to 770)**
* **ULA Module 12: Sample Object Assignment (Pages 771 to 775)**

---

## Verification & Forensic Audit

```text
================================================================================
COP 3330 COMPENDIUM VERIFICATION DOSSIER
================================================================================
[PASS] Deliverable Path:     COP3330_OOP_Complete_Course_Reference.pdf
[PASS] Total Page Count:     775 Pages
[PASS] Output Dimensions:    1600 pt x 900 pt (Standard 16:9 Landscape)
[PASS] Aspect Ratio:         1.7778 (True Widescreen)
[PASS] Left Pane Geometry:   740 pt x 795 pt (Vector Slide Framing)
[PASS] Right Pane Geometry:  755 pt x 795 pt (Dark Mode Code / Concept IDE)
[PASS] Syntax Lexer:         Pygments JavaLexer with Dracula Theme Palette
[PASS] Text Fidelity:        100% Vector preserved; searchable and copyable
[PASS] Outline Tree:         Hierarchical PDF bookmarks across all 5 Parts
[PASS] Build Time:           76.86 seconds
================================================================================
```

> **Note:** To browse the document with native PDF bookmarks in your default viewer, run:
> ```bash
> xdg-open COP3330_OOP_Complete_Course_Reference.pdf
> ```
