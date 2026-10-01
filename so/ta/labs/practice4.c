#include <stdio.h>
#include <ctype.h>

int main(void) {
    int T;
    int pos;
    char letter;

    scanf("%d", &T);

    int i = 1;
    while (i <= T) {
        scanf(" %c", &letter);

        printf("%d: ", i);

        if (isalpha(letter)) {

            pos = 'Z' - toupper(letter) + 1;

            printf("%d", pos);

        } else {
            printf("Invalid");
        }

        printf("\n");

        i++;
    }

    return 0;
}
