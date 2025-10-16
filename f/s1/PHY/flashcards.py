#!/usr/bin/env python3

import csv
import random
import argparse
import os
import platform
import textwrap

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_flashcard(definition, result):
    """Prints the flashcard UI."""
    width = 80
    clear_screen()

    # Definition
    print('┌' + '─' * (width - 2) + '┐')
    print('│ ' + "Definition".center(width - 4) + ' │')
    print('├' + '─' * (width - 2) + '┤')
    wrapped_definition = textwrap.wrap(definition, width - 4)
    for line in wrapped_definition:
        print('│ ' + line.ljust(width - 4) + ' │')
    
    # Result
    if result:
        print('├' + '─' * (width - 2) + '┤')
        print('│ ' + "Result".center(width - 4) + ' │')
        print('├' + '─' * (width - 2) + '┤')
        
        result_no_color = result.replace(GREEN, "").replace(RED, "").replace(RESET, "")
        wrapped_result = textwrap.wrap(result_no_color, width - 4)
        
        for i, line in enumerate(wrapped_result):
            # Add color back to the line
            if "Correct!" in result_no_color and i == 0:
                line = GREEN + line
            elif "Incorrect" in result_no_color and i == 0:
                line = RED + line

            # Reset color at the end of the line
            if i == len(wrapped_result) - 1:
                line += RESET

            print('│ ' + line.ljust(width - 4 + len(line) - len(line.replace(GREEN, "").replace(RED, "").replace(RESET, ""))) + ' │')

    print('└' + '─' * (width - 2) + '┘')

def flashcards(filename):
    """
    A simple flashcard program that reads terms and definitions from a CSV file.
    """
    correct_count = 0
    incorrect_count = 0

    while True:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            all_rows = list(reader)
            random_row = random.choice(all_rows)
            term, definition = random_row

            print_flashcard(definition, "")
            user_input = input("Term (or type 'quit' to exit): ")

            if user_input.lower() == 'quit':
                break

            if user_input.lower() == term.lower():
                result_text = f"Correct!"
                correct_count += 1
            else:
                result_text = f"Incorrect. The correct term is: {term}"
                incorrect_count += 1
            
            # Add color to result_text
            if "Correct" in result_text:
                result_text = GREEN + result_text + RESET
            else:
                result_text = RED + result_text + RESET

            print_flashcard(definition, result_text)
            input("\nPress Enter to continue...")

    # Calculate and display summary
    total = correct_count + incorrect_count
    if total > 0:
        percentage = (correct_count / total) * 100
        print("\n--- Session Summary ---")
        print(f"Correct: {correct_count}")
        print(f"Incorrect: {incorrect_count}")
        print(f"Percentage: {percentage:.2f}%")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple flashcard program.')
    parser.add_argument('filename', help='The filename of the CSV file.')
    args = parser.parse_args()
    flashcards(args.filename)
