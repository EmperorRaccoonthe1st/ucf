#include <stdio.h>

int get_reverse(int num);
int is_palindrome(int num);

int main(void) {
    int input;
    printf("Input a number here:");
    scanf("%d", &input);
    get_reverse(input);
    return 0;
}

int get_reverse(int num) {
    int r;
    while ((num/10) > 0) {
        r += (num % (num/10))*(num/10);
        printf("%d\n", r);
        num = num/10;
    }
    return r;
}
