#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE "arr.txt"
#define MAX_LEN 256

int isMinHeap(int *arr, int size, int capacity);

int main() {
    // FIX: fopen requires a string literal or variable, and the result must be assigned to the pointer.
    FILE *ifile = fopen(INPUT_FILE, "r");
    if (ifile == NULL) {
        printf("Error: Could not open file %s\n", INPUT_FILE);
        return -1;
    }

    // FIX: parentBuff is an array of pointers, sizes should be an array of ints (not pointers).
    int *parentBuff[MAX_LEN];
    int sizes[MAX_LEN];
    int psize = 0;

    // FIX: Simplified the logic to read arrays ending with -1
    while (psize < MAX_LEN) {
        int buff[MAX_LEN];
        int currentSize = 0;
        int tmp;

        // Read numbers until we hit -1 or the end of the file
        while (fscanf(ifile, "%d", &tmp) == 1 && tmp != -1) {
            buff[currentSize++] = tmp;
        }

        // If we didn't read anything and it's EOF, we are done
        if (currentSize == 0 && feof(ifile)) break;

        // Allocate memory for the specific array found
        int *arr = malloc(currentSize * sizeof(int));
        for (int y = 0; y < currentSize; y++) {
            arr[y] = buff[y];
        } 
        
        parentBuff[psize] = arr;
        sizes[psize] = currentSize;
        psize++;

        if (feof(ifile)) break;
    }

    // FIX: Removed redundant double pointer allocation. We use parentBuff directly.
    for (int i = 0; i < psize; i++) {
        int val = isMinHeap(parentBuff[i], sizes[i], sizes[i]);
        printf("Array %d (Size %d): %s\n", i, sizes[i], val ? "Min-Heap" : "Not Min-Heap");
        printf("\n"); 
    }
        
    printf("EOF\n");
     
    // Cleanup memory
    for (int i = 0; i < psize; i++) {
        free(parentBuff[i]);
    }
    
    fclose(ifile);
    return 0;
}


int isMinHeap(int *arr, int size, int capacity) {
    int val = 1;

    for (int i = 0; i < size; i++) {
        int lChild = 2*i + 1;
        int rChild = 2*i + 2;

        if (lChild < size && arr[lChild] < arr[i]) val = 0;
        if (lChild < size) printf("Parent: %d -> lChild: %d | ", i, lChild);

        if (rChild < size && arr[rChild] < arr[i]) val = 0;
        if (rChild < size) printf("Parent: %d -> rChild: %d \n", i, rChild);
    }

    
    return val;
}
