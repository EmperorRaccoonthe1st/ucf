typedef struct node {
    int data;
    struct node* next;
} node;

node* addValue3(node* head) {
    if (head == NULL || head->data > 3) {
        node* tmp = malloc(sizeof(node));
        tmp->data = 3;
        tmp->next = head;
        return tmp;
    }

    if (head->data == 3)
        return head;

    node* iter = head;

    while (iter->next != NULL && iter->next->data < 3) {
        iter = iter->next;
    }

    if (iter->next->data == 3 && __________)
        return head;

    node* tmp = malloc(sizeof(node));
    tmp->data = 3;

    tmp->next = iter->next;
    iter->next = tmp;
    
    return head;
}
