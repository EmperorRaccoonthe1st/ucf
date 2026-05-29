typedef struct node {
    int num;
    struct node* next;
} node;

typedef struct stack {
    struct node *top;
    int size;
} stack;

// Returns the value stored at the top of the stack pointed to by s. If stack pointed to by s is empty,
// random value is returned.
int peek(stack *s);

// Returns 1 if the stack pointed to by s is empty, and 0 otherwise.
int isEmpty(stack *s);

void printValidMoves(stack towers[], int numTowers) {
    for (int i = 0; i < numTowers; i++) {
        for (int j = 0; j < numTowers; j++) {
            if (isEmpty(towers[i] == 0 && isEmpty(towers[j]) == 0 && peek(numTowers[i]) > peek(numTowers[j]) continue;
            if (isEmpty(towers[j]) || peek(numTowers[i]) < peek(numTowers[j]))
                printf("Valid move from tower %d to tower %d.\n", i, j);            
        }
    }
}
