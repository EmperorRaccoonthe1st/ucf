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

char *readStr(FILE *ifile);
int populateCats(FILE *ifile, int n, int c);
void populateRivalsArr(FILE *ifile, int amtRivals, int amtCats);
Cat createCat(FILE *ifile);
Rivals createRivals(char *c1, char *c2, int amtCats);
void printState(int amtCats, int amtRivals);
void findBestCombination(int size, int teamSize, int numTeams);
void permutate(int size, int teamSize, int numTeams, int *solution, int *is_used, int pos);
void officiateTeam(int size, int teamSize, int numTeams, int *solution);
double calculatePermScore(int size, int teamSize, int numTeams, int *solution);
double calculateBaseScore(int size, int *solution);
double calculateBonusPoints(int size, int *solution);
int countHighPerformerTraits(int size, int *solution, int pos);
int doesSynergyBonusApply(int size, int *solution, int pos);
int calculatePenalty(int size, int *solution); 
int doesRivalPenaltyApply(int size, int *solution, Cat *prevC, int pos);
int calculateBreedDiversity(int size, int *solution);
double calculatePositionBonus(int size, int *solution);
void printBestTeam(int teamSize, int numTeams);
void freeCats(int numCats);
void freeTracker(int teamSize, int numTeams);
void freeRivals();





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
    
    int n;
    int c;    

    fscanf(ifile, "%d", &n);
    fscanf(ifile, "%d", &c);
    int amtCats = populateCats(ifile, n, c);

    int amtRivals;
    fscanf(ifile, "%d", &amtRivals);
    populateRivalsArr(ifile, amtRivals, amtCats);

    findBestCombination(amtCats, c, n);

    printBestTeam(c, n);

    freeCats(amtCats);
    freeTracker(c, n);
    freeRivals();
}


int populateCats(FILE *ifile, int n, int c) {
    cats = malloc((n * c) * sizeof(Cat));     

    for (int i = 0; i < (n * c); i++) {
        cats[i] = createCat(ifile);
    }

    return n * c;
}


void populateRivalsArr(FILE *ifile, int amtRivals, int amtCats) {

    rivals = malloc(amtRivals * sizeof(Rivals));
    
    for (int i = 0; i < amtRivals; i++) {
        char *c1 = readStr(ifile);
        char *c2 = readStr(ifile);

        Rivals rival = createRivals(c1, c2, amtCats);
        rivals[i] = rival;
        
        free(c1);
        free(c2);
    } 
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
    Rivals r;
    
    for (int i = 0; i < amtCats; i++) {
        if (strcmp(c1, cats[i].name) == 0) r.cat1 = &cats[i];
    }
    
    for (int i = 0; i< amtCats; i++) {
        if (strcmp(c2, cats[i].name) == 0) r.cat2 = &cats[i];
    }

    return r;
}


char *readStr(FILE *ifile) {
    char buff[MAX_LEN];

    fscanf(ifile, "%s", buff);

    char *word = malloc((strlen(buff) + 1) * sizeof(char));    
    strcpy(word, buff);

    return word;
} 


void printState(int amtCats, int amtRivals) {
//    printf("Cats:\n");
//    for (int i = 0; i < amtCats; i++) {
//        printf("%d: %s %s ", i, cats[i].name, cats[i].breed);
//        for (int x = 0; x < MAX_SCORES; x++) {
//            printf("%d ", cats[i].scores[x]);
//        }
//        printf("| %d\n", cats[i].baseScore);
//    }
//
//    printf("Rivals: \n"); 
//
//    for (int i = 0; i < amtRivals; i++) {
//        printf("%d: %s & %s\n", i,  rivals[i].cat1->name, rivals[i].cat2->name);
//    }

    printf("Printing State!\n"); 
    
    printf("bestPermScore: %lf\n", bestPermScore);

    printf("###\n");
}


void findBestCombination(int size, int teamSize, int numTeams) {
    int *is_used = malloc(size * sizeof(int));
    for (int  i = 0; i < size; i++) {
        is_used[i] = 0;
    }

    int *solution = malloc(size * sizeof(int));

    permutate(size, teamSize, numTeams, solution, is_used, 0);

    free(is_used);
    free(solution);
}


void permutate(int size, int teamSize, int numTeams, int *solution, int *is_used, int pos) {

    if (pos == size) {
        double permScore = calculatePermScore(size, teamSize, numTeams, solution);

        if (permScore > bestPermScore + 1e-6) {
            bestPermScore = permScore;

            officiateTeam(size, teamSize, numTeams, solution);
        }

    }

    int num;

    for (int i = 0; i < size; i++) {
        if (is_used[i] == 0) {
            num = i;

            solution[pos] = num;
            is_used[num] = 1;

            permutate(size, teamSize, numTeams, solution, is_used, pos+1);

            is_used[num] = 0;
        }
    }
}


void officiateTeam(int size, int teamSize, int numTeams, int *solution) {
    tracker = malloc(numTeams * sizeof(int *));

    for (int i = 0; i < numTeams; i++) {
        tracker[i] = malloc(teamSize * sizeof(int));
        for (int x = 0; x < teamSize; x++) {
            tracker[i][x] = solution[(i*teamSize) + x];
        }
    } 
}


double calculatePermScore(int size, int teamSize, int numTeams, int *solution) {
    double permScore = 0;

    int **team = malloc(numTeams * sizeof(int *));
    for (int i = 0; i < numTeams; i++) {
        team[i] = malloc(teamSize * sizeof(int));
    } 

    for (int i = 0; i < numTeams; i++) {

        for (int x = 0; x < teamSize; x++) {
            team[i][x] = solution[(i*teamSize) + x];
        }

        permScore += calculateBaseScore(teamSize, team[i]);

        double bonusPoints = calculateBonusPoints(teamSize, team[i]);    
        permScore += bonusPoints;

        double penalty = calculatePenalty(teamSize, team[i]);
        permScore += penalty;
        
    }

    for (int i = 0; i < numTeams; i++) {
        free(team[i]);
    }
    free(team);

    return permScore;
}


double calculateBaseScore(int size, int *solution) {
    double sum = 0;

    for (int i = 0; i < size; i++) {
        sum += cats[solution[i]].baseScore;
    }

    return sum/size;
}


double calculateBonusPoints(int size, int *solution) {
    double bonusPoints = 0;
    
    bonusPoints += (countHighPerformerTraits(size, solution, 0)) * 5;

    if (doesSynergyBonusApply(size, solution, 0) == 1){
        bonusPoints += 30;
    }

    if (calculateBreedDiversity(size, solution)) {
        bonusPoints += 10;
    } else {
        bonusPoints -= 15;
    }

    double positionBonus = calculatePositionBonus(size, solution);
    bonusPoints += positionBonus;
    
    return bonusPoints;
}


int countHighPerformerTraits(int size, int *solution, int pos) {

    int amt = 0;

    if (pos == size) {
        return amt;
    }

    amt = countHighPerformerTraits(size, solution, pos+1);
    for (int i = 0; i < MAX_SCORES; i++) {
        if (cats[solution[pos]].scores[i] > 89) amt++;
    }

    return amt;
}


int doesSynergyBonusApply(int size, int *solution, int pos) {
    int val = 1;

    if (pos == size) {
        return val;
    }

    val = doesSynergyBonusApply(size, solution, pos+1);
    if (val == 0) return 0;

    for (int i = 0; i < MAX_SCORES; i++) {
        if (cats[solution[pos]].scores[i] > 84) {
            return 1; 
        }
    }
    return 0;
}


int calculateBreedDiversity(int size, int *solution) {
    char **used = malloc(size * sizeof(char *)); 

    for (int i = 0; i < size; i++) {
        for (int x = 0; x < i; x++) {
            if (strcmp(cats[solution[i]].breed, used[x]) == 0) {
                free(used);
                return 0;
            }
        }
        used[i] = cats[solution[i]].breed;
    }

    free(used);

    return 1;
}


double calculatePositionBonus(int size, int *solution) {
    double bonus = 0;

    for (int i = 0; i < size; i++) {
        bonus += cats[solution[i]].baseScore * ( 0.01 * POSITION_BONUS[i]);
    }

    return bonus;
}


int calculatePenalty(int size, int *solution) {
    int penalty = 0;

    if (doesRivalPenaltyApply(size, solution, NULL, 0)) penalty -= 25;

    return penalty;
}


int doesRivalPenaltyApply(int size, int *solution, Cat *prevC, int pos) {

    int val = 0;

    if (pos == size) {
        return val;
    }

    val = doesRivalPenaltyApply(size, solution, &cats[solution[pos]], pos+1);
    if (val == 1) return 1;

    if ((prevC == rivals->cat1 || prevC == rivals->cat2) && (&cats[solution[pos]] == rivals->cat1 || &cats[solution[pos]] == rivals->cat2)) {
        return 1;
    } else {
        return 0;
    }       
}


void printBestTeam(int teamSize, int numTeams) {

    printf("Best Teams Grouping Score: %0.2lf\n", bestPermScore);

    double high = 0;
    int highPos = 0;

    for (int i = 0; i < numTeams; i++) {
        double permScore = 0;

        permScore += calculateBaseScore(teamSize, tracker[i]);

        double bonusPoints = calculateBonusPoints(teamSize, tracker[i]);    
        permScore += bonusPoints;

        double penalty = calculatePenalty(teamSize, tracker[i]);
        permScore += penalty;

        printf("Team %d: ", i+1); 

        for (int x = 0; x < teamSize; x++) {
            printf("%s ", cats[tracker[i][x]].name);
        }

        printf("%0.2lf\n", permScore);

        if ( permScore > high + 1e-6 ) {
            high = permScore;
            highPos = i;
        }
    }

    printf("Best Candidate: ");  
    for (int x = 0; x < teamSize; x++) {
        printf("%s ", cats[tracker[highPos][x]].name);
    }
    printf("\n");
}


void freeCats(int numCats) {
    for (int i = 0; i < numCats; i++) {
        free(cats[i].name);
        free(cats[i].breed);
    }

    free(cats);
}


void freeTracker(int teamSize, int numTeams) {
    for (int i = 0; i < numTeams; i++) {
        free(tracker[i]);
    }

    free(tracker);
}


void freeRivals() {
    free(rivals);
}
