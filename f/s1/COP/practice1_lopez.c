#include <stdio.h>

int main(void) {
    int one, two;
    printf("Enter the first number: ");
    scanf("%d", &one);
    printf("Enter the second number: ");
    scanf("%d", &two);
    printf("\n");
    
    printf("Sum: %d\n", one+two);
    printf("Difference: %d\n", one-two);
    printf("Product: %d\n", one*two);
    printf("Quotient: %d\n", one/two);
}
    
