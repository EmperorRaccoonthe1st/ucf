#include <stdio.h>
#include <stdlib.h>

int main(void) {
    FILE *ifile = NULL;
    int n;
    
    ifile = fopen("file.txt", "r");    
    if (ifile == NULL) return -1;

    fscanf(ifile, "%d", &n);

    int *arr = malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        fscanf(ifile, "%d", &arr[i]);
    }

    for (int i = 0; i < n; i++) {
        int low = i;
        int tmp;
        
        for (int j = i+1; j < n; j++) {
            if (arr[j] < arr[low]) low = j;
        }
        
        tmp = arr[i];
	    arr[i] = arr[low];
        arr[low] = tmp;
    }

    for (int i = 0; i < n; i++) {
        printf("%d\n", arr[i]);
    }

    free(arr);
    fclose(ifile);

    return 0;
}
