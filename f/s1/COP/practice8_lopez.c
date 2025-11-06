#include <stdio.h>
#define MAX_SIZE 256

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s);

int main(void) {
    char canvas[MAX_SIZE][MAX_SIZE];
    FILE *ifile = NULL;
    int R, C, x, y;
    char S;
    
    ifile = fopen("data.txt", "r");
    if (ifile == NULL) return -1; 

    fscanf(ifile, "%d%d", &R, &C); 
    reset_art(canvas, R, C);

    while (fscanf(ifile, "%d %d %c", &y, &x, &S) != EOF) {
        printf("%d, %d: %c\n", y, x, S);
        draw_art(canvas, R, C, x, y, S); 
    }

    print_art(canvas, R, C);

    fclose(ifile);
    
    return 0;
}

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int i = 0; i < R+2; i++) {
        for (int j = 0; j < C+3; j++) {
            canvas[i][j] = ' ';
            if (i == 0 || i == R+1) canvas[i][j] = '*';
            if (j == 0 || j == C+1) canvas[i][j] = '*';
            if (j == C+2) canvas[i][j] = '\n';
        }
    }
}

void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int i = 0; i < R+2; i++) {
        for (int j = 0; j < C+3; j++) {
            printf("%c", canvas[i][j]);
        }
    }
    printf("\n");
}


void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s) {
    for (int i = 0; i < R+1; i++) {
        for (int j = 0; j < C+1; j++) {
            if (i == y && j == x) canvas[i][j] = s;
        }
    }
}
