#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INPUT_FILE "input.txt"

/*
    COP 3502C PA1
    This program is written by: Owen Manuel Lopez 
*/

typedef struct Cat_s {
    char *name;         // Cat's name (dynamic string)
    int age;            // Cat's age
    float weight;       // Cat's weight
    char *breed;        // Cat's breed (already allocated dynamic string)
    int status;         // Cat's status 0, 1, or 2 (default) [index to an array]
} Cat;

typedef struct Kennel_s {
    char *location;     // Kennel's location name (dynamic string)
    int occupancy;      // Actual number of cats currently residing
    Cat **cats;         // The cats residing (dynamic array of pointers to struct)
    int maxCapacity;    // The maximum number of cats that can reside
} Kennel;

typedef struct CatStore_s {
    Kennel *kennels;    // Kennels owned by the store (dynamic array)
    int numKennels;     // Number of kennels owned
    int **capacities;   // Dynamic 2D array indicating the constraints across kennels and breeds
} CatStore;


// Global Variable
const char CAT_STATUS[3][20] = {"ADOPTED", "PENDING", "AVAILABLE"};


// Function Prototypes (Required 14 Functions)
char **readBreeds(FILE *ifile, int *count);
char *lookupBreed(char **dictionary, int breedCount, char *breedName);
CatStore *createStore(FILE *ifile, int kennelCount, char **dictionary, int breedCount);
Kennel *createKennels(FILE *ifile, int kennelCount, char **dictionary, int breedCount, int **constraints);
Cat **createCats(FILE *ifile, char **dictionary, int breedCount, int catCount);
Cat *createSingleCat(FILE *ifile, char **dictionary, int breedCount);
int canMoveTo(CatStore *s, char *location, char *breed, char **dictionary, int breedCount);
Kennel *getKennelByCat(CatStore *s, Cat *cat);
int getCatIndex(Kennel *home, Cat *cat);
Cat *getCatByName(CatStore *s, char *catName);
void removeCatFromKennel(Kennel *k, Cat *cat);
void runQueries(FILE *ifile, CatStore *s, char **dictionary, int breedCount, int numQueries);
void freeBreeds(char **dictionary, int breedCount);
void freeStore(CatStore *store);

// You may add more functions if necessary

int getBreedIndex(char **dictionary, int breedCount, char *breedName);
int findBreedAmt(char **dictionary, char *breedName, Kennel *k);
void query1(FILE *ifile, CatStore *s, char **dictionary, int breedCount);
void query2(FILE *ifile, CatStore *s, char **dictionary, int breedCount);
void query3(FILE *ifile, CatStore *s, char **dictionary, int breedCount);

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
    
    char **dictionary;      // Dynamic array of dynamic strings
    int breedCount;         // The number of strings in dictionary
    
    // Allocate the array and populate it
    dictionary = readBreeds(ifile, &breedCount);
    
    // Read the number of kennels
    int kennelCount;
    fscanf(ifile, "%d", &kennelCount);
    
    // Create a store and populate it
    CatStore *s = createStore(ifile, kennelCount, dictionary, breedCount);
    
    // Read the number of queries
    int numQueries;
    fscanf(ifile, "%d", &numQueries);
    
    // Run the queries
    runQueries(ifile, s, dictionary, breedCount, numQueries);

    // Close the file
    fclose(ifile);
    
    // Deallocate the store and all memory associated within
    freeStore(s);
    
    // Deallocate the array of dynamic strings
    freeBreeds(dictionary, breedCount);
    
    return 0;
}
#endif
// END: DO NOT MODIFY THE MAIN FUNCTION



// Function Definitions
char **readBreeds(FILE *ifile, int *count) {
    // TODO: Complete this function
    // TODO 1 BEGIN

    fscanf(ifile, "%d", count);
    printf("%d\n", *count);
    int tmpC = *count;

    char **breeds = malloc(tmpC * sizeof(char *));

    for (int i = 0; i < tmpC; i++) {
        // Make Tmp Buffer and grab breed
        char buff[100];
        fscanf(ifile, "%s", buff);
        printf("%s\n", buff);

        // Make small sized buffer and copy over
        char *breed = malloc(strlen(buff) * sizeof(char)); 
        strcpy(breed, buff);
        breeds[i] = breed;
    }

    return breeds;

    // TODO 1 END
}

char *lookupBreed(char **dictionary, int breedCount, char *breedName) {
    // TODO: Complete this function
    // TODO 2 BEGIN
    
    for (int i = 0; i < breedCount; i++) {
        if (strcmp(dictionary[i], breedName) == 0) {
            return dictionary[i];
        }
    }

    // TODO 2 END
}

CatStore *createStore(FILE *ifile, int kennelCount, char **dictionary, int breedCount) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    CatStore *s = malloc(sizeof(CatStore));

    s->numKennels = kennelCount;

    int **constraints = malloc(kennelCount * (sizeof(int *)));
    for (int i = 0; i < kennelCount; i++) {
        constraints[i] = malloc(breedCount * sizeof(int));
    }
    s->capacities = constraints;
    Kennel *kennels = createKennels(ifile, kennelCount, dictionary, breedCount, constraints);
    s->kennels = kennels;

    return s;

    // TODO 3 END
}

Kennel *createKennels(FILE *ifile, int kennelCount, char **dictionary, int breedCount, int **constraints) {
    // TODO: Complete this function
    // TODO 4 BEGIN

    // Create Kennel Array
    Kennel *kennels = malloc(kennelCount * sizeof(Kennel));
    
    // Populate Constraints
    for (int i = 0; i < kennelCount; i++) {
        for (int x = 0; x < breedCount; x++) {
            int num;
            fscanf(ifile, "%d", &num); 
            printf("%d ", num);
            constraints[i][x] = num;
        }
        printf("\n");
    }

    // Populate Kennels Array
    for (int i = 0; i < kennelCount; i++) {
        Kennel kennel;
        int occupancy;
        int maxCapacity;

        //Per Kennel Input

        // Make Tmp Input Buff
        char buff[100];
        fscanf(ifile, "%s", buff);
        printf("%s ", buff);
        
        // Copy from tmp to correct sized char array
        char *location = malloc(strlen(buff) * sizeof(char));
        kennel.location = location;

        fscanf(ifile, "%d", &occupancy);
        printf("%d\n", occupancy);
        kennel.occupancy = occupancy;

        //Cat Array Creation
        Cat **cats = createCats(ifile, dictionary, breedCount, occupancy);
        kennel.cats = cats;

        //Calculate Max Capacity
        kennel.maxCapacity = maxCapacity;
        for (int x = 0; x < kennelCount; x++) {
            if (x == i) {
                for (int y = 0; y < breedCount; y++) {
                    maxCapacity += constraints[x][y];
                } 
            }
        }

        kennels[i] = kennel;
      }

    return kennels;

    // TODO 4 END
}

Cat **createCats(FILE *ifile, char **dictionary, int breedCount, int catCount) {
    // TODO: Complete this function
    // TODO 5 BEGIN
    
    Cat **cats = malloc(catCount * sizeof(Cat *));
      
    for (int i = 0; i < catCount; i++) {
        Cat *cat = createSingleCat(ifile, dictionary, breedCount);
        cats[i] = cat;
    }

    return cats;
    // TODO 5 END
}

Cat *createSingleCat(FILE *ifile, char **dictionary, int breedCount) {
    // TODO: Complete this function
    // TODO 6 BEGIN

    Cat *cat = malloc(sizeof(Cat));

    char buff[100];
    fscanf(ifile, "%s", buff);
    printf("%s ", buff);
    char *name = malloc(strlen(buff) * sizeof(char));
    strcpy(name, buff);
    cat->name = name;

    int age;
    fscanf(ifile, "%d", &age);
    printf("%d ", age);
    cat->age = age;

    float weight;
    fscanf(ifile, "%f ", &weight);
    printf("%.2f ", weight);
    cat->weight = weight;
    
    char breedBuff[100];
    fscanf(ifile, "%s", breedBuff);
    printf("%s\n", breedBuff);
    char *breed = lookupBreed(dictionary, breedCount, breedBuff);
    cat->breed = breed;

    return cat; 

    // TODO 6 END
}

int canMoveTo(CatStore *s, char *location, char *breed, char **dictionary, int breedCount) {
    // TODO: Complete this function
    // TODO 7 BEGIN

    for (int i = 0; i < s->numKennels; i++) {
        if (strcmp(s->kennels[i].location, location) == 0) {
            if (s->kennels[i].occupancy == s->kennels[i].maxCapacity) return 0;
            int amtCats = findBreedAmt(dictionary, breed, &(s->kennels[i]));
            if (s->capacities[i][getBreedIndex(dictionary, breedCount, breed)] == amtCats) return 0; 
            return 1;
       }
    }

    return 0;

    // TODO 7 END
}

Kennel *getKennelByCat(CatStore *s, Cat *cat) {
    // TODO: Complete this function
    // TODO 8 BEGIN

    for (int i = 0; i < s->numKennels; i++) {
        for (int x = 0; x < s->kennels[i].occupancy; x++) {
            if (cat == s->kennels[i].cats[x]) return &(s->kennels[i]);
        }
    } 

    return NULL;

    // TODO 8 END
}

int getCatIndex(Kennel *home, Cat *cat) {
    // TODO: Complete this function
    // TODO 9 BEGIN

    for (int i = 0; i < home->occupancy; i++) {
        if (home->cats[i] == cat) return i;
    }

    return -1;
       
    // TODO 9 END
}

Cat *getCatByName(CatStore *s, char *catName) {
    // TODO: Complete this function
    // TODO 10 BEGIN

    for (int i = 0; i < s->numKennels; i++) {
        for (int x = 0; x < s->kennels[i].occupancy; x++) {
            if (strcmp(s->kennels[i].cats[x]->name, catName) == 0) return s->kennels[i].cats[x];
        }
    } 

    return NULL;

    // TODO 10 END
}

void removeCatFromKennel(Kennel *k, Cat *cat) {
    // TODO: Complete this function
    // TODO 11 BEGIN
    
    for (int i = 0; i < k->occupancy; i++) {
        if (k->cats[i] == cat) {
            for (int x = i; x < k->occupancy - 1; x++) {
                k->cats[x] = k->cats[x+1];
            }
        } 
    }  

    k->occupancy -= 1;

    // TODO 11 END
}

void runQueries(FILE *ifile, CatStore *s, char **dictionary, int breedCount, int numQueries) {
    // TODO: Complete this function
    // TODO 12 BEGIN

    printf("###\nIn Function:\n");
    printf("NumQueries: %d\n", numQueries);
    for (int z = 0; z < numQueries; z++) {
        int queryType = 0;
        fscanf(ifile, "%d", &queryType);
        printf("%d\n", queryType);

        switch (queryType) {
            case 1:
                query1(ifile, s, dictionary, breedCount);
                break;

            case 2:
                query2(ifile, s, dictionary, breedCount);
                break;

            case 3:
                query3(ifile, s, dictionary, breedCount);
                break;
        }
    }

    // TODO 12 END
}

void freeBreeds(char **dictionary, int breedCount) {
    // TODO: Complete this function
    // TODO 13 BEGIN





    // TODO 13 END
}

void freeStore(CatStore *store) {
    // TODO: Complete this function
    // TODO 14 BEGIN





    // TODO 14 END
}

// You may add more functions if necessary

int getBreedIndex(char **dictionary, int breedCount, char *breedName) {
    int index = 0;
    
    for (int i = 0; i < breedCount; i++) {
        if (strcmp(dictionary[i], breedName) == 0) {
            index = i;
            break;
        }
    }
    
    return index;
}


int findBreedAmt(char **dictionary, char *breedName, Kennel *k) {
    int amt;
    
    for (int i = 0; i < k->occupancy; i++) {
        if (strcmp(k->cats[i]->breed, breedName) == 0) amt++;
    }
    
    return amt;
}


void query1(FILE *ifile, CatStore *s, char **dictionary, int breedCount) {
    char buff[100];
    fscanf(ifile, "%s", buff);
    char *breed = lookupBreed(dictionary, breedCount, buff);

    for (int i = 0; i < s->numKennels; i++) {
        if (findBreedAmt(dictionary, breed, &(s->kennels[i])) == 0) {
            printf("No cat with breed %s\n", breed);
            continue;
        }

        printf("Location: |");
        printf("%s|\n", s->kennels[i].location);

        for (int x = 0; x < s->kennels[i].occupancy; x++) {
            if (strcmp(s->kennels[i].cats[x]->breed, breed) == 0) {
                printf("%s ", s->kennels[i].cats[x]->name);
                printf("%.2f ", s->kennels[i].cats[x]->weight);
                printf("%d ", s->kennels[i].cats[x]->age);
                printf("%s ", s->kennels[i].location);
                printf("%s\n", CAT_STATUS[s->kennels[i].cats[x]->status]);
            }
        }
    }                
}


void query2(FILE *ifile, CatStore *s, char **dictionary, int breedCount) {
    int status;
    fscanf(ifile, "%d",  &status);

    char name[100];
    fscanf(ifile, "%s", name);

    Cat *cat = getCatByName(s, name);
    cat->status = status;
    
    printf("%s is now %s!\n", name, CAT_STATUS[status]);
}


void query3(FILE *ifile, CatStore *s, char **dictionary, int breedCount) {
    char name[100];
    fscanf(ifile, "%s", name);
    
    char location[100];
    fscanf(ifile, "%s", location);

    Cat *cat = getCatByName(s, name);
    Kennel *k = getKennelByCat(s, cat);

    if (canMoveTo(s, location, cat->breed, dictionary, breedCount) == 1) {
         for (int i = 0; i < s->numKennels; i++) {
            if (strcmp(s->kennels[i].location, location) == 0) {
                s->kennels[i].cats[s->kennels[i].occupancy] = cat;
                removeCatFromKennel(k, cat);
            }
        }         
        printf("%s moved successfully to %s\n", name, location);
    } else {
        printf("%s cannot take a %s cat!\n", location, cat->breed);
    } 
}
