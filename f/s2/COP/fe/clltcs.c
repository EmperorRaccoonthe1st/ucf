typedef struct node {
    char letter;
    struct node* next;
} node;

int length(node* head);

char* toCString(node * head) {
    
    // WRITE YOUR CODE HERE
    
    char *str = malloc((length(head) + 1) * sizeof(char));

    str[length] = '\0';

    node *cur = head;
    int i = 0;
    while (cur != NULL) {
        str[i] = cur->letter; 
        cur = cur->next;
        i++;
    }

    return str;
}
