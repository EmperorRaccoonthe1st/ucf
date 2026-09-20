#include <stdio.h>
#include <math.h>

int main(void) {

// In case you're having any issues compiling:
// gcc practice2.c -o practice2 -lm
// That '-lm' flag is important for this lab.

    int num, tmp, rem, sum;
    int acc = 0;
    double res; 

    printf("Enter Number: ");
    scanf("%d", &num);
    
    tmp = num; // 123
    
    rem = tmp % 10; // 3
    tmp = tmp / 10; // 012 
    acc = (acc * 10) + rem;
    /// 000 + 3

    rem = tmp % 10; // 2
    tmp = tmp / 10; // 001
    acc = (acc * 10) + rem;
    /// 030 + 2

    rem = tmp % 10; // 1
    tmp = tmp / 10; // 001
    acc = (acc * 10) + rem;
    /// 320 + 1

    printf("Reversed: %d\n", acc);

    // Our Calculations
    sum = acc + num;
    printf("Sum: %d\n", sum);

    res = sqrt(sum);
    printf("Square Root: %.2lf\n", res);

    
    char alpha = 'A'; // 65
    
    char ch3 = (char)(acc / 1 % 10) + alpha; 
    char ch2 = (char)(acc / 10 % 10) + alpha; 
    char ch1 = (char)(acc / 100 % 10) + alpha; 

    printf("Hidden Code: %c%c%c\n", ch1, ch2, ch3);

    return 0;
}
