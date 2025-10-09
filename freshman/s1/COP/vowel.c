#include <stdio.h>
#include <ctype.h>

int main(void) {
    char a, b;
    int count = 0;
    printf("Input two characters:");
    scanf("%c%c", &a, &b);
    a = tolower(a);
    b = tolower(b);

    if (a > b) {
        char t = a;
        a = b;
        b = t;
    }
   
    if (a <= 'a' && b >= 'a') {
        count++;
    }
    if (a <= 'e' && b >= 'e') {
        count++;
    }
    if (a <= 'i' && b >= 'i') {
        count++;
    }
    if (a <= 'o' && b >= 'o') {
        count++;
    }
    if (a <= 'u' && b >= 'u') {
        count++;
    }
    printf("The number of vowels between %c and %c is %d\n", a, b, count);
    return 0; 
}
