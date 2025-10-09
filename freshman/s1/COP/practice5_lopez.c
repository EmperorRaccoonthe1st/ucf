#include <stdio.h>
#include <math.h>

void populate_array(int arr[], int size, int num);
void print_array(int arr[], int size);
int get_next_pos(int cur_pos, int size, int shift);
void left_shift_array(int arr[], int size, int shift);

int main(void) {
    int amt;
    scanf("%d", &amt);
    for (int i = 0; i < amt; i++) {
        int num;
        int shift;
        int count = 0;
    
        // Get current number
        scanf("%d%d", &num, &shift);
        int n = num;
        // Find the amount of digits
        while (n > 0) {
            count++;
            n /= 10;
        }

        int numA[count];
        populate_array(numA, count, num);  
        print_array(numA, count);
        left_shift_array(numA, count, shift);

        printf("%d: ", i+1);
        print_array(numA, count);
    }
    return 0;
}

void populate_array(int arr[], int size, int num) {
    for (int i = 0; i < size; i++) {
        int d;
        int cSize = 0;
        int cNum = num;
        while (cNum > 10) {
            cSize++;
            cNum /= 10;
        }
        int powN = (int)(pow(10, cSize));
        d = (num)/((int)pow(10, cSize));
        num = (num)%(int)(pow(10, cSize));

        arr[i] = d;
    }    
}


void print_array(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d", arr[i]);   
    }
    printf("\n");
}


//int get_next_pos(int cur_pos, int size, int shift) {
//    
//}


void left_shift_array(int arr[], int size, int shift) {
    for (int i = 0; i < shift; i++) {
        int numB[size];
        for (int x = 0; x < size; x++) {
            numB[x] = arr[x];
        } 
        for (int x = 0; x < size; x++){
           if (x < size-1) {
                arr[x] = numB[x+1]; 
           } else {
                arr[x] = numB[0];
           } 
        }
    }
}

