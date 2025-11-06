#include <stdio.h>
#define MAX_SIZE 256

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s);

int main(void) {
    char canvas[MAX_SIZE][MAX_SIZE];
    FILE *ifile = NULL;
    int R;
    int C;
    
    ifile = fopen("input.txt", "r");
    if (ifile == NULL) return -1; 

    fscanf(ifile, "%d%d", &R, &C); 
    reset_art(canvas, R, C);
    print_art(canvas, R, C);
    
    return 0;
}

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int x = 0; x <= C+2; x++) {
        for (int y = 0; y < R; y++) {
            canvas[x][y] = ' ';
            if (y == 0) canvas[x][y] = '*';
            if (y == R+1) canvas[x][y] = '*';
            if (x == 0) canvas[x][y] = '*';
            if (x == C+1) canvas[x][y] = '*';
            if (x == C+2) canvas[x][y] = '\n';
        }
    }
}

void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int x = 0; x <= C+2; x++) {
        for (int y = 0; y < R; y++) {
            printf("%c", canvas[x][y]);
        }
    }
}


void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s) {

}
