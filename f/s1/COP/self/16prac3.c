#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int col, row;

    printf("Enter the amount of columns and rows: ");
    scanf("%d%d", &col, &row);

    char *arr = malloc(row * (col * sizeof(char)));

    for (int i = 0; i < row+2; i++) {
        printf("#");
    }
    printf("\n");

    for (int i = 0; i < row; i++) {
        printf("#");
        for (int j = 0; j < col; j++) {
            *(arr + (i*col) + j) = '*'; 
            printf("%c", *(arr + (i*col) + j));
        } 
        printf("#");
        printf("\n");
    }

    for (int i = 0; i < row+2; i++) {
        printf("#");
    }
    printf("\n");

    return 0;
}
