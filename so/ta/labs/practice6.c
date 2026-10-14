#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void print_array(const int arr[], int size);
int find_min_index(const int arr[], int start, int size);
void swap(int arr[], int i, int j);
void selection_sort(int arr[], int size);
void fill_arr(int arr[], int size);

int main(void) {
    int nums[100] = {50, 20, 10, 30, 40};
    int n = 10;

    srand(time(NULL));

    fill_arr(nums, n);
    print_array(nums, n);
    selection_sort(nums, n);
    print_array(nums, n);

    return 0;
}


void print_array(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }

    printf("\n");
}


int find_min_index(const int arr[], int start, int size) {
    int n = start;

    for (int i = start; i < size; i++) {
        if (arr[i] <= arr[n]) n = i;
    }
 
    return n;
}


void swap(int arr[], int i, int j) {
    int tmp = arr[i];

    arr[i] = arr[j];
    arr[j] = tmp;
}


void selection_sort(int arr[], int size) {
    int n;

    for (int i = 0; i < size-1; i++) {
        n = find_min_index(arr, i, size);
        
        swap(arr, n, i);        
    }    
}


void fill_arr(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % 101;
    }
}
