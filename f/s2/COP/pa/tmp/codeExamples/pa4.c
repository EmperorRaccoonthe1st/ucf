#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INPUT_FILE "scores.txt"
#define NUM_TRAITS 7
#define TOTAL_IDX 6
#define MAX_LEN 13
#define BASE_CASE_SIZE 30

/*
    COP 3502C PA4
    This program is written by: Owen Manuel Lopez
*/

typedef struct Cat_s {
    char *name;         	   // Cat's name (unique)
    int scores[NUM_TRAITS];
} Cat;


// Global Variable
const char TRAITS[NUM_TRAITS][MAX_LEN] = {
    "Cuteness", "Fluffiness", "Agility", "Friendliness", 
    "Intelligence", "Laziness", "Total"
};


// Function Prototypes
void myMain(FILE *ifile);
int compareTo(Cat *ptrC1, Cat *ptrC2, int key);
void mergeSort(Cat **list, int n, int key);
void mergeSortRec(Cat **list, int low, int high, int key);
void quickSort(Cat **list, int n, int key);
void quickSortRec(Cat **list, int low, int high, int key);

// You may add more functions if necessary

Cat **readCats(FILE *ifile, int num);
Cat *createCat(FILE *ifile);
void printCats(Cat **cats, int low, int high, int key);
void freeCats(Cat **cats, int n);
void freeCat(Cat *cat);
void merge(Cat **list, int low, int mid, int high, int key);
void insertionSort(Cat **list, int low, int high, int key);
int partition(Cat **list, int low, int high, int key);
void swap(Cat **c1, Cat **c2);



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
    // TODO 1 BEGIN

    // Cat Input
    int numCats;
    fscanf(ifile, "%d", &numCats);
    Cat **cats = readCats(ifile, numCats);


    // Core Logic

    int sortType;
    int key;

    fscanf(ifile, "%d", &sortType);
    fscanf(ifile, "%d", &key);

    if (sortType == 1) {
        mergeSort(cats, numCats, key);
    } else {
        quickSort(cats, numCats, key);
    }


    // Using an Arena here would be more fun 
    freeCats(cats, numCats);

    // TODO 1 END
}

int compareTo(Cat *ptrC1, Cat *ptrC2, int key) {
    // TODO: Complete this function
    // TODO 2 BEGIN

    if (ptrC1->scores[key] > ptrC2->scores[key]) {
        return -1;
    } else if (ptrC1->scores[key] < ptrC2->scores[key]) {
        return 1;
    }

    return strcmp(ptrC1->name, ptrC2->name);

    // TODO 2 END
}

void mergeSort(Cat **list, int n, int key) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    //printf("Merge Sorting from %d to %d\n", 0, n);
    mergeSortRec(list, 0, n-1, key);  

    printCats(list, 0, n, key);

    // TODO 3 END
}

void mergeSortRec(Cat **list, int low, int high, int key) {
    // TODO: Complete this function
    // TODO 4 BEGIN

   //printf("Sort Range: %d - %d\n", low, high);

    if (abs(high - low) < 31) {
       //printf("Total number of items in array (%d - %d) is under 30. Switching to insertionSort!\n", high, low);
        insertionSort(list, low, high, key);
        return;
    }

    int mid = (low + high + 1) / 2;
   
    mergeSortRec(list, low, mid-1, key);

    mergeSortRec(list, mid, high, key);

    merge(list, low, mid, high, key);
    //printCats(list, low, high, key);

    // TODO 4 END
}

void quickSort(Cat **list, int n, int key) {
    // TODO: Complete this function
    // TODO 5 BEGIN

    quickSortRec(list, 0, n-1, key);

    printCats(list, 0, n, key);

    // TODO 5 END
}

void quickSortRec(Cat **list, int low, int high, int key) {
    // TODO: Complete this function
    // TODO 6 BEGIN

    if (abs(high - low) < 31) {
        insertionSort(list, low, high, key);
        return;
    }

    int p = partition(list, low, high, key);

    quickSortRec(list, low, p-1, key);
    quickSortRec(list, p+1, high, key);

    // TODO 6 END
}


Cat **readCats(FILE *ifile, int num) {


    Cat **cats = malloc(num * sizeof(Cat *));

    for (int i = 0; i < num; i++) {
        Cat *cat = createCat(ifile);

        cats[i] = cat;
    }

    return cats;
}

 
Cat *createCat(FILE *ifile) {

    Cat *cat = malloc(sizeof(Cat));

    char buff[MAX_LEN];
    fscanf(ifile, "%s", buff);

    char *name = malloc((strlen(buff) + 1) * sizeof(char));
    strcpy(name, buff);
    cat->name = name;

    int sum = 0;
    for (int i = 0; i < NUM_TRAITS - 1; i++) {
        fscanf(ifile, "%d", &cat->scores[i]);
        sum += cat->scores[i];
    } 
    cat->scores[NUM_TRAITS - 1] = sum;
    
    return cat;
}


void printCats(Cat **cats, int low, int high, int key) {

    printf("%s Rank List\n", TRAITS[key]);

    for (int i = low; i < high; i++) {
        printf("%d. %-15s %d\n", i+1, cats[i]->name, cats[i]->scores[key]);
    }
}


void freeCats(Cat **cats, int n) {

    for (int i = 0; i < n; i++) {
        freeCat(cats[i]);
    }

    free(cats);
}


void freeCat(Cat* cat) {

    free(cat->name);

    free(cat);

}


void merge(Cat **list, int low, int mid, int high, int key) {

    //printf("Attempting to merge %d %d %d\n", low, mid, high);
    int size = high - low + 1;
    Cat **tmp = malloc(size * sizeof(Cat *));

    int i = low;
    int j = mid;

    int p = 0;


    while (i < mid && j <= high) {
        if (compareTo(list[i], list[j], key) < 1) {
            tmp[p] = list[i++];
        } else {
            tmp[p] = list[j++];
        }

        p++;
    }

    //printf("Majority of both arrays sorted! Now to fill the overflow\n");


    while (i < mid) {
        tmp[p++] = list[i++];
    }
    while (j <= high) {
        tmp[p++] = list[j++];
    }

    for (int x = low, pos = 0; x <= high; x++, pos++) {
        list[x] = tmp[pos];
    }

    
    free(tmp);

    //printf("Array Merged!\n");
}


void insertionSort(Cat **list, int low, int high, int key) {
    for (int i = low; i < high + 1; i++) {
        Cat *tmp = list[i];
        int j;

        for (j = i-1; j >= low && compareTo(tmp, list[j], key) < 0; j--) {
            list[j+1] = list[j];
        }

        list[j+1] = tmp;
    }    

}


int partition(Cat **list, int low, int high, int key) {
    int pivot = (rand() % (high - low + 1)) + low;
    swap(&list[pivot], &list[high]);

    pivot = high;
    int j = low - 1;
    
    for (int i = low; i <= high - 1; i++) {
        if (compareTo(list[i], list[pivot], key) < 1) {
            j++;        
            swap(&list[i], &list[j]);
        }
    } 

    swap(&list[j + 1], &list[high]);
    
    return j + 1;
}


void swap(Cat **c1, Cat **c2) {
    Cat *buff = *c1;

    *c1 = *c2;

    *c2 = buff;
}
