#!/usr/bin/env python3

import csv
import random
import argparse
import os
import platform
import textwrap
import Levenshtein
import readline

readline.parse_and_bind('set editing-mode emacs')

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
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

def print_summary(correct_count, incorrect_count, percentage):
    """Prints the summary UI."""
    width = 80
    clear_screen()

    # Title
    print('┌' + '─' * (width - 2) + '┐')
    print('│ ' + "Session Summary".center(width - 4) + ' │')
    print('├' + '─' * (width - 2) + '┤')

    # Stats
    correct_text = f"Correct: {correct_count}"
    incorrect_text = f"Incorrect: {incorrect_count}"
    percentage_text = f"Percentage: {percentage:.2f}%"

    print('│ ' + f"{GREEN}{correct_text.ljust(width - 4)}{RESET}" + ' │')
    print('│ ' + f"{RED}{incorrect_text.ljust(width - 4)}{RESET}" + ' │')

    if percentage >= 80:
        color = GREEN
    elif percentage >= 60:
        color = YELLOW
    else:
        color = RED

    print('│ ' + f"{color}{percentage_text.ljust(width - 4)}{RESET}" + ' │')

    print('└' + '─' * (width - 2) + '┘')

def flashcards(filename):
    """
    A simple flashcard program that reads terms and definitions from a CSV file.
    """
    correct_count = 0
    incorrect_count = 0

    try:
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

                print(f"DEBUG: Term from CSV: '{term}'")
                print(f"DEBUG: User input: '{user_input}'")

                is_correct = False
                term_stripped = term.strip()
                user_input_stripped = user_input.strip()

                is_numeric_term = False
                try:
                    float(term_stripped)
                    is_numeric_term = True
                except ValueError:
                    pass

                print(f"DEBUG: is_numeric_term: {is_numeric_term}")

                if is_numeric_term:
                    # If term is a pure number, require exact match
                    comparison_result = (user_input_stripped.lower() == term_stripped.lower())
                    print(f"DEBUG: Numeric comparison result: {comparison_result}")
                    if comparison_result:
                        is_correct = True
                else:
                    # If term is not a pure number (could be word or alphanumeric)
                    # Check if it contains any digits
                    contains_digit = any(char.isdigit() for char in term_stripped)
                    print(f"DEBUG: contains_digit: {contains_digit}")

                    if contains_digit:
                        # If it contains digits but is not a pure number, require exact match
                        comparison_result = (user_input_stripped.lower() == term_stripped.lower())
                        print(f"DEBUG: Alphanumeric comparison result: {comparison_result}")
                        if comparison_result:
                            is_correct = True
                    else:
                        # If it's a pure word, allow Levenshtein distance
                        distance = Levenshtein.distance(user_input_stripped.lower(), term_stripped.lower())
                        print(f"DEBUG: Levenshtein distance: {distance}")
                        if distance <= 2:
                            is_correct = True
                print(f"DEBUG: Final is_correct: {is_correct}")

                if is_correct:
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
    except KeyboardInterrupt:
        pass
    finally:
        # Calculate and display summary
        total = correct_count + incorrect_count
        if total > 0:
            percentage = (correct_count / total) * 100
            print_summary(correct_count, incorrect_count, percentage)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple flashcard program.')
    parser.add_argument('filename', help='The filename of the CSV file.')
    args = parser.parse_args()
    flashcards(args.filename)