plugins {
    application
    java
}

version = "1.0-0"

repositories {
    mavenCentral()
}

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(21) // Change to your preferred Java version
    }
}

application {
    // Define the main class for the application
    mainClass.set("assignment3.CarDataProcess")
}

tasks.named<JavaExec>("run") {
    standardInput = System.`in`
}
