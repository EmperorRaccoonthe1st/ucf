#include <math.h>
#include <stdio.h>

int get_reverse(int num);
int is_palindrome(int num);

int main(void) {
    int loop;
    scanf("%d", &loop);
    for (int i = 0; i < loop; i++) {
        int input;
        scanf("%d", &input);
        printf("%d: %d %d %d\n", i+1, input, get_reverse(input), is_palindrome(input));
    }
    return 0;
}

int get_reverse(int n) {
    int nf = 0;
    while (n > 0) {
        int count = 0;
        int num = n;
        while (num > 10) {
           count++;
           num /= 10;
        }
        nf += (n % 10)*(pow(10, count));
        n = (n - (n % 10))/10;
    } 
    return nf;
}

int is_palindrome(int num) {
    if (num == get_reverse(num)) {
        return 0;
    } else {
        return 1;
    }
}
