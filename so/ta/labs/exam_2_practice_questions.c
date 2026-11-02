#include <stdio.h>

int main(void) {

    int arr[7] = {1, 2, 3, 0, 4, 0, 5};
    int size = 7;

    int pos = 0;
   int i = 0;
    while (i < size) {
        if (arr[pos] == 0) {
            size--; 
        } else {
            arr[i] = arr[pos];
            i++;
        }

        pos++;
    }

    printf("#\n");

    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    } 

    printf("Size: %d", size);

    printf("\n");
    
    return 0;
}
