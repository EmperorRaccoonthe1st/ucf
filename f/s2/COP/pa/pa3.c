#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INPUT_FILE "logs.txt"
#define MAX_LENGTH 101

/*
    COP 3502C PA3
    This program is written by: Owen Manuel Lopez
*/

typedef struct Cat_s {
    int arrival;            // Cat's arrival time at the clinic 
                            // Minutes since clinic opened (unique)
    char *name;             // Cat's unique name (dynamic string)
    int duration;           // Required treatment time in minutes
} Cat;

typedef struct SLLNode_s {
    Cat *cat;               // Pointer to a dynamically allocated Cat
    struct SLLNode_s *next;
} SLLNode;

// Function Prototypes
void myMain(FILE *ifile);

// You may add more functions if necessary

SLLNode *readCats(FILE *ifile);
Cat *createCat(int arrival, char *name, int duration);
void eventLoop(SLLNode **cats, SLLNode **exposed, SLLNode **queue, SLLNode **rejected);
Cat *getCurrentCat(SLLNode **cats, int t);
void pushToSLL(SLLNode **sll, Cat *cat);
Cat *popFromSLL(SLLNode **sll);
Cat *getNextCatFromQueue(SLLNode **queue, SLLNode **rejected, int t);
void printRejected(SLLNode *rejected);
void printExposed(SLLNode *cur);
void printSLL(SLLNode *sll);
void freeSLL(SLLNode *sll);
void freeCats(SLLNode *sll);
void rejectLateCatsSLLNode(SLLNode **cats, SLLNode **rejected);
void rejectCatsInQueue(SLLNode **queue, SLLNode **rejected);


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
    
    SLLNode *cats = readCats(ifile);
    //printSLL(cats);
    //printf("Cats SLL Created!\n###\n");
    
    SLLNode *exposed = NULL;
    SLLNode *queue = NULL;
    SLLNode *rejected = NULL;
        
    eventLoop(&cats, &exposed, &queue, &rejected);

    rejectLateCatsSLLNode(&cats, &rejected);
    rejectCatsInQueue(&queue, &rejected);
    printRejected(rejected);

    if (exposed == NULL) {
        printf("No Exposed Cats\n");
    } else {
        printf("Exposed Cats\n");
        printExposed(exposed);
    }

    freeSLL(exposed);
    freeSLL(rejected);
    freeCats(cats);

}


SLLNode *readCats(FILE *ifile) {

    SLLNode *cats = NULL;

    while (1) {
        int arrival, duration;
        char buff[MAX_LENGTH];

        fscanf(ifile, "%d", &arrival);
        if (arrival == -1) break;

        fscanf(ifile, "%s", buff);
        char *name = malloc((strlen(buff) + 1) * sizeof(char));
        strcpy(name, buff);

        fscanf(ifile, "%d", &duration);

        SLLNode *n = malloc(sizeof(SLLNode));
        n->cat = createCat(arrival, name, duration);
        n->next = NULL;

        if (cats == NULL || n->cat->arrival < cats->cat->arrival) {
            n->next = cats;
            cats = n;
        } 
        else {
            SLLNode *temp = cats;
            while (temp->next != NULL && temp->next->cat->arrival < n->cat->arrival) {
                temp = temp->next;
            }
            n->next = temp->next;
            temp->next = n;
        }
    }

    return cats;
}


Cat *createCat(int arrival, char *name, int duration) {
    Cat *c = malloc(sizeof(Cat)); 

    c->arrival = arrival;
    c->duration = duration;
    c->name = name;

    return c;
}


void eventLoop(SLLNode **cats, SLLNode **exposed, SLLNode **queue, SLLNode **rejected) {

    int unoBusy = 0;
    int dosBusy = 0;

    for (int t = 0; t < 481; t++) {
        Cat *newCat = getCurrentCat(cats, t);

        if (newCat != NULL) {
            if (newCat->duration != 0) {
                pushToSLL(queue, newCat);
            } else {
                free(newCat->name);
                free(newCat);
            }
        }

        if (unoBusy < 1) {
            Cat *c = getNextCatFromQueue(queue, rejected, t);

            if (c != NULL) {
                unoBusy = c->duration;

                printf("Doctor Uno treated %s at %d\n", c->name, t);

                free(c->name);
                free(c);
            }
        }
        unoBusy--;

        if (dosBusy < 1) {
            Cat *c = getNextCatFromQueue(queue, rejected, t);

            if (c != NULL) {
                dosBusy = c->duration;

                pushToSLL(exposed, c);

                printf("Doctor Dos treated %s at %d\n", c->name, t);
            }

        }
        dosBusy--;
    }
}


Cat *getCurrentCat(SLLNode **cats, int t) {

    if ((*cats) == NULL) return NULL;

    if ((*cats)->cat->arrival == t) {
        return popFromSLL(cats);
    } 

    return NULL;
}


void pushToSLL(SLLNode **sll, Cat *cat) {
    
    SLLNode *n = malloc(sizeof(SLLNode));
    n->next = NULL;
    n->cat = cat;

    if (*sll == NULL) {
        *sll = n;
    } else {
        SLLNode *cur = *sll; 
        while (cur->next != NULL) {
            cur = cur->next;
        }

        cur->next = n;
    }
}


Cat *popFromSLL(SLLNode **sll) {
    Cat *cat = NULL;

    if (*sll != NULL) {
        SLLNode *head = *sll;

        cat = head->cat;

        *sll = head->next;

        free(head);
    }

    return cat;
}


Cat *getNextCatFromQueue(SLLNode **queue, SLLNode **rejected, int t) {

    while (1) {
        Cat *c = popFromSLL(queue);

        if (c == NULL) return NULL;

        if (t + c->duration <= 480) {
            return c;
        } else {
           pushToSLL(rejected, c); 
        }
    }
}


void printRejected(SLLNode *rejected) {
    if (rejected == NULL) return;

    SLLNode *cur = rejected;
    while (cur != NULL) {
        printf("Cannot accommodate %s\n", cur->cat->name);
        cur = cur->next;
    }

}


void printExposed(SLLNode *cur) {

    if (cur == NULL) {
        return;
    }

    printExposed(cur->next);
    printf("%s\n", cur->cat->name);

}


void printSLL(SLLNode *sll) {
    if (sll == NULL) {
        printf("SLL Empty!\n");
        return;
    }

    printf("[");
    
    SLLNode *cur = sll;
    while (cur != NULL) {
        printf("%s, ", cur->cat->name);
        cur = cur->next;
    }

    printf("]\n");
}


void freeSLL(SLLNode *sll) {
    
    if (sll == NULL) return;
    
    SLLNode *cur = sll;
    while (cur != NULL) {
        SLLNode *last = cur;

        cur = last->next;
        free(last->cat->name);
        free(last->cat);
        free(last);
    }

}


void freeCats(SLLNode *sll) {
    if (sll == NULL) return;
    
    SLLNode *cur = sll;
    while (cur != NULL) {
        SLLNode *last = cur;

        cur = last->next;

        free(last->cat->name);
        free(last->cat);
        free(last);
    }
}


void rejectLateCatsSLLNode(SLLNode **cats, SLLNode **rejected) {
    while (*cats != NULL) {
        Cat *cat = popFromSLL(cats);
        pushToSLL(rejected, cat);
    }

}


void rejectCatsInQueue(SLLNode **queue, SLLNode **rejected) {
    while (*queue != NULL) {
        pushToSLL(rejected, popFromSLL(queue));
    }
}
