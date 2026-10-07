#include <stdio.h>
#include <math.h>

int get_reverse(int num);
int is_palindrome(int num);

int main(void) {
    int T, num;
    scanf("%d", &T);

    for (int i = 1; i <= T; i++ ){
        scanf("%d", &num);
        printf("%d: %d %d %d\n", i, num, get_reverse(num), is_palindrome(num));
    }

    T = i;

    return 0;
}


int get_reverse(int num) {
    int rev = 0;    
    int digit;

    while ( num > 0) {
        digit = num % 10;

        rev = (rev * 10) + digit;

        num = num / 10;
    }
    
    return rev;
}


int is_palindrome(int num) {

    int rev = get_reverse(num);

    return num == rev;
}
