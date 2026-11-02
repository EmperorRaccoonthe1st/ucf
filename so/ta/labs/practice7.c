#include <stdio.h>
#define MAX_SIZE 52

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C);
void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s);


int main(void) {
    char grid[MAX_SIZE][MAX_SIZE];
    FILE *ifile = NULL;

    ifile = fopen("data.txt", "r");

    if (!ifile) {
        printf("Error opening file!\n");
        return -1;
    }

    int row, col;
    fscanf(ifile, "%d%d", &row, &col);

    int actual_row = row + 2;
    int actual_col = col + 2;

    reset_art(grid, actual_row, actual_col);
    print_art(grid, actual_row, actual_col);

    int x, y;
    char s;

    while (fscanf(ifile, "%d%d %c", &x, &y, &s) != EOF) {
        draw_art(grid, actual_row, actual_col, x, y, s);
    }

    fclose(ifile);

    print_art(grid, actual_row, actual_col);
    
}

void reset_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            if (i == 0 || i == R-1) {
                canvas[i][j] = '*';
            } else if (j == 0 || j == C-1) {
                canvas[i][j] = '*';
            } else {
                canvas[i][j] = ' ';
            }
        }
    }
}


void print_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C) {
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            printf("%c", canvas[i][j]); 
        }
        printf("\n");
    }
}


void draw_art(char canvas[MAX_SIZE][MAX_SIZE], int R, int C, int x, int y, char s) {
    canvas[x][y] = s;
}
