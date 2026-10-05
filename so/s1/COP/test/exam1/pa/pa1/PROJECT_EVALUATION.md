# Project Setup Evaluation: PA1

**Target Directory:** `/home/owen/ucf/so/s1/COP/pa/pa1`  
**Evaluation Scope:** Gradle configuration, directory structure, and runtime readiness.

---

## 1. Executive Summary

| Component | Status | Details |
| --- | --- | --- |
| Gradle Wrapper | `[PASS]` | Gradle 9.7.1 wrapper scripts and binaries present |
| Java Toolchain | `[PASS]` | Target Java 21 LTS detected and configured |
| `./gradlew compileJava` | `[PASS]` | Java compilation task completes successfully |
| `./gradlew build` | `[PASS]` | Compiles code and generates JAR artifact |
| `./gradlew run` | `[FAIL]` | Crashes with `ClassNotFoundException: Lopez_Owen` |
| Directory Structure | `[WARN]` | Package folder mismatch (`package assignment1`) |

**Direct Answer:**  
The project compiles (`./gradlew compileJava` works), but **it will NOT run** via `./gradlew run` in its current state.

---

## 2. Root Cause Analysis

### Issue A: ClassNotFoundException on `./gradlew run` `[FAIL]`

When running `./gradlew run`, the JVM throws:

```text
> Task :run FAILED
Error: Could not find or load main class Lopez_Owen
Caused by: java.lang.ClassNotFoundException: Lopez_Owen
```

* In `build.gradle.kts`, the main class is configured as:
  ```kotlin
  application {
      mainClass = "Lopez_Owen"
  }
  ```
* However, inside `src/main/java/Lopez_Owen.java`, line 8 defines:
  ```java
  package assignment1;
  ```
* Because of `package assignment1;`, the compiled class's fully qualified runtime name is `assignment1.Lopez_Owen`, not `Lopez_Owen`. Gradle cannot find a class named `Lopez_Owen` at the root classpath.

---

### Issue B: Directory Structure vs Package Declaration `[WARN]`

In standard Java and Gradle conventions, the filesystem folder path must mirror the package statement:

```text
Current (Non-standard):
src/main/java/
└── Lopez_Owen.java               (declares 'package assignment1;')

Standard Convention:
src/main/java/
└── assignment1/
    └── Lopez_Owen.java           (declares 'package assignment1;')
```

While `javac` tolerates compiling the file from the root, it places the `.class` file in `build/classes/java/main/assignment1/`. Build tools, IDEs, and autograders expect the source folder to match the package name.

---

## 3. Recommended Fixes

Depending on your course / assignment instructions, select one of the two approaches below:

### Option 1: The assignment requires `package assignment1;`

1. Move the source file into the package directory:
   ```bash
   mkdir -p src/main/java/assignment1
   mv src/main/java/Lopez_Owen.java src/main/java/assignment1/
   ```
2. Update `build.gradle.kts` to specify the fully qualified class name:
   ```kotlin
   application {
       mainClass = "assignment1.Lopez_Owen"
   }
   ```

### Option 2: The assignment requires default (unnamed) package

> **Note:** Many university autograders require students to omit the `package` line so grading scripts can run classes directly.

1. Keep `Lopez_Owen.java` directly in `src/main/java/`.
2. Remove `package assignment1;` from `Lopez_Owen.java`.
3. Keep `mainClass = "Lopez_Owen"` in `build.gradle.kts`.

---

## 4. Configuration Review Checklist

* **`settings.gradle.kts`**: `[PASS]`  
  Correctly configures `foojay-resolver-convention` and sets `rootProject.name = "Lopez_Owen"`.
* **`gradle.properties`**: `[PASS]`  
  Configuration caching is enabled.
* **`gradle/libs.versions.toml`**: `[PASS]`  
  Declares dependencies for Guava and JUnit 4.
* **Console Input (`standardInput = System.`in`)**: `[PASS]`  
  Line 38-40 in `build.gradle.kts` properly attaches `System.in` to the `:run` task.
