#include <stdio.h>

void print_array(int arr[], int size);
int compress_array(int arr[], int size);
int shift_array(int arr[], int size, int index);


int main(void) {
    int runs;
    scanf("%d", &runs);
    
    for (int i = 0; i < runs; i++) {
        int size = 0;
        int arr[0];
        int *arrAddr = arr;
        int num = 1;
        
        while (num != 0) {
            scanf("%d", &num);
            if (num == 0) {
                break;
            }

            size++;
            int arrTmp[size];
            for (int i = 0; i < size; i++) {
                arrTmp[i] = 0;
            } 
            for (int i = 0; i < size-1; i++) {
                arrTmp[i] = arrAddr[i];
            } 
            arrTmp[size-1] = num;
            arrAddr = arrTmp;
        } 

        print_array(arrAddr, size);
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
    if (i < index) {
            arrTmp[i] = arr[i];
        } else {
            arrTmp[i] = arr[i+1];
        }
    }

    return size - 1;
}

