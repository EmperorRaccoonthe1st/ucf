typedef struct node {
    int data;
    struct node* next;
    struct node* prev;
} node;

node* deleteMe(node* head, node* me) {

    // WRITE YOUR CODE HERE
    node *prev = me->prev;
    node *next = me->next;

    prev->next = next;
    next->prev = prev;

    return head;
}
