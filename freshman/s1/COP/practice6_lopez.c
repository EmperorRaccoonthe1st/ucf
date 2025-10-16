#include <stdio.h>
void print_array(int arr[], int size);
int compress_array(int arr[], int size);
int shift_array(int arr[], int size, int index);


int main(void) {
    int runs;
    scanf("%d", &runs);
    
    for (int i = 0; i < runs; i++) {
        int arr[10];
        int size = 0;

        for (int i = 0; i < 10; i++) {
            arr[i] = 0; 
        }

        for (int i = 0; i < 11; i++, size++) {
            int num = 1;
            scanf("%d", &num);
            if (num == 0) break;
            arr[i] = num;
        }
        size = compress_array(arr, size);
        printf("%d: ", i+1);
        print_array(arr, size);
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
    for (int j = 0; j < size; j++) {
        for (int i = 0; i < size; i++) {
            if (arr[i] == arr[i+1]) {
                size = shift_array(arr, size, i);
            }
        }
    }
    return size;
}

int shift_array(int arr[], int size, int index) {
    for (int i = index; i < size; i++) {
        arr[i] = arr[i+1];
    }
    return size-1;
}

