// Arup Guha
// 2/5/2026
// Code for COP 3502H Exam 1 Questions 1, 3, 5

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAXLEN 50

typedef struct UCFStudent {
	char* first;
	char* last;
	int UCFID;
} UCFStudent;

int* reverseCopy(int* numbers, int n);
UCFStudent** readStudentData(int n);
int sumArithSequence(int firstTerm, int diff, int nTerms);
void print(int* arr, int n);
void printStudent(UCFStudent* ptr);

int main() {

    // Test for #1
    printf("%d\n", sumArithSequence(13, 4, 6));

    // Read in n.
    int n;
    scanf("%d", &n);

    // Test for #3
    UCFStudent** arrTmp = readStudentData(n);
    for (int i=0; i<n; i++)
        printStudent(arrTmp[i]);
    for (int i=0; i<n; i++) {
        free(arrTmp[i]->first);
        free(arrTmp[i]->last);
        free(arrTmp[i]);
    }
    free(arrTmp);

    // Test for #5 - put some values in an array, print it/
    int* vals = calloc(20, sizeof(int));
    for (int i=0; i<20; i++)
        vals[i] = (3*i+7)%20;
    print(vals, 20);

    // Reverse, print and free.
    int* other = reverseCopy(vals, 20);
    print(other, 20);
    free(vals);
    free(other);

    return 0;
}

// Just for test.
void printStudent(UCFStudent* ptr) {
    printf("%s %s %d\n", ptr->first, ptr->last, ptr->UCFID);
}

// Same...
void print(int* arr, int n) {
    for (int i=0; i<n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// Code for #5
int* reverseCopy(int* numbers, int n) {

    // Allocate spac.
    int* res = calloc(n, sizeof(int));

    // Copy in like this. Many ways to do this.
    for (int i=0; i<n; i++)
        res[i] = numbers[n-1-i];

    // Ta da!
    return res;
}

// Code for #3
UCFStudent** readStudentData(int n) {

    // First allocate space for the array.
    UCFStudent** res = calloc(n, sizeof(UCFStudent*));

    // Read through the students.
    for (int i=0; i<n; i++) {

        // We need space for this student.
        res[i] = malloc(sizeof(UCFStudent));

        // Make sure these are 51 or bigger.
        char readF[MAXLEN+1], readL[MAXLEN+1];

        // Read everything in.
        scanf("%s%s%d", readF, readL, &( res[i]->UCFID));

        // Allocate the amount of necessary space for this string.
        res[i]->first = calloc(strlen(readF)+1, sizeof(char));

        // Copy it in.
        strcpy(res[i]->first, readF);

        // Do the same for last name.
        res[i]->last = calloc(strlen(readL)+1, sizeof(char));
        strcpy(res[i]->last, readL);
    }

    // Here's the result.
    return res;
}

// Pre-condition: nTerms >= 0.
int sumArithSequence(int firstTerm, int diff, int nTerms) {

    // Nothing to add.
    if(nTerms == 0) return 0;

    // Add the first term to the rest of the numbers which are
    // an arithmetic sequence starting at firstTerm+diff, with
    // the same difference and 1 fewer term.
    return firstTerm + sumArithSequence(firstTerm+diff, diff, nTerms-1);

}

