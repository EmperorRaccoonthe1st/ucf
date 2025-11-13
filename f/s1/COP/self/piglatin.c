#include <stdio.h>
#include <ctype.h>

int isvowel(char c);

int main(void) {
    char buff[256];
    
    printf("Input a single word: ");
    fgets(buff, 256, stdin);

    for (int i = 0; i < 256; i++) {
        if (buff[i] == '\n') buff[i] = '\0';
    }
    
    if (isvowel(buff[0])) {
        printf("%sway\n", buff);
    } else {
        char w[256];
        for (int i = 0; i < 256; i++) {
            w[i] = buff[i+1];
        }
        printf("%s%cay\n", w, tolower(buff[0]));
    }
      
    return 0;
}

int isvowel(char c) {
    c = tolower(c);
    if (c == 'a') return 1;
    if (c == 'e') return 1;
    if (c == 'i') return 1;
    if (c == 'o') return 1;
    if (c == 'u') return 1;
    return 0;
}
