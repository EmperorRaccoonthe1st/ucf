# Unit Testing Guide for Java and Gradle

A comprehensive guide on unit testing concepts, Java ecosystem options, and
practical test authoring for this project.

---

## 1. Unit Testing: Core Concepts

### Origin
* **Early History:** Formal program verification and subroutine isolation date
  back to the 1950s and 1960s with modular programming.
* **Modern Inception:** In 1989, Kent Beck created **SUnit** for Smalltalk.
* **The xUnit Boom:** In 1997, Kent Beck and Erich Gamma ported SUnit to Java
  on a flight from Zurich to Atlanta, creating **JUnit**. JUnit became the
  foundational archetype for the "xUnit" family across every major programming
  language (NUnit, PyTest, CppUnit, etc.) and served as the cornerstone of
  Extreme Programming (XP) and Test-Driven Development (TDD).

### Philosophy
* **Isolation (The Unit):** A "unit" is the smallest testable piece of code in
  an application (typically a single method or class). Unit testing isolates
  that unit from external dependencies (user prompts, network sockets, databases,
  filesystems) to verify internal logic alone.
* **Fast Feedback:** Unit tests execute in milliseconds. Developers can run
  hundreds of tests on every save without waiting on slow I/O or manual UI input.
* **Executable Specification:** Tests serve as living documentation. Reading a
  test suite demonstrates exactly what inputs a method accepts, what outputs
  it produces, and what exceptions it throws.
* **Fearless Refactoring:** An existing test suite forms a safety harness. You
  can optimize, rename, or restructure internal algorithms knowing any breakage
  will be immediately caught.
* **The FIRST Principles:**
  * **Fast:** Executes in milliseconds.
  * **Independent:** No test depends on the execution or outcome of another.
  * **Repeatable:** Produces identical results in any environment.
  * **Self-Validating:** Binary pass/fail outcome without manual inspection.
  * **Timely:** Written alongside or immediately preceding production code.

### Major Use Cases
* **Algorithmic Logic:** Validating math formulas, pricing calculations, date
  formatting, and state transitions.
* **Edge and Boundary Cases:** Testing zero values, negative numbers, empty
  strings, leap days, and boundary numbers (`Integer.MAX_VALUE`).
* **Error Handling:** Verifying that methods throw correct exceptions
  (`IllegalArgumentException`, `NullPointerException`) on invalid arguments.
* **Regression Prevention:** Locking in bug fixes with a test case so bugs never
  reoccur unnoticed.

### Inherent Downsides
* **Maintenance Cost:** Test code is code. When specifications change, test suites
  must be updated.
* **False Sense of Security:** A suite of passing unit tests does not prove the
  entire system functions. Components can behave perfectly in isolation yet fail
  when wired together (which is why integration and end-to-end tests exist).
* **Brittleness:** Tests that inspect private implementation details rather than
  public observable behavior break during harmless internal refactors.
* **Mocking Overhead:** Replacing complex dependencies (databases, web APIs)
  with mock objects can introduce boilerplate and disconnect tests from reality.

### Common Frameworks Across Languages

| Language | Primary Testing Frameworks |
| --- | --- |
| Java | JUnit 5 (Jupiter), TestNG, Spock |
| Python | pytest, unittest |
| C / C++ | GoogleTest (gtest), Catch2 |
| C# / .NET | xUnit.net, NUnit |
| JavaScript / TS | Jest, Vitest, Mocha |
| Rust / Go | Built-in test harnesses (`cargo test`, `go test`) |

---

## 2. Java and Gradle Specific Unit Testing

### Framework Options in Java

1. **JUnit 4 (`junit:junit:4.13.2`):**
   * *Status:* Legacy / Maintenance mode.
   * *Characteristics:* Relies on older Java 5 annotations (`@Test`, `@Before`,
     `@After`). Lacks modularity and requires cumbersome custom runners (`@RunWith`)
     for parameterized testing.
   * *Presence:* Currently declared in your `gradle/libs.versions.toml`.

2. **JUnit 5 (JUnit Jupiter):**
   * *Status:* Modern industry standard.
   * *Characteristics:* Redesigned from the ground up for modern Java (Java 8+).
     Divided into three distinct subsystems:
     * `JUnit Platform`: Low-level engine interface that Gradle interacts with.
     * `JUnit Jupiter`: The modern API (`@Test`, `@BeforeEach`, `@Nested`,
       `@ParameterizedTest`, `assertAll`, `assertThrows`).
     * `JUnit Vintage`: Backward compatibility engine allowing JUnit 3/4 tests
       to run on the new platform.
   * *Presence:* Supported natively in Gradle via `useJUnitPlatform()`.

3. **TestNG:**
   * *Status:* Active alternative.
   * *Characteristics:* Originally built to offer advanced features JUnit 4 lacked
     (flexible test grouping, parallel execution, native XML suite definitions).
     Rarely needed for modern assignments since JUnit 5 adopted most of its strengths.

4. **Spock:**
   * *Status:* Popular in Groovy/enterprise environments.
   * *Characteristics:* Highly expressive BDD-style (Given-When-Then) syntax.
     Requires adding the Groovy plugin and runtime to your Gradle build.

### Evaluation and Recommendation

**Selected Framework: JUnit 5 (JUnit Jupiter)**

**Rationale:**
* **Native Gradle Support:** Gradle 9.x integrates directly with the JUnit Platform.
* **Modern Assertions:** Clean exception testing via `assertThrows()` and grouped
  assertions via `assertAll()`.
* **Standard Academic & Industry Choice:** UCF COP 3330 and standard Java toolchains
  use JUnit 5 conventions.

---

## 3. Project Configuration for JUnit 5

### Step 1: Update `build.gradle.kts`

Ensure [`build.gradle.kts`](file:///home/owen/ucf/so/s1/COP/pa/pa1/build.gradle.kts)
configures the test task and imports JUnit Jupiter:

```kotlin
dependencies {
    // JUnit 5 Jupiter API and Engine
    testImplementation("org.junit.jupiter:junit-jupiter:5.11.4")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")

    // Guava (if used by your application)
    implementation(libs.guava)
}

tasks.named<Test>("test") {
    // Instruct Gradle to use the JUnit Platform runner
    useJUnitPlatform()
}
```

---

## 4. Writing Tests for This Assignment

### Directory Structure

Gradle expects tests to mirror the package structure of production code under
`src/test/java/`:

```text
pa1/
└── src/
    ├── main/
    │   └── java/
    │       └── assignment1/
    │           └── Lopez_Owen.java
    └── test/
        └── java/
            └── assignment1/
                └── Lopez_OwenTest.java
```

Create the directory:

```bash
mkdir -p src/test/java/assignment1
```

### Example Test Class: `Lopez_OwenTest.java`

Your production code has a modular static method: `generateDate(Random ran)`.
Notice how passing a seeded `Random` makes the test 100% deterministic and
reproducible.

Create `src/test/java/assignment1/Lopez_OwenTest.java`:

```java
package assignment1;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import java.util.Random;

import static org.junit.jupiter.api.Assertions.*;

public class Lopez_OwenTest {

    @Test
    @DisplayName("generateDate should return a non-null, valid date string")
    void testGenerateDateBasic() {
        Random rand = new Random(12345);
        String date = Lopez_Owen.generateDate(rand);

        assertNotNull(date, "Generated date must not be null");
        assertFalse(date.isBlank(), "Generated date must not be blank");
    }

    @Test
    @DisplayName("generateDate format should match '<Month> <DD> <YYYY>'")
    void testGenerateDateFormat() {
        Random rand = new Random(42);
        String date = Lopez_Owen.generateDate(rand);

        // Regex pattern: Word (Month) + Space + 2 digits (Day) + Space + 4 digits (Year)
        String regex = "^[A-Z][a-z]+ \\d{2} \\d{4}$";
        assertTrue(date.matches(regex), 
            "Date string '" + date + "' should match pattern: Month DD YYYY");
    }

    @Test
    @DisplayName("generateDate should produce identical output with identical random seed")
    void testGenerateDateDeterministic() {
        long seed = 987654321L;
        Random rand1 = new Random(seed);
        Random rand2 = new Random(seed);

        String date1 = Lopez_Owen.generateDate(rand1);
        String date2 = Lopez_Owen.generateDate(rand2);

        assertEquals(date1, date2, "Identical seeds must produce identical dates");
    }
}
```

---

## 5. Running Tests with Gradle

### Core Execution Commands

| Command | Action |
| --- | --- |
| `./gradlew test` | Runs all unit tests |
| `./gradlew test --info` | Runs tests and prints individual test names and outcomes |
| `./gradlew test -t` | Continuous mode: reruns tests on file changes |
| `./gradlew test --rerun` | Forces test re-execution even if outputs are up-to-date |

### Running a Specific Test

To target a specific class or method:

```bash
# Run only Lopez_OwenTest
./gradlew test --tests "assignment1.Lopez_OwenTest"

# Run a single test method
./gradlew test --tests "assignment1.Lopez_OwenTest.testGenerateDateFormat"
```

### Inspecting Test Reports

When tests finish, Gradle generates an interactive HTML report:

```text
build/reports/tests/test/index.html
```

You can open this file in any browser, or check failure summaries directly in
the terminal using `./gradlew test --info`.

---

## 6. Testing Interactive Console User Input

When a program uses `Scanner scanner = new Scanner(System.in)`, you cannot
interactively type during automated `./gradlew test` runs. There are three
standard strategies for testing user input.

### Method 1: Automated Unit Testing via Stream Redirection (Recommended)

Java allows replacing standard input (`System.in`) and standard output (`System.out`)
at runtime using `System.setIn(...)` and `System.setOut(...)`.

#### Lifecycle Rules for Stream Tests
1. **Save Original Streams:** In `@BeforeEach`, store the original `System.in` and
   `System.out` pointers.
2. **Inject Simulated Input:** Convert a string with linebreaks (`\n`) into a
   `ByteArrayInputStream`.
3. **Capture Output:** Attach a `ByteArrayOutputStream` to `System.out`.
4. **Restore Streams:** In `@AfterEach`, always restore `System.in` and `System.out`
   so other tests and the Gradle runner are not broken.

#### Complete JUnit 5 Example

```java
package assignment1;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.nio.charset.StandardCharsets;

import static org.junit.jupiter.api.Assertions.*;

public class Lopez_OwenInputTest {

    private final InputStream originalIn = System.in;
    private final PrintStream originalOut = System.out;
    private ByteArrayOutputStream capturedOut;

    @BeforeEach
    void setUp() {
        capturedOut = new ByteArrayOutputStream();
        System.setOut(new PrintStream(capturedOut));
    }

    @AfterEach
    void tearDown() {
        System.setIn(originalIn);
        System.setOut(originalOut);
    }

    private void simulateInput(String inputString) {
        System.setIn(new ByteArrayInputStream(
            inputString.getBytes(StandardCharsets.UTF_8)
        ));
    }

    @Test
    @DisplayName("main should process a food item and compute total on DONE")
    void testSingleFoodItem() {
        // Simulates: item name 'food', price '10.00', then 'DONE'
        String input = "food\n10.00\nDONE\n";
        simulateInput(input);

        Lopez_Owen.main(new String[]{});

        String output = capturedOut.toString();

        // Verify key milestones in output
        assertTrue(output.contains("1 items"), "Should report 1 item");
        assertTrue(output.contains("total 10.00"), "Total should be 10.00");
    }

    @Test
    @DisplayName("main should apply 30% markup to non-food items")
    void testNonFoodMarkup() {
        // Simulates: item name 'shirt', price '10.00', then 'DONE'
        String input = "shirt\n10.00\nDONE\n";
        simulateInput(input);

        Lopez_Owen.main(new String[]{});

        String output = capturedOut.toString();

        // 10.00 * 1.3 = 13.00
        assertTrue(output.contains("total 13.00"), 
            "Total should reflect 30% markup for non-food items");
    }
}
```

---

### Method 2: OOP Architectural Refactoring (Dependency Injection)

Rather than mutating global JVM state with `System.setIn()`, an object-oriented
approach separates input/output streams from the execution logic.

Instead of hardcoding `System.in` and `System.out` directly inside `main()`:

```java
// Production code refactoring
public class Lopez_Owen {
    public static void run(Scanner scanner, PrintStream out) {
        // All business logic runs against the passed scanner and out stream
    }

    public static void main(String[] args) {
        // Production delegates to System.in and System.out
        run(new Scanner(System.in), System.out);
    }
}
```

In your unit test, you instantiate a `Scanner` backed by a `String` directly:

```java
@Test
void testLogicWithoutGlobalStreams() {
    Scanner testScanner = new Scanner("food\n10.00\nDONE\n");
    ByteArrayOutputStream outBuffer = new ByteArrayOutputStream();
    PrintStream testOut = new PrintStream(outBuffer);

    Lopez_Owen.run(testScanner, testOut);

    assertTrue(outBuffer.toString().contains("total 10.00"));
}
```

---

### Method 3: Command-Line Piped Input & Regression Diffing

If you have sample inputs provided by course instructors (e.g., `test1_input.txt`
and `test1_expected.txt`), you can test the entire application from the terminal.

#### Piping Input Files
* **Linux / macOS:**
  ```bash
  ./gradlew -q run < test1_input.txt
  ```
* **Windows CMD:**
  ```cmd
  gradlew -q run < test1_input.txt
  ```

#### Inline Piping
* **Linux / macOS:**
  ```bash
  printf "food\n10.00\nDONE\n" | ./gradlew -q run
  ```
* **Windows CMD:**
  ```cmd
  (echo food & echo 10.00 & echo DONE) | gradlew -q run
  ```

#### Automated Output Diffing
Save actual output and verify against expected output:
```bash
./gradlew -q run < test1_input.txt > actual_output.txt
diff -u actual_output.txt test1_expected.txt
```
If `diff` prints nothing, your output matched the expected output character for character.

