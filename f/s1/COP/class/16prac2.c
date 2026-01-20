#include <stdio.h>
#include <stdlib.h>

int* create_array(int len);
void print_array(int *arr, int len);
void destroy_array(int *arr);

int main(void) {
    int n;

    printf("Input a number to create an array\n");
    scanf("%d", &n);

    int *arr = create_array(n);

    for (int i = 0; i < n; i++) {
        arr[i] = i*i;
    }

    print_array(arr, n);

    free(arr);

    return 0;
}

int* create_array(int len) {
    int *arr = malloc(len * sizeof(int));    

    return arr;
}

void print_array(int *arr, int len) {
    for (int i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    
    printf("\n");
}

void destroy_array(int *arr) {
    free(arr);
}
