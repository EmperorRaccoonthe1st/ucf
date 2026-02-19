#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SCORES 5
#define INPUT_FILE "scores.txt"
#define MAX_LEN 101
#define EPSILON 1e-6

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
const double POSITION_BONUS[10] = {3.0, 5.0, 4.0, 6.0, 7.0, 2.0, 8.0, 1.0, 9.0, 1.5}; 
Cat *cats = NULL;
Rivals *rivals = NULL;
double bestPermScore = -1.0;
int **tracker = NULL;

// Function Prototypes
void myMain(FILE *ifile);
char *readStr(FILE *ifile);
int populateCats(FILE *ifile, int n, int c);
int populateRivalsArr(FILE *ifile, int amtCats);
Cat createCat(FILE *ifile);
void findBestCombination(int size, int teamSize, int numTeams, int amtRivals);
void permutate(int size, int teamSize, int numTeams, int *solution, int *is_used, int pos, int amtRivals);
void officiateTeam(int teamSize, int numTeams, int *solution);
double calculatePermScore(int teamSize, int numTeams, int *solution, int amtRivals);
double calculateTeamScore(int size, int *solution, int amtRivals);
double calculateBaseScore(int size, int *solution);
double calculateBonusPoints(int size, int *solution);
int countHighPerformerTraits(int size, int *solution, int pos);
int doesSynergyBonusApply(int size, int *solution, int pos);
int calculatePenalty(int size, int *solution, int amtRivals); 
int doesRivalPenaltyApply(int size, int *solution, int pos, int amtRivals);
int calculateBreedDiversity(int size, int *solution);
double calculatePositionBonus(int size, int *solution);
void printResults(int teamSize, int numTeams, int amtRivals);
void freeCats(int numCats);
void freeTracker(int numTeams);

#ifndef MAIN_FUNCTION
int main(void) {
    FILE *ifile = fopen(INPUT_FILE, "r");
    if(ifile == NULL) {
        printf("File Does Not Exist!\n");
        return 1;
    }
    myMain(ifile);
    fclose(ifile);
    return 0;
}
#endif

void myMain(FILE *ifile) {
    int n, c;    
    if (fscanf(ifile, "%d %d", &n, &c) != 2) return;
    int amtCats = populateCats(ifile, n, c);
    int amtRivals = populateRivalsArr(ifile, amtCats);

    tracker = malloc(n * sizeof(int *));
    for (int i = 0; i < n; i++) tracker[i] = malloc(c * sizeof(int));

    findBestCombination(amtCats, c, n, amtRivals);
    printResults(c, n, amtRivals);

    freeCats(amtCats);
    freeTracker(n);
    free(rivals);
}

int populateCats(FILE *ifile, int n, int c) {
    cats = malloc((n * c) * sizeof(Cat));     
    for (int i = 0; i < (n * c); i++) {
        cats[i] = createCat(ifile);
    }
    return n * c;
}

int populateRivalsArr(FILE *ifile, int amtCats) {
    int amtRivals;
    if (fscanf(ifile, "%d", &amtRivals) != 1) return 0;
    rivals = malloc(amtRivals * sizeof(Rivals));
    for (int i = 0; i < amtRivals; i++) {
        char r1[MAX_LEN], r2[MAX_LEN];
        fscanf(ifile, "%s %s", r1, r2);
        for (int j = 0; j < amtCats; j++) {
            if (strcmp(r1, cats[j].name) == 0) rivals[i].cat1 = &cats[j];
            if (strcmp(r2, cats[j].name) == 0) rivals[i].cat2 = &cats[j];
        }
    }
    return amtRivals;
}

Cat createCat(FILE *ifile) {
    Cat cat;
    char nBuf[MAX_LEN], bBuf[MAX_LEN];
    fscanf(ifile, "%s %s", nBuf, bBuf);
    cat.name = malloc(strlen(nBuf) + 1);
    cat.breed = malloc(strlen(bBuf) + 1);
    strcpy(cat.name, nBuf);
    strcpy(cat.breed, bBuf);

    int sum = 0;
    for (int i = 0; i < MAX_SCORES; i++) {
        fscanf(ifile, "%d", &cat.scores[i]);
        sum += cat.scores[i];
    }
    cat.baseScore = sum;
    return cat;
}

void findBestCombination(int size, int teamSize, int numTeams, int amtRivals) {
    int *is_used = calloc(size, sizeof(int));
    int *solution = malloc(size * sizeof(int));
    permutate(size, teamSize, numTeams, solution, is_used, 0, amtRivals);
    free(is_used);
    free(solution);
}

void permutate(int size, int teamSize, int numTeams, int *solution, int *is_used, int pos, int amtRivals) {
    if (pos == size) {
        double permScore = calculatePermScore(teamSize, numTeams, solution, amtRivals);
        if (permScore > bestPermScore + EPSILON) {
            bestPermScore = permScore;
            officiateTeam(teamSize, numTeams, solution);
        }
        return;
    }
    for (int i = 0; i < size; i++) {
        if (!is_used[i]) {
            solution[pos] = i;
            is_used[i] = 1;
            permutate(size, teamSize, numTeams, solution, is_used, pos + 1, amtRivals);
            is_used[i] = 0;
        }
    }
}

void officiateTeam(int teamSize, int numTeams, int *solution) {
    for (int i = 0; i < numTeams; i++) {
        for (int x = 0; x < teamSize; x++) {
            tracker[i][x] = solution[(i * teamSize) + x];
        }
    } 
}

double calculatePermScore(int teamSize, int numTeams, int *solution, int amtRivals) {
    double total = 0;
    for (int i = 0; i < numTeams; i++) {
        total += calculateTeamScore(teamSize, &solution[i * teamSize], amtRivals);
    }
    return total;
}

double calculateTeamScore(int size, int *solution, int amtRivals) {
    double score = calculateBaseScore(size, solution);
    score += calculateBonusPoints(size, solution);
    score += calculatePenalty(size, solution, amtRivals);
    return score;
}

double calculateBaseScore(int size, int *solution) {
    double sum = 0;
    for (int i = 0; i < size; i++) sum += cats[solution[i]].baseScore;
    return sum / size;
}

double calculateBonusPoints(int size, int *solution) {
    double bonus = (countHighPerformerTraits(size, solution, 0)) * 5.0;
    if (doesSynergyBonusApply(size, solution, 0)) bonus += 30.0;
    bonus += calculateBreedDiversity(size, solution) ? 10.0 : -15.0;
    bonus += calculatePositionBonus(size, solution);
    return bonus;
}

int countHighPerformerTraits(int size, int *solution, int pos) {
    if (pos == size) return 0;
    int current = 0;
    for (int i = 0; i < MAX_SCORES; i++) {
        if (cats[solution[pos]].scores[i] >= 90) current++;
    }
    return current + countHighPerformerTraits(size, solution, pos + 1);
}

int doesSynergyBonusApply(int size, int *solution, int pos) {
    if (pos == size) return 1;
    int hasOne = 0;
    for (int i = 0; i < MAX_SCORES; i++) {
        if (cats[solution[pos]].scores[i] >= 85) { hasOne = 1; break; }
    }
    return hasOne && doesSynergyBonusApply(size, solution, pos + 1);
}

int calculateBreedDiversity(int size, int *solution) {
    for (int i = 0; i < size; i++) {
        for (int j = i + 1; j < size; j++) {
            if (strcmp(cats[solution[i]].breed, cats[solution[j]].breed) == 0) return 0;
        }
    }
    return 1;
}

double calculatePositionBonus(int size, int *solution) {
    double bonus = 0;
    for (int i = 0; i < size; i++) {
        bonus += cats[solution[i]].baseScore * (POSITION_BONUS[i] / 100.0);
    }
    return bonus;
}

int calculatePenalty(int size, int *solution, int amtRivals) {
    return doesRivalPenaltyApply(size, solution, 0, amtRivals) ? -25 : 0;
}

int doesRivalPenaltyApply(int size, int *solution, int pos, int amtRivals) {
    if (pos >= size - 1) return 0;
    for (int i = 0; i < amtRivals; i++) {
        Cat *c1 = &cats[solution[pos]];
        Cat *c2 = &cats[solution[pos + 1]];
        if ((c1 == rivals[i].cat1 && c2 == rivals[i].cat2) || 
            (c1 == rivals[i].cat2 && c2 == rivals[i].cat1)) return 1;
    }
    return doesRivalPenaltyApply(size, solution, pos + 1, amtRivals);
}

void printResults(int teamSize, int numTeams, int amtRivals) {
    printf("Best Teams Grouping Score: %0.2f\n", bestPermScore);
    double bestSingle = -1.0;
    int bestIdx = 0;
    for (int i = 0; i < numTeams; i++) {
        double s = calculateTeamScore(teamSize, tracker[i], amtRivals);
        printf("Team %d: ", i + 1);
        for (int x = 0; x < teamSize; x++) printf("%s ", cats[tracker[i][x]].name);
        printf("%0.2f\n", s);
        if (s > bestSingle + EPSILON) { bestSingle = s; bestIdx = i; }
    }
    printf("Best Candidate: ");
    for (int x = 0; x < teamSize; x++) printf("%s%s", cats[tracker[bestIdx][x]].name, (x == teamSize-1) ? "" : " ");
    printf("\n");
}

void freeCats(int numCats) {
    for (int i = 0; i < numCats; i++) {
        free(cats[i].name);
        free(cats[i].breed);
    }
    free(cats);
}

void freeTracker(int numTeams) {
    for (int i = 0; i < numTeams; i++) free(tracker[i]);
    free(tracker);
}
