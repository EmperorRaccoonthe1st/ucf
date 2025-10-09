#include <stdio.h>
#define SIZE 5

int main(void) {
    int nums[SIZE];
    int sum = 0;
    int l = 0;

    printf("Input %d numbers: ", SIZE);
    for (int i = 0; i < SIZE; i++) {
        scanf("%d", &nums[i]);
    }

    printf("This is the array: ");
    for (int i = 0;i < SIZE; i++) {
        printf("%d ", nums[i]);
    };

    printf("\nThis is the array backwards: ");
    for (int i = SIZE - 1; i > -1; i--) {
        printf("%d ", nums[i]);
    };
    
    for (int i = 0; i < SIZE; i++) {
       sum += nums[i]; 
    }
    printf("\nThe total sum of all numbers: %d\n", sum);

    printf("The average of the values is %.2lf\n", (float)sum/SIZE);
    
    printf("Input a value to query: ");
    scanf("%d", &sum);
    for (int i = 0; i < SIZE; i++) {
        if (nums[i] == sum) {
            printf("Found\n");
            break;
        }
        if (i == SIZE-1) {
           printf("Not Found\n");
        }
     }

    for (int i = 0; i < SIZE; i++) {
        if (sum > nums[i]) {
            sum = nums[i];
        } 
        
        if (l < nums[i]) {
            l = nums[i];
        } 
    }
    printf("The highest = %d and the lowest = %d\n", sum, l);

    return 0;
}
