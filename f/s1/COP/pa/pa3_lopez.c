#include <stdio.h>
#define MAX_COUNT 10

/*
    COP3223C Fall 2025
    Programming Assignment 3
    Student Name: Owen Lopez
    File Name: pa3_lopez.c
    NOTE: I hereby certify that this submission is my original work. 
    It was completed independently by me without unauthorized assistance. 
    I affirm that all sources consulted have been properly acknowledged.
    No part of this work was copied or plagiarized from any other source/s.
*/

// Note: DO NOT modify or remove TODO comments as it will interfere 
// with the grading system. You are not allowed to define any
// other helper functions or to modify other parts of the code. You are 
// limited to adding only codes in between the TODO comments.

// Function Prototypes
int compute_secret(int arr[], int size);
int get_mode(int arr[], int size);
int count_unique(int arr[], int size);
int get_min(int arr[], int size);
int get_max(int arr[], int size);
int get_range(int arr[], int size);


int main(void) {
    int T;
    int nums[MAX_COUNT];
    
    // Determine the number of test cases
    scanf("%d", &T);
    
    // For each test case
    for (int i = 1; i <= T; i++) {
        // Read 10 numbers and store them in the array
        for (int j = 0; j < MAX_COUNT; j++) {
            scanf("%d", &nums[j]);
        }

        // Print the secret code for the test case
        printf("%d: %d\n", i, compute_secret(nums, MAX_COUNT));
    }
    
    return 0;
}


// Function Definitions
int compute_secret(int arr[], int size) {
    // Compute the secret code based on the statistics
    return get_mode(arr, size) + count_unique(arr, size) + 
        get_min(arr, size) + get_max(arr, size) + get_range(arr, size);
}

int get_mode(int arr[], int size) {
    // TODO 1 BEGIN
    int tmp[MAX_COUNT];
    int hPos = 0;
    int hNum = 0;
    
    for (int i = 0; i < MAX_COUNT; i++) {
        int count = 1;
        for (int j = (i == 9) ? 0 : i+1; j != i;) {
            if (arr[i] == arr[j]) count++;
            if (j == 9) {
                j = 0;
            } else {
                j++;
            }
        }
        tmp[i] = count;
    } 
    
    for (int i = 0; i < MAX_COUNT; i++) {
        if (tmp[i] > hNum) {
            hNum = tmp[i];
            hPos = i;
        } 
    } 
    return arr[hPos];

    // TODO 1 END
}

int count_unique(int arr[], int size) {
    // TODO 2 BEGIN

    int tmp[MAX_COUNT];
    int count = 0;
    for (int i = 0; i < MAX_COUNT; i++) {
        tmp[i] = 0;
	}

    for (int i = 0; i < MAX_COUNT; i++) {
        for (int j = 0; j <= MAX_COUNT; j++) {
            if (j == MAX_COUNT) {
                count++; 
                for (int k = 0; k < MAX_COUNT; k++) {
                    if (tmp[k] == 0) {
                        tmp[k] = arr[i];     
                        break;
                    }
                }  
                break;
            }
            if (arr[i] == tmp[j]) break;
        } 
    }
    return count;
    
    // TODO 2 END
}

int get_min(int arr[], int size) {
    // TODO 3 BEGIN

    int hNum = arr[0];    
    
    for (int i = 0; i < MAX_COUNT; i++) {
        if (arr[i] < hNum) hNum = arr[i];
    }
    return hNum;

    // TODO 3 END
}

int get_max(int arr[], int size) {
    // TODO 4 BEGIN

    int hNum = arr[0];    
    
    for (int i = 0; i < MAX_COUNT; i++) {
        if (arr[i] > hNum) hNum = arr[i];
    }
    return hNum;

    // TODO 4 END
}

int get_range(int arr[], int size) {
    // TODO 5 BEGIN
    
    return  get_max(arr, MAX_COUNT)-get_min(arr, MAX_COUNT);

    // TODO 5 END
}

