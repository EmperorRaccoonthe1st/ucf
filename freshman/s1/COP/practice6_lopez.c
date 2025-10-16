#include <stdio.h>

void print_array(int arr[], int size);
int compress_array(int arr[], int size);
int shift_array(int arr[], int size, int index);


int main(void) {
    int runs;
    scanf("%d", &runs);
    
    for (int i = 0; i < runs; i++) {
          
    }
    return 0;
}

void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);
    }
    printf("\n");
}

int compress_array(int arr[], int size) {

}

int shift_array(int arr[], int size, int index) {
   int arrTmp[size-1];

    for (int i = 0; i < size; i++) {
        if (i >= index) {
            arrTmp[i] = arr[i+1];
            continue;
        }
        arrTmp[i] = arr[i];
    }

    return size - 1;
}

