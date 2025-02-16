pluginManagement {
    plugins {
        id("com.diffplug.spotless") version "7.0.2"
        id("com.github.johnrengelman.shadow") version "8.1.1"
    }
}

rootProject.name = "snippets"

include(
    ":hello-world",
)
