# Phase 1 Extraction: Linked Lists, Stacks & Queues

## 1. Theoretical Core

### Linked Lists
- **Singly Linked List**: A collection of sequential nodes (linear). Each node contains data and a reference (pointer) to the next node. Only the last node does not have a reference to the next node (i.e., `NULL`). The list maintains a reference to the `head` (first node).
- **Doubly Linked List**: Nodes keep track of three fields: `data`, `next`, and `prev`. A node knows both which node comes after it and which node comes before it.
- **Circular Linked List**: Keeping track of the `tail` is sufficient, as accessing the `head` simply requires accessing the `next` field of the `tail`.
- **Array vs. Linked Implementation**: 
  - Arrays store data contiguously and can be dynamically allocated. However, moving elements around (shifting) for insertion or removal in the middle is an expensive operation. Arrays can also waste memory if allocated with a capacity significantly larger than their logical size.
  - Linked lists dynamically allocate memory per node, providing flexibility. They avoid the overhead of shifting elements during insertions and deletions, but they require sequential traversal to access arbitrary elements.

### Queues
- An Abstract Data Type (ADT) representing a collection of items following the **First In, First Out (FIFO)** principle.
- Implementation requires tracking both the `front` (first element to be removed) and the `rear` (last element added).
- **Implementations**:
  - Array implementation (naïve): Suffers from inefficiency due to element shifting.
  - Array implementation (circular): More efficient approach using modulo arithmetic.
  - Linked-list implementation: Naturally supports dynamic sizing and avoids shifting.

### Stacks
- An Abstract Data Type (ADT) representing a collection of elements following the **Last In, First Out (LIFO)** principle.
- Implementation requires tracking only the `topmost` element of the stack.
- **Applications**: Evaluating mathematical expressions (Postfix/Infix notation), tracking function calls (Call Stack), and converting recursive solutions to iterative ones.

## 2. Algorithmic Tracing & Code Implementation

### Linked Lists: Traversal & Generic Deletion
```c
typedef struct SLLNode_s {
    int data;
    struct SLLNode_s *next;
} SLLNode;

typedef struct SLList_s {
    SLLNode *head;
} SLList;

// Traversal pattern
void sll_print_list(SLList *list) {
    SLLNode *ptr = list->head;
    while(ptr != NULL) {
        printf("%d ", ptr->data);
        ptr = ptr->next;
    }
}

// Generic node deletion utilizing a trailing pointer
SLLNode* remove_element(SLList *list, int target) {
    SLLNode *ptr = list->head;
    SLLNode *trail = NULL;
    
    while (ptr != NULL && ptr->data != target) {
        trail = ptr;
        ptr = ptr->next;
    }
    
    if (ptr == NULL) return NULL; // Target not found
    
    if (trail == NULL) {
        list->head = ptr->next;   // Target is at the head
    } else {
        trail->next = ptr->next;  // Target is in the middle or end
    }
    
    ptr->next = NULL;
    return ptr; // Caller is responsible for free()
}
```

### Stacks: Push and Pop (Linked List Implementation)
```c
typedef struct Stack_s {
    SLLNode *top;
} Stack;

void push(Stack *s, int val) {
    SLLNode *newNode = malloc(sizeof(SLLNode));
    newNode->data = val;
    newNode->next = s->top;
    s->top = newNode;
}

int pop(Stack *s) {
    if (s->top == NULL) return -1; // Stack is empty
    
    SLLNode *tmp = s->top;
    int val = tmp->data;
    s->top = s->top->next;
    
    free(tmp);
    return val;
}
```

### Queues: Enqueue and Dequeue (Linked List Implementation)
```c
typedef struct Queue_s {
    SLLNode *front;
    SLLNode *rear;
} Queue;

void enqueue(Queue *q, int val) {
    SLLNode *newNode = malloc(sizeof(SLLNode));
    newNode->data = val;
    newNode->next = NULL;
    
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    
    q->rear->next = newNode;
    q->rear = newNode;
}

int dequeue(Queue *q) {
    if (q->front == NULL) return -1; // Queue is empty
    
    SLLNode *tmp = q->front;
    int val = tmp->data;
    q->front = q->front->next;
    
    if (q->front == NULL) {
        q->rear = NULL; // Queue became empty
    }
    
    free(tmp);
    return val;
}
```

## 3. Skills & Pitfalls

### Common Mistakes
- **Losing the head pointer:** Never modify the `head` pointer directly when traversing the list. Always use a temporary pointer (e.g., `ptr`) to iterate through nodes.
- **Ignoring NULL checks:** Failing to check if `ptr != NULL` before accessing `ptr->next` or `ptr->data` will lead to segmentation faults, especially when searching for a value that doesn't exist.
- **Memory Leaks:** Forgetting to store the reference to the next node before deallocating the current node during a list destruction operation.
- **Responsibility of Deallocation:** Deliberate design choices often detach a node rather than immediately `free()`ing it. The caller must be aware of their responsibility to deallocate the detached node.

### Must-Know Skills
- **Trailing Pointers:** Mastering the use of a trailing pointer (`trail`) that stays one step behind the main traversal pointer (`ptr`). This is crucial for generic insertion and deletion operations.
- **Boundary Conditions:** Actively accounting for edge cases:
  1. The list is currently empty.
  2. The operation affects the very first element (requires updating `head`).
  3. The operation affects the last element (requires updating the trailing node's `next` to `NULL` or updating the `tail` reference).
- **Visualization:** Developing the ability to visualize node connections and pointer assignments. The *order of actions* matters significantly in pointer manipulation.