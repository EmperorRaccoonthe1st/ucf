#include <stdio.h>

#define GRID_SIZE 3

int get_magic_constant(int n);
int is_magic_square(int grid[GRID_SIZE][GRID_SIZE], int size, int target);
int validate_rows(int grid[GRID_SIZE][GRID_SIZE], int size, int target);
int validate_cols(int grid[GRID_SIZE][GRID_SIZE], int size, int target);
int validate_diag1(int grid[GRID_SIZE][GRID_SIZE], int size, int target);
int validate_diag2(int grid[GRID_SIZE][GRID_SIZE], int size, int target);

int main(void) {
    int grid[GRID_SIZE][GRID_SIZE];
    int t;
    
    scanf("%d", &t);

    for (int k = 0; k < t; k++) { 
        for (int i = 0; i < GRID_SIZE; i++) {
            for (int j = 0; j < GRID_SIZE; j++) {
                scanf("%d", &grid[i][j]); 
            }    
        }
    
        if (is_magic_square(grid, GRID_SIZE, get_magic_constant(GRID_SIZE)) == 1) {
            printf("%d: Magic\n", k);
        } else {
            printf("%d: Not Magic\n", k);
        }
    }
    return 0;
}


int get_magic_constant(int n) {
    return (n) * (((n*n) + 1)/2);
}

int is_magic_square(int grid[GRID_SIZE][GRID_SIZE], int size, int target) {
    if (validate_rows(grid, size, target) == 0) return 0;
    if (validate_cols(grid, size, target) == 0) return 0;
    if (validate_diag1(grid, size, target) == 0) return 0;
    if (validate_diag2(grid, size, target) == 0) return 0;
    return 1; 
}

int validate_rows(int grid[GRID_SIZE][GRID_SIZE], int size, int target) {
    for (int i = 0; i < GRID_SIZE; i++) {
        int sum = 0;
        for (int j = 0; j < GRID_SIZE; j++) {
           sum += grid[i][j]; 
        }
        if (sum != target) return 0;
    }
    return 1;
}

int validate_cols(int grid[GRID_SIZE][GRID_SIZE], int size, int target) {
    for (int i = 0; i < GRID_SIZE; i++) {
        int sum = 0;
        for (int j = 0; j < GRID_SIZE; j++) {
           sum += grid[j][i]; 
        }
        if (sum != target) return 0;
    }
    return 1;
}

int validate_diag1(int grid[GRID_SIZE][GRID_SIZE], int size, int target) {
    int sum = 0;
    for (int i = 0; i < GRID_SIZE; i++) {
        sum += grid[i][i];
    }

    if (sum == target) {
        return 1;
    } else {
        return 0;
    }
}

int validate_diag2(int grid[GRID_SIZE][GRID_SIZE], int size, int target) {
    int sum = 0;
    for (int i = GRID_SIZE-1; i >= 0; i--) {
        sum += grid[i][i];
    }

    if (sum == target) {
        return 1;
    } else {
        return 0;
    }
}
