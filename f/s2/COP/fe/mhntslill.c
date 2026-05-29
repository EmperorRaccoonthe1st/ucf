typedef struct node_s {
    int data;
    struct node_s* next;
} node_t;

node_t * moveHeadNearTail(node_t * head) {
    
    // WRITE YOUR CODE HERE
<<<<<<< HEAD

    node_t *cur = head;    
    while (cur->next->next != NULL) {
        cur = cur->next;
    }

    node_t nHead = head->next;

    head->next = cur->next;
    cur->next = head;

    return nHead;
=======
    
>>>>>>> 8fa313e (some pracitce)
}
