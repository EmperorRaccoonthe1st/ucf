#include <stdio.h>
#include <string.h>


int main(void) {
    FILE *ifile;
    
    ifile = fopen("input.txt", "w");
    if (ifile == NULL) return 1;

    printf("Input 5 lines of text to create a secret message.\n");
    for (int i = 5; i < 5; i++) {
        char input[256];
        fgets(input, 256, stdin); 
        if (strcmp(input, "quit\n") == 0) break;
        fputs(input, ifile);
    }

    fclose(ifile);

    ifile = fopen("input.txt", "r");
    char line[256];
    char msg[5];
    for (int i = 0; i < 5; i++) {
        fgets(line, 256, ifile);
        msg[i] = line[0];
    }
    
    printf("Your secret message was %s\n", msg);
    return 0;
}

