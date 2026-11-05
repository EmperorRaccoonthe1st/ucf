#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define LETTER_COUNT 26
#define MAX_CODE_SIZE 5
#define MAX_WORD_SIZE 101

int get_idx(char letter);
void print_morse(const char *str);


int main(void) {
    FILE  *ifile = fopen("words.txt", "r");    

    if (!ifile) {
        printf("Cannot open file!\n");
        return 1;
    }

    int N;
    char word[MAX_WORD_SIZE];

    fscanf(ifile, "%d", &N);

    for (int i = 0; i < N; i++) {
        fscanf(ifile, "%100s", word);

        print_morse(word);
    } 

    fclose(ifile);

    return 0;
}


int get_idx(char letter) {
    return toupper(letter) - 'A';
}


void print_morse(const char *str) {

    const char codes[LETTER_COUNT][MAX_CODE_SIZE] = {
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
        "....", "..", ".---", "-.-", ".-..", "--", "-.",
        "---", ".--.", "--.-", ".-.", "...", "-", "..-",
        "...-", ".--", "-..-", "-.--", "--.."
    };

    int len = strlen(str); 

    for (int i = 0; i < len; i++) {
       printf("%s ", codes[get_idx(str[i])]); 
    }

    printf("\n");
}
