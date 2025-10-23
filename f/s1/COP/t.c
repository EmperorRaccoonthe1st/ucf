#include <stdio.h>

void swap(int *a, int *b);

int main(void) {
    int a, b;
    printf("Input two numbers: ");
    scanf("%d%d", &a, &b);
    swap(&a, &b);
    printf("a swapped is %d\n", a);
    printf("b swapped is %d\n", b);
        
    return 0;
}

void swap(int *a, int *b) {
    int tmp;

    tmp = *a;
    *a = *b;
    *b = tmp;
}
