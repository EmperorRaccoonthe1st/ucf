struct node {
    int data;
    struct node* next;
};

int check_all_even(struct node *head) {
    
    // WRITE YOUR CODE HERE

    if (head == NULL) return 0;

    if (head->next == NULL) {
        if (head->data % 2 == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    if (head->data % 2 == 0) {
        return check_all_even(head->next);
    } else {
        return 0;
    }
}
