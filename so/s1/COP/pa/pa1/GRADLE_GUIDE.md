# Gradle Guide for OOP Assignments

A practical guide to building, running, and testing Java Object-Oriented
Programming (OOP) assignments using Gradle in this directory.

---

## 1. Current Directory Inspection & Status

This directory contains a Gradle project generated via `gradle init`:

```text
pa1/
├── build.gradle.kts        # Main build script (currently empty skeleton)
├── settings.gradle.kts     # Project name and subproject configuration
├── gradle.properties       # Gradle JVM flags and caching options
├── gradlew                 # Shell script for Linux / macOS
├── gradlew.bat             # Batch script for Windows
├── gradle/
│   └── wrapper/
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties  # Pins Gradle version (9.7.1)
└── build/                  # Generated build outputs (ignored by git)
```

> **Important:**
> The existing `build.gradle.kts` was created as a "general purpose"
> build. It does not apply the Java or Application plugins yet. Until
> configured, commands such as `./gradlew build` or `./gradlew run`
> will not compile Java code or execute tests.

---

## 2. Setting Up `build.gradle.kts`

To use Java with a main class and JUnit testing, replace the content of
`build.gradle.kts` with the following configuration:

```kotlin
plugins {
    // Adds Java compilation, testing, and packaging capabilities
    java
    // Adds application execution tasks (e.g., ./gradlew run)
    application
}

repositories {
    // Source for testing and third-party libraries
    mavenCentral()
}

dependencies {
    // JUnit Jupiter for writing and running unit tests
    testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

java {
    toolchain {
        // Sets target Java language version (Java 21 LTS or 25)
        languageVersion.set(JavaLanguageVersion.of(21))
    }
}

application {
    // Specify the fully qualified name of the class containing main()
    mainClass.set("Main")
}

tasks.named<Test>("test") {
    // Enables the JUnit 5 platform runner
    useJUnitPlatform()
}

// CRITICAL FOR OOP ASSIGNMENTS USING Scanner(System.in):
// By default, Gradle runs background executions without an open stdin stream.
// This block connects terminal input so Scanner / System.in works interactively.
tasks.named<JavaExec>("run") {
    standardInput = System.`in`
}
```

> **Note:**
> If your assignment does not use a package name, keep `mainClass.set("Main")`.
> If you place code in a package (e.g., `package edu.ucf.pa1;`), set
> `mainClass.set("edu.ucf.pa1.Main")`.

---

## 3. Standard Directory Structure

Gradle follows standard Maven directory conventions for Java source code:

```text
pa1/
├── build.gradle.kts
├── settings.gradle.kts
├── gradlew
└── src/
    ├── main/
    │   └── java/
    │       └── Main.java             # Your assignment source code
    └── test/
        └── java/
            └── MainTest.java         # Your JUnit 5 unit tests
```

To create these directories in one command:

```bash
mkdir -p src/main/java src/test/java
```

---

## 4. Daily Workflow Commands

Always execute the Gradle Wrapper (`./gradlew`) rather than a system-wide
`gradle` command. The wrapper guarantees consistent behavior and eliminates
version mismatches.

| Command | Action |
| --- | --- |
| `./gradlew compileJava` | Compiles source files under `src/main/java` |
| `./gradlew build` | Compiles code, runs tests, and creates JAR |
| `./gradlew run` | Executes `mainClass` with interactive terminal input |
| `./gradlew test` | Runs all unit tests under `src/test/java` |
| `./gradlew clean` | Removes the `build/` directory |

### Passing Command-Line Arguments

If your assignment requires command-line arguments:

```bash
./gradlew run --args="input.txt output.txt"
```

### Viewing Test Results

When `./gradlew test` runs, test reports are generated as human-readable HTML:

```text
build/reports/tests/test/index.html
```

You can view the raw text summaries directly or inspect failures in the terminal.

### Continuous Development (Watch Mode)

Run tests automatically every time you save a `.java` file:

```bash
./gradlew test --continuous
```

---

## 5. Submission and Packaging

UCF OOP assignments commonly require either a standalone JAR file or a zip
containing the project source.

1. **Creating a standalone JAR:**
   ```bash
   ./gradlew jar
   ```
   The compiled JAR will be placed in `build/libs/`.

2. **Clean before zipping:**
   Always clean build caches and compiled binaries before submitting:
   ```bash
   ./gradlew clean
   ```
   Then package your project directory according to instructor guidelines.
