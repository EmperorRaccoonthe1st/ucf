#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 101

void destroy_list(char **words, int size);
void process_list(char **words, int size);
int has_reverse(char **words, int size, int pos);
int is_reverse(const char *w1, const char *w2);


int main(void) {
    FILE *ifile = fopen("words.txt", "r");
    
    if (!ifile) {
        printf("Cannot open file!\n");
        return 1;
    }

    int N;
    fscanf(ifile, "%d", &N);

    char **words = malloc( sizeof(char *) * N ); 
    if (!words) {
        printf("Cannot allocate memory!\n");
        fclose(ifile);

        return 1;
    }

    char buffer[BUFFER_SIZE];

    for (int i = 0; i < N; i++) {
        fscanf(ifile, "%100s", buffer); 

        words[i] = malloc( sizeof(char) * (strlen(buffer) + 1));

        strcpy(words[i], buffer);
    }

    fclose(ifile);

    process_list(words, N);

    destroy_list(words, N);

    return 0;
}


void destroy_list(char **words, int size) {

    if (!words) return;

    for (int i = 0; i < size; i++) {
        free(words[i]);
    }
    
    free(words);
}


void process_list(char **words, int size) {
    for (int i = 0; i < size; i++) {
        printf("%s\n", (has_reverse(words, size, i) ) ? "Yes" : "No");
    }
}


int has_reverse(char **words, int size, int pos) {
    for (int i = 0; i < size; i++) {
        if (i == pos) continue;

        if (is_reverse(words[pos], words[i]) ) return 1;
    }

    return 0;
}


int is_reverse(const char *w1, const char *w2) {
    int len1 = strlen(w1);
    int len2 = strlen(w2);

    if (len1 != len2) return 0;

    for (int i = 0; i < len1; i++) {
        if (w1[i] != w2[len1 - 1 - i]) return 0;
    }

    return 1;
}
