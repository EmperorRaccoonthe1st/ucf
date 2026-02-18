#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_SCORES 5
#define INPUT_FILE "scores.txt"
#define MAX_LEN 101

/*
    COP 3502C PA2
    This program is written by: Owen Manuel Lopez
*/

typedef struct Cat_s {
    char *name;             // Cat's name (dynamic string)
    char *breed;            // Cat's breed (dynamic string)
    int scores[MAX_SCORES]; // Fixed-sized array for the cat's 5 traits scores
    int baseScore;          // Sum of the cat's 5 traits scores
} Cat;

typedef struct Rivals_s {
    Cat *cat1;              // Pointer to cat1
    Cat *cat2;              // Pointer to cat2
} Rivals;


// Global Variables
const float POSITION_BONUS[10] = {3.0, 5.0, 4.0, 6.0, 7.0, 2.0, 8.0, 1.0, 9.0, 1.5}; 

// The following 4 variables are the only allowed GLOBAL variables.
// These variables can be used or accessed by any functions. They
// do not have to be declared within a function. Further, try to
// prevent declaring local variables using the same names within
// a function to prevent variable shadowing.

Cat *cats = NULL;
Rivals *rivals = NULL;
double bestPermScore = 0;
int **tracker = NULL;


// Function Prototypes
void myMain(FILE *ifile);

// You may add more functions if necessary

void readInput(FILE *ifile, Cat *cats, Rivals *rivals);
char *readStr(FILE *ifile);
int populateCats(FILE *ifile, Cat *cats, int n, int c);
Rivals *populateRivalsArr(FILE *ifile, Rivals *rivals, int amt, int amtCats);
Cat createCat(FILE *ifile);
Rivals createRivals(char *c1, char *c2, int amtCats);
void printState(int amtCats, int amtRivals);




// BEGIN: DO NOT MODIFY THE MAIN FUNCTION
#ifndef MAIN_FUNCTION
int main(void) {
    // Open the input file for reading.
    // This is the only part of the entire code where the file
    // is going to be opened. You should not have any
    // fopen() function call in your functions. Simply
    // pass this existing FILE pointer when necessary.
    FILE *ifile = fopen(INPUT_FILE, "r");
    
    if( ifile == NULL ) {
        printf("File Does Not Exist!\n");
        return 1;
    }
    
    // Calls your own main function and passes the file stream
    myMain(ifile);

    // Close the file
    fclose(ifile);
    
    return 0;
}
#endif
// END: DO NOT MODIFY THE MAIN FUNCTION





// Function Definitions
void myMain(FILE *ifile) {
    // TODO: Complete this function
    
    readInput(ifile, cats, rivals);    
    
    
    
}


void readInput(FILE *ifile, Cat *cats, Rivals *rivals) {
    int n;
    int c;    

    fscanf(ifile, "%d", &n);
    fscanf(ifile, "%d", &c);
    int amtCats = populateCats(ifile, cats, n, c);

    int num;
    fscanf(ifile, "%d", &num);
    rivals = populateRivalsArr(ifile, rivals, num, amtCats);

    printState(amtCats, num);
}


int populateCats(FILE *ifile, Cat *cats, int n, int c) {
    cats = malloc((n * c) * sizeof(Cat));     

    for (int i = 0; i < (n * c); i++) {
        Cat cat = createCat(ifile);
        cats[i] = cat;
    }

    return (n * c);
}


Rivals *populateRivalsArr(FILE *ifile, Rivals *rivals, int amt, int amtCats) {

    rivals = malloc(amt * sizeof(Rivals));
    
    for (int i = 0; i < amt; i++) {
        char *c1 = readStr(ifile);
        char *c2 = readStr(ifile);

        Rivals rival = createRivals(c1, c2, amtCats);
        rivals[i] = rival;
        
        free(c1);
        free(c2);
    } 

    return rivals;
}


Cat createCat(FILE *ifile) {
    Cat cat;

    cat.name = readStr(ifile);
    cat.breed = readStr(ifile);

    for (int i = 0; i < MAX_SCORES; i++) {
        fscanf(ifile, "%d", &cat.scores[i]);
    }

    int sum = 0;
    for (int i = 0; i < MAX_SCORES; i++) {
        sum += cat.scores[i];
    }
    
    cat.baseScore = sum;

    return cat;
} 


Rivals createRivals(char *c1, char *c2, int amtCats) {
    Rivals rivals;
    
    for (int i = 0; i < amtCats; i++) {
        printf("%d\n", i);
        printf("%d: %s to %s\n", i, c1, cats[i].name);
        if (strcmp(c1, cats[i].name) == 0) rivals.cat1 = &cats[i];
    }
    
    for (int i = 0; i< amtCats; i++) {
        printf("%d: %s to %s\n", i, c1, cats[i].name);
        if (strcmp(c2, cats[i].name) == 0) rivals.cat2 = &cats[i];
    }

    return rivals;
}


char *readStr(FILE *ifile) {
    char buff[MAX_LEN];

    fscanf(ifile, "%s", buff);

    char *word = malloc((strlen(buff) + 1) * sizeof(char));    
    strcpy(word, buff);

    return word;
} 


void printState(int amtCats, int amtRivals) {
    printf("Cats:\n");
    for (int i = 0; i < amtCats; i++) {
        printf("%d: %s %s ", i, cats[i].name, cats[i].breed);
        for (int i = 0; i < MAX_SCORES; i++) {
            printf("%d ", cats[i].scores[i]);
        }
        printf("%d\n", cats[i].baseScore);
    }

    printf("Rivals: \n"); 

    for (int i = 0; i < amtRivals; i++) {
        printf("%d: %s & %s\n", i,  rivals[i].cat1->name, rivals[i].cat2->name);
    }

    printf("bestPermScore: %lf\n", bestPermScore);
}
