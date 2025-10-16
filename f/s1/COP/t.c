#include <stdio.h>

int main(void) {
    int num;
    int count;
    printf("Input a number here:");
    scanf("%d", &num);
    while (num > 0) {
       count++;
       num = num/10;
    }
    printf("Your number had %d digits.\n", count);
    return 0;
}
