struct node {
    int num;
    struct node* next;
};

struct node* make_circle(struct node* head) {
    
    // WRITE YOUR CODE HERE
    
    node *cur = head;    
    while (cur->next != NULL) {
        cur = cur->next;
    }

    cur->next = head; 

    return head;
}
