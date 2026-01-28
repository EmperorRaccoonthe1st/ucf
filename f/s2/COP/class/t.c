#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    FILE *ifile = NULL;
    
    ifile = fopen("t.txt", "r");
    if (ifile == NULL) return 1;

    printf("File opened!\n");

    int arr[10000];
    int i = 0;

    while (1) {
        if (fscanf(ifile, "%d", &arr[i]) == -1) break;
        i++;
    }

    for (int i = 2; i < 10000; i++) {
        int key = arr[i];
        int j = i-1;

        while (j > 0 && arr[i] > key) {
            arr[j+1] = arr[j];
            j--;
            arr[j+1] = key;
        }
    }

    for (int i = 0; i < 10000; i++) {
        printf("%d\n", arr[i]);
    }

    return 0;
}
