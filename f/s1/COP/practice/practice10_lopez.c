#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_WORDS 2000          // Maximum number of words the list can store
#define MAX_LEN 101             // Maximum length of a word (100 chars + null)
#define FILE_NAME "words.txt"


// COP 3223C Fall 2025
// Student Name: Owen_Lopez
// File Name: practice10_lopez.c

// IMPORTANT: Rename this file using your actual surname in lowercase,
// removing any whitespace or dashes. Do not modify or remove any TODO 
// comments, as doing so will interfere with the grading system. 
// Only make changes within the function bodies. No other parts of 
// the file will be graded, so do not alter any other code.


typedef struct WordFreq_s {
    char word[MAX_LEN];         // a single word
    int freq;                   // how many times it appeared
} WordFreq;

typedef struct WordList_s {
    WordFreq words[MAX_WORDS];  // array of WordFreq structs
    int size;                   // current logical size (number of elements used)
    int capacity;               // maximum number of elements allowed
} WordList;


// Function Prototypes
WordFreq create_word(const char *word);
WordList create_list(int capacity);
WordFreq *get_word(WordList *list, const char *query);
void increment_count(WordFreq *word);
void add_word(WordList *list, const char *word);
void process_word(WordList *list, char *line);
void print_list(const WordList *list);
int populate_list(WordList *list, const char *filename);
void selection_sort(WordList *list);

// Helper Functions (in case you need them)
char *to_lower(char *str);
void clear_buffer(FILE *fp);
char *trim_string(char *str);



// DO NOT MODIFY THIS PORTION OF THE MAIN FUNCTION
#ifndef MAIN_FUNCTION
int main(void) {
    // Create an empty word list with the MAX_WORDS capacity
    WordList words = create_list(MAX_WORDS);
    
    // Load words from the text file and build the frequency list
    if( !populate_list(&words, FILE_NAME) )
        return 0;
    
    // Sort by frequency (descending), breaking ties alphabetically
    selection_sort(&words);
    
    // Display results
    print_list(&words);

    return 0;
}
#endif
// DO NOT MODIFY THIS PORTION OF THE MAIN FUNCTION



// Function Definitions
WordFreq create_word(const char *word) {
    // TODO: Complete this function
    // TODO 1 BEGIN
    
    
    
    
    
    // TODO 1 END
}

WordList create_list(int capacity) {
    // TODO: Complete this function
    // TODO 2 BEGIN
    
    
    
    
    
    // TODO 2 END
}

WordFreq *get_word(WordList *list, const char *query) {
    // TODO: Complete this function
    // TODO 3 BEGIN
    
    
    
    
    
    // TODO 3 END
}

void increment_count(WordFreq *word) {
    // TODO: Complete this function
    // TODO 4 BEGIN
    
    
    
    
    
    // TODO 4 END
}

void add_word(WordList *list, const char *word) {
    // TODO: Complete this function
    // TODO 5 BEGIN
    
    
    
    
    
    // TODO 5 END
}

void process_word(WordList *list, char *line) {
    // TODO: Complete this function
    // TODO 6 BEGIN
    
    
    
    
    
    // TODO 6 END
}

void print_list(const WordList *list) {
    // TODO: Complete this function
    // TODO 7 BEGIN
    
    
    
    
    
    // TODO 7 END
}

int populate_list(WordList *list, const char *filename) {
    // TODO: Complete this function
    // TODO 8 BEGIN
    
    
    
    
    
    // TODO 8 END
}

void selection_sort(WordList *list) {
    // TODO: Complete this function
    // TODO 9 BEGIN
    
    
    
    
    
    // TODO 9 END
}



// Provided Helper Functions

char *to_lower(char *str) {
    // Convert a string to lowercase (in place)
    int len = strlen(str);
    for(int i = 0; i < len; i++) {
        str[i] = tolower(str[i]);
    }
    return str;
}

void clear_buffer(FILE *fp) {
    // Clear all characters until newline or EOF.
    int c;
    if(fp == NULL) return;
    
    while( (c = fgetc(fp)) != '\n' && c != EOF );
}

char *trim_string(char *str) {
    // Remove the first newline character from a string.
    int pos = strcspn(str, "\n");
    str[pos] = '\0';
    return str;
}

