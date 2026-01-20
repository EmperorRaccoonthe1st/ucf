#include <stdio.h>
#include <string.h>

int main(void) {
    FILE *ifile = NULL;
    FILE *rfile = NULL;
    char msg[6];
    msg[6] = '\0';

    ifile = fopen("input.txt", "w");
    if (ifile == NULL) return -1;

    printf("Input 5 sentences to create a secret message\n");

    for (int i = 0; i < 5; i++) {
        char buff[256];
        fgets(buff, 256, stdin);
        fputs(buff, ifile);
    }

    fclose(ifile);
    
    rfile  = fopen("input.txt", "r");
    if (rfile == NULL) return -1;

    for (int i = 0; i < 5; i++) {
        char buff[256];
        fgets(buff, 256, rfile);
        msg[i] = buff[0];
    }

    fclose(rfile);

    printf("Your secret message was is \"%s\"\n", msg);
    return 0;
}
