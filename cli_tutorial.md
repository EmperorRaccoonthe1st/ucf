# 🚀 Command Line Showcase & Tutorial

Welcome to the world of the Command Line Interface (CLI)! While it might look like a "hacker screen" from a movie, it is actually the most powerful way to talk to your computer.

Instead of clicking icons, you type **commands**. Here are the basics to get you started!

---

## 1. Finding Your Way Around 🧭

Before you can do anything, you need to know where you are and what is around you.

*   **`pwd` (Print Working Directory):** Shows you exactly which folder you are currently in.
*   **`ls` (List):** Shows you all the files and folders in your current spot.
    *   *Pro Tip:* Try `ls -l` for more detail or `ls -a` to see "hidden" files!
*   **`cd` (Change Directory):** Moves you into a folder.
    *   `cd Documents` takes you into the Documents folder.
    *   `cd ..` (two dots) takes you back up one level.

---

## 2. Creating and Moving Things 🛠️

You don't need a mouse to manage your files.

*   **`mkdir` (Make Directory):** Creates a new folder.
    *   Example: `mkdir MyCoolProject`
*   **`touch`:** Creates a brand new, empty file.
    *   Example: `touch notes.txt`
*   **`cp` (Copy):** Copies a file or folder.
    *   Example: `cp notes.txt backup.txt`
*   **`mv` (Move):** Moves a file or renames it!
    *   Example: `mv notes.txt Secrets/` (Moves it into the Secrets folder)
    *   Example: `mv notes.txt journal.txt` (Renames it)

---

## 3. Reading Files Without Opening an App 📖

*   **`cat` (Concatenate):** Dumps the whole content of a file onto your screen.
*   **`head` / `tail`:** Shows just the first or last 10 lines of a file.
*   **`less`:** Opens a file in a way that lets you scroll up and down (Press `q` to quit!).

---

## 4. Superpowers (Searching & Filtering) 🔍

This is where the CLI gets way faster than a mouse.

*   **`grep`:** Searches for specific text inside files.
    *   Example: `grep "Pizza" grocery_list.txt` (Finds every line with the word Pizza)
*   **`|` (The Pipe):** This is a magic trick. It takes the output of one command and sends it to another.
    *   Example: `ls | grep ".jpg"` (Lists all files, but only shows the ones that end in .jpg)

---

## 5. System Info & Fun Utilities 🖥️

*   **`top` or `htop`:** Shows you all the programs running on your computer and how much "brain power" (CPU) they are using.
*   **`df -h`:** Shows you how much hard drive space you have left in a "human-readable" format.
*   **`curl`:** Can download files or even check the weather!
    *   Try this one: `curl wttr.in` (It shows the weather forecast in your terminal!)

---

## 💡 Top 3 Pro Tips for Beginners

1.  **Tab Completion:** Start typing a filename and hit the `Tab` key. The computer will finish the word for you!
2.  **The Arrow Keys:** Press the **Up Arrow** to see the last command you typed. No need to re-type everything!
3.  **`clear`:** If your screen gets too messy, type `clear` to start with a fresh, blank page.

**Happy Hacking!** 💻
