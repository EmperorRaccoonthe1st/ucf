# COP 3330 Course Materials

This directory contains the unzipped, converted, and organized materials for **COP 3330: Object-Oriented Programming** (University of Central Florida).

---

## Directory Overview

```text
COP/
|-- 01_Syllabus/
|   `-- COP3330_syllabus_slides.pdf
|-- 02_Lecture_Slides/
|   |-- Slide01_JavaIntro.pdf
|   |-- Slide02_JavaBasics.pdf
|   |-- Slide03_JavaBasics2.pdf
|   |-- Slide03_Supplement_bufferProblem.pdf -> bufferProblem.pdf
|   |-- bufferProblem.pdf
|   |-- Slide04_Methods.pdf
|   |-- Slide05_Strings.pdf
|   |-- Slide06_ArraysInJava.pdf
|   |-- Slide07_ArrayLists.pdf
|   |-- Slide08_OOP.pdf
|   |-- Slide09_Objects2.pdf
|   |-- Slide10_Objects3.pdf
|   |-- Slide11_Review_After_OOP.pdf
|   |-- Slide12_InheritancePart1.pdf
|   |-- Slide13_InheritancePart2.pdf
|   |-- Slide14_Interfaces.pdf
|   |-- Slide15_Polymorphism.pdf
|   |-- Slide16_Java_File_Operations.pdf
|   |-- Slide17_Memory.pdf
|   |-- Slide18_RunTimeAnalysis.pdf
|   |-- Slide19_Linked_Lists.pdf
|   |-- Slide20_Stacks.pdf
|   |-- Slide21_Queues.pdf
|   |-- Slide22_Exceptions.pdf
|   |-- Slide23_Collections.pdf
|   `-- Slide24_Iterator_Enum.pdf
|-- 03_Lecture_Notes/
|   |-- COP3330_linked_list_notes.pdf
|   |-- COP3330_Queue_Notes.pdf
|   `-- COP3330_Stack_Notes.pdf
|-- 04_Code_Examples/
|   `-- FileTester/
|       |-- FileTester.pdf
|       |-- example.txt
|       `-- src/FileTester/FileTester.java
|-- 05_Sample_Exams/
|   |-- sampleMidtermExam.pdf
|   `-- rooms/
|       |-- Room.java / Room.pdf
|       |-- RoomTester.java / RoomTester.pdf
|       `-- RoomTesterArray.java / RoomTesterArray.pdf
|-- Exam_1_Topics/
|   `-- (Symlinks to all Midterm slides, guides, & code)
`-- _Archive_Original_Sources/
    |-- pptx/
    `-- zips/
```

---

## Actions Performed

1. **Archive Extraction**:
   * Extracted root archive `course_files_export.zip`.
   * Extracted nested archives `FileTesterCodeExample.zip` and `rooms.zip`.

2. **PDF Conversion**:
   * Converted PowerPoint presentations to PDF:
     * `syllabus/COP3330_syllabus_slides.pptx` -> `01_Syllabus/COP3330_syllabus_slides.pdf`
     * `pdfSlides/bufferProblem.pptx` -> `02_Lecture_Slides/bufferProblem.pdf`
     * Verified existing PDF versions for `Slide20_Stacks` and `Slide21_Queues`.
   * Generated printable PDF versions of standalone Java source files (`FileTester.java`, `Room.java`, `RoomTester.java`, `RoomTesterArray.java`).

3. **Reorganization**:
   * Grouped materials into five numbered categories (`01_Syllabus` through `05_Sample_Exams`).
   * Created symbolic link `Slide03_Supplement_bufferProblem.pdf` pointing to `bufferProblem.pdf` so the scanner buffer lesson naturally follows Java Basics 2 in alphabetical listings.
   * Preserved all original `.zip` and `.pptx` source files in `_Archive_Original_Sources/`.

---

## Content Inventory

### 01. Syllabus

* `COP3330_syllabus_slides.pdf`: Course policies, grading distribution, office hours, and expectations.

### 02. Lecture Slides

| File Name | Topic | Pages |
| --- | --- | --- |
| `Slide01_JavaIntro.pdf` | Introduction to Java | 16 |
| `Slide02_JavaBasics.pdf` | Basic Syntax & Types | 23 |
| `Slide03_JavaBasics2.pdf` | Input & Conditionals | 22 |
| `bufferProblem.pdf` | Scanner Buffer Handling | 10 |
| `Slide04_Methods.pdf` | Methods & Parameter Passing | 21 |
| `Slide05_Strings.pdf` | String Class & Methods | 24 |
| `Slide06_ArraysInJava.pdf` | 1D & 2D Arrays | 27 |
| `Slide07_ArrayLists.pdf` | Dynamic Lists | 21 |
| `Slide08_OOP.pdf` | OOP Concepts | 17 |
| `Slide09_Objects2.pdf` | Object References & Methods | 29 |
| `Slide10_Objects3.pdf` | Object Construction & State | 18 |
| `Slide11_Review_After_OOP.pdf` | Mid-Course OOP Review | 12 |
| `Slide12_InheritancePart1.pdf` | Inheritance Basics | 20 |
| `Slide13_InheritancePart2.pdf` | Superclasses & Overriding | 12 |
| `Slide14_Interfaces.pdf` | Interface Implementation | 15 |
| `Slide15_Polymorphism.pdf` | Polymorphic Behavior | 26 |
| `Slide16_Java_File_Operations.pdf` | File I/O (`BufferedReader`/`Writer`) | 21 |
| `Slide17_Memory.pdf` | JVM Heap & Stack Memory | 28 |
| `Slide18_RunTimeAnalysis.pdf` | Asymptotic Analysis (Big-O) | 21 |
| `Slide19_Linked_Lists.pdf` | Singly Linked Lists | 16 |
| `Slide20_Stacks.pdf` | Stack ADT & Operations | 8 |
| `Slide21_Queues.pdf` | Queue ADT & Operations | 8 |
| `Slide22_Exceptions.pdf` | Exception Handling & Try-Catch | 20 |
| `Slide23_Collections.pdf` | Java Collections Framework | 19 |
| `Slide24_Iterator_Enum.pdf` | Iterators & Enumerations | 22 |

### 03. Lecture Notes

* `COP3330_linked_list_notes.pdf`: In-depth walkthrough on linked list operations (12 pages).
* `COP3330_Queue_Notes.pdf`: Queue structures, FIFO mechanisms, and code implementations (6 pages).
* `COP3330_Stack_Notes.pdf`: Stack operations (push, pop, peek) and call-stack concepts (5 pages).

### 04. Code Examples

* `FileTester/`:
  * `FileTester.java`: Demonstration of `BufferedReader`, `BufferedWriter`, and `StringTokenizer`.
  * `FileTester.pdf`: Formatted printable PDF of the source code.
  * `example.txt`: Sample text file used for file operations demo.
  * Eclipse project configuration files (`.project`, `.classpath`, `.settings`).

### 05. Sample Exams

* `sampleMidtermExam.pdf`: Midterm Exam Study Guide covering Hotel Room Management System problem (12 pages).
* `rooms/`:
  * `Room.java` / `Room.pdf`: Hotel room model class.
  * `RoomTester.java` / `RoomTester.pdf`: ArrayList-based driver and verification test.
  * `RoomTesterArray.java` / `RoomTesterArray.pdf`: Array-based driver and verification test.

---

> **Note:** Original archives (`course_files_export.zip`, `FileTesterCodeExample.zip`, `rooms.zip`) and PowerPoint sources (`.pptx`) are preserved in `_Archive_Original_Sources/` for future reference.
