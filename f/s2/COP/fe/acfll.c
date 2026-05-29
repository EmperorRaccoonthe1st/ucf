typedef struct node {
    char letter;
    struct node* next;
} node;

void printMixed(node* word1, node* word2) {
    
    // WRITE YOUR CODE HERE
    if (word1 == NULL && word2 == NULL) return;

    node *w1 = word1;
    node *w2 = word2;
    while (w1 != NULL || w2 != NULL) {
        if (w1 != NULL) printf("%c", w1->letter);
        if (w2 != NULL) printf("%c", w2->letter);

        if (w1 != NULL) w1 = w1->next;
        if (w2 != NULL) w2 = w2->next;
    }
}
