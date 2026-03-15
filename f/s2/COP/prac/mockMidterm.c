This document is the written portion of a practice comp sci 1 midterm exam.
The following sections are responses to free response questions that require code to be written.


# Part A Question 1 Part B
```c

int main(void) {

// rewriting scores = realloc(etc..)

    int *tmp = realloc(scores, n * 2 * sizeof(int));

    if (tmp == NULL) {
        free(scores);
        printf("failed\n");
    } else {
        scores = tmp;
        printf("success\n");
    }

    return 0;
}

```


# Part A Question 2 Part A
```c

Book *createBook(char *title, char authNames[][50], float price, int n) {
    Book *b = malloc(sizeof(Book));    

    char buff[50];
    b->title = buff;
    strcpy(b->title, title);
    

    char **names = malloc(n * sizeof(char *)):
    for (int i = 0; i < n; i++) {
        names[i] = malloc(50 * sizeof(char));
        strcpy(names[i], authNames[i]);
    }

    b->price = price;
    b->nAuth = n;
}

```


# Part A Question 2 Part B
```c

void freeBook(Book *book) {
    for (int i = 0; i < book->nAuth; i++) {
        free(book->authNames[i]);
    }

    free(book->authNames);

    free(book);
}

```


# Part B Question 2
```c

void byeList(node *head) {
    
    if (head->next = NULL) {
        free(head);
        return;
    }

    byeList(head->next);
    free(head);
    
    return;
}

```


# Part B Question 3
```c

#include <stdio.h>
#include <stdlib.h> //in case you want to use abs function for absolute value
#define SIZE 10

void makePerm(int* perm, int* used, int k, int n);
void print(int* perm, int n);
int check(int* perm, int n);

int main() {
    int perm[SIZE];
    int used[SIZE];
    for (int i=0; i<SIZE; i++)
        used[i] = 0;
    makePerm(perm, used, 0, SIZE);
    return 0;
}

void makePerm(int* perm, int* used, int k, int n) {
    if (k == n) {
        if (check(perm,n))
            print(perm, n);
        return;
    }
    /*** FILL IN FOR LOOP ***/
    for (int i=0; i<n; i++) {

        for (int j = 0; j < n; j++) {
            if (used[j] == 0) perm[k] = j;
            used[j] = 1;
        }

        makePerm(perm, used, k+1, n);
    
        used[k] = 0;
    }
}

void print(int* perm, int n) {
    for (int i=0; i<n; i++)
        printf("%d ", perm[i]);
    printf("\n");
}

// This function should be written iteratively.
int check(int* perm, int n) {

    if (abs((perm[0] - perm[1])) == 1) return 1;
    if (abs((perm[n-1] - perm[n-2])) == 1) return 1;

    for (int i = 1; i < n-1; i++) {
        if (abs((perm[i] - perm[i+1])) == 1) return 1;
        if (abs((perm[i] - perm[i-1])) == 1) return 1;
    }
    
    return 0;
}

```


# Part C Question 1

## Clarification
    In the exam source the struct "node" is uncapitlized. I chose to write following repsonse with a captilized "Node" as the node struct.
    This is a specific choice on my part as I beleive the exam has a small typo with the uncharacteristically uncapitilized first letter of the struct.

```c

int insertAt(Node* head, int x, int p) {

    int size = 0;
    
    Node *tail = head;
    while (tail->next != NULL) {
        size++;
        tail = tail->next;
    }

    If (p > amt) {
        Node n;
        n.data = x;
        n.next = NULL;

        tail->next = &n;
        return amt+1;
    }

    Node *prev = head;
    for (int i = 0; i < p-2; i++) {
        prev = prev->next; 
    }

    Node n;
    n.data = x;

    n.next = prev->next;
    prev->next = n;

    return amt+1;
}

```


# Part D Question 4
```c

int dequeue(struct queue* qPtr) {

    if (qPtr->noe = 0) return -1;

    int val = qPtr->front;
    
    qPtr->noe--;

    if (qPtr->noe > 1) {
        qPrt->front = qPrt->elements[0];
        for (int i = 0; i < noe; i++) {
           if (i != qPrt->queueSize-1) qPrt->elements[i] = qPrt->elements[i+1];
        }
    } else if (qPtr->noe == 1) {
        qPrt->front = qPrt->elements[0];
    }

    return val;
}

```
