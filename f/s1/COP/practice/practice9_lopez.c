#include <stdio.h>
#include <string.h>
#include <ctype.h>
#define MAX_WORDS 200
#define MAX_LEN 101
#define FILE_NAME_1 "words1.txt"
#define FILE_NAME_2 "words2.txt"


// COP 3223C Fall 2025
// Student Name: Owen Lopez
// File Name: practice9_lopez.c

// IMPORTANT: Rename this file using your actual surname in lowercase,
// removing any whitespace or dashes. Do not modify or remove any TODO 
// comments, as doing so will interfere with the grading system. 
// Only make changes within the function bodies. No other parts of 
// the file will be graded, so do not alter any other code.


// Function Prototypes
char *trim_string(char *str);
char *to_lower(char *str);
int populate_list(char list[MAX_WORDS][MAX_LEN], int *size,
int max_size, char *fname);
void print_list(char words[MAX_WORDS][MAX_LEN], int size);
int contains_word(char words[MAX_WORDS][MAX_LEN], int size, char *query);
void combine_lists(char list1[MAX_WORDS][MAX_LEN], int list1_size,
char list2[MAX_WORDS][MAX_LEN], int list2_size,
char list3[MAX_WORDS][MAX_LEN], int *list3_size);
void selection_sort(char words[MAX_WORDS][MAX_LEN], int size);


// DO NOT MODIFY THIS PORTION OF THE MAIN FUNCTION
#ifndef MAIN_FUNCTION
int main(void) {
    char list1[MAX_WORDS][MAX_LEN];  // assume size up to MAX_WORDS
    char list2[MAX_WORDS][MAX_LEN];  // assume size up to MAX_WORDS
    char list3[MAX_WORDS][MAX_LEN];  // to store common words; size up to MAX_WORDS
    
    int list1_size = 0, list2_size = 0, list3_size = 0;
    
    // populate the two lists using the two input files
    int flag1 = populate_list(list1, &list1_size, MAX_WORDS, FILE_NAME_1);
    int flag2 = populate_list(list2, &list2_size, MAX_WORDS, FILE_NAME_2);
    
    // terminate the program if unsuccessful in loading either list
    if( !flag1 || !flag2 ) return 0;
    
    //print_list(list1, list1_size);    // test if read correctly
    //print_list(list2, list2_size);    // test if read correctly
    
    // combine list1 and list2 and put the result in list3
    //combine_lists(list1, list1_size, list2, list2_size, list3, &list3_size);
     
    // sort the list in ascending order
    //selection_sort(list3, list3_size);
    
    // print the output list
    //print_list(list3, list3_size);
    
    return 0;
}
#endif
// DO NOT MODIFY THIS PORTION OF THE MAIN FUNCTION


// Function Definitions
char *trim_string(char *str) {
    // TODO: Complete this function
    // TODO 1 BEGIN
    int pos;
    pos = strcspn(str, "\n");
    str[pos] = '\0';
    
    return str;
    // TODO 1 END
}

char *to_lower(char *str) {
    // TODO: Complete this function
    // TODO 2 BEGIN
    int count = 0;
    while (true) {
        if (str[count] == '\n' || str[count] == '\0') break;
        str[count] = tolower(str[count]);
        count++;
    }
    
     return str;
    // TODO 2 END 
}

int populate_list(char list[MAX_WORDS][MAX_LEN], int *size, int max_size, char *fname) {
    // TODO: Complete this function
    // TODO 3 BEGIN
    FILE *rfile = NULL;
    char buff[MAX_LEN];
    int count = 0;
    
    rfile = fopen(fname, "r");
    if (rfile == NULL) return 0;
    printf("rfile: %p\n", rfile);

    while (fgets(buff, MAX_LEN, rfile) != NULL) {
        fgets(buff, MAX_LEN, rfile);
        trim_string(buff);
        to_lower(buff);
        strcpy(list[count], buff); 
        printf("%s\n", list[count]);
        count++;
    }

    fclose(rfile);
    return 1;
    // TODO 3 END
}

void print_list(char words[MAX_WORDS][MAX_LEN], int size) {
    // TODO: Complete this function
    // TODO 4 BEGIN





    // TODO 4 END
}

int contains_word(char words[MAX_WORDS][MAX_LEN], int size, char *query) {
    // TODO: Complete this function
    // TODO 5 BEGIN





    // TODO 5 END
}

void combine_lists(char list1[MAX_WORDS][MAX_LEN], int list1_size,
                   char list2[MAX_WORDS][MAX_LEN], int list2_size,
                   char list3[MAX_WORDS][MAX_LEN], int *list3_size) {
    // TODO: Complete this function
    // TODO 6 BEGIN




 
    // TODO 6 END 
}

void selection_sort(char words[MAX_WORDS][MAX_LEN], int size) {
    // TODO: Complete this function
    // TODO 7 BEGIN
    
    
    
    
    
    // TODO 7 END
}

