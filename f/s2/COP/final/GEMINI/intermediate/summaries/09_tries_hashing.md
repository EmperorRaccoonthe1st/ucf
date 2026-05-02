# Topic Summary: Tries & Hash Tables

## 1. Theoretical Core

### Tries
- **Definition**: A multiway tree (often called a prefix tree) used to store a list of strings (a dictionary). Nodes usually do not contain the character data itself; instead, the character is implied by the path (e.g., an array of 26 child pointers for the English alphabet).
- **Structure**: Each node contains an array of pointers to its children and a flag (`is_end_of_word`) to indicate if the path from the root to that node forms a valid string in the dictionary.
- **Complexity**: Operations (Insert, Search, Remove) take $O(k)$ time in the worst-case, where $k$ is the length of the string. The height of the trie is bound by the length of the longest prefix/string.
- **Space Trade-off**: Tries can use a lot of memory (many pointers), especially if the prefixes are not shared extensively. However, they are highly optimized for prefix-based searches and dictionary lookups.

### Hash Tables
- **Definition**: An implementation of the Table Abstract Data Type (ADT), which stores `(key, value)` pairs and allows for constant-time expected retrieval based on a unique key.
- **Hash Function ($h(k)$)**: A function that maps a key $k$ to a slot index in an array of size $m$. This maps a large universe of keys $U$ into a smaller table, saving space compared to a Direct Address Table. A simple hash function uses the division method: $h(k) = k \pmod m$.
- **Load Factor ($\alpha$)**: The ratio of the number of elements $n$ to the number of slots $m$ ($\alpha = n / m$). It measures how full the table is.
- **Collision Resolution**: Occurs when two different keys hash to the same slot ($h(k_1) = h(k_2)$).
  - **Separate Chaining**: Each slot in the hash table points to a linked list of all elements that hashed to that slot. Expected search time is $O(1 + \alpha)$.
  - **Open Addressing**: All elements are stored in the hash table itself. When a collision occurs, a *probe sequence* is followed to find the next available slot.
    - **Linear Probing**: $h(k, i) = (h'(k) + i) \pmod m$
    - **Quadratic Probing**: $h(k, i) = (h'(k) + i^2) \pmod m$

## 2. Algorithmic Tracing

**Hashing Trace Example**: 
Given a hash table of size $m = 7$ and keys with initial hash values $h'(k) = k \pmod 7$. 
Keys to insert: `A(6)`, `B(6)`, `C(5)`, `D(5)`

*   **Linear Probing** ($h(k, i) = (h'(k) + i) \pmod 7$):
    *   Insert `A`: $6 \pmod 7 = 6$. Slot 6 is empty. Insert at index 6.
    *   Insert `B`: $6 \pmod 7 = 6$ (Collision). Probe $i=1$: $(6 + 1) \pmod 7 = 0$. Slot 0 is empty. Insert at index 0.
    *   Insert `C`: $5 \pmod 7 = 5$. Slot 5 is empty. Insert at index 5.
    *   Insert `D`: $5 \pmod 7 = 5$ (Collision). Probe $i=1$: $(5 + 1) \pmod 7 = 6$ (Collision). Probe $i=2$: $(5 + 2) \pmod 7 = 0$ (Collision). Probe $i=3$: $(5 + 3) \pmod 7 = 1$. Slot 1 is empty. Insert at index 1.

*   **Quadratic Probing** ($h(k, i) = (h'(k) + i^2) \pmod 7$):
    *   Insert `A`: $6 \pmod 7 = 6$. Slot 6 is empty. Insert at index 6.
    *   Insert `B`: $6 \pmod 7 = 6$ (Collision). Probe $i=1$: $(6 + 1^2) \pmod 7 = 0$. Slot 0 is empty. Insert at index 0.
    *   Insert `C`: $5 \pmod 7 = 5$. Slot 5 is empty. Insert at index 5.
    *   Insert `D`: $5 \pmod 7 = 5$ (Collision). Probe $i=1$: $(5 + 1^2) \pmod 7 = 6$ (Collision). Probe $i=2$: $(5 + 2^2) \pmod 7 = (5+4) \pmod 7 = 2$. Slot 2 is empty. Insert at index 2.

## 3. Code Implementation

**Trie Structures & Insertion (C Snippet)**
```c
#define MAX_CHILD_COUNT 26

typedef struct TrieNode_s {
    struct TrieNode_s *children[MAX_CHILD_COUNT];
    int is_end_of_word;
} TrieNode;

typedef struct Trie_s {
    TrieNode *root;
} Trie;

void trie_insert(Trie *trie, char *word) {
    TrieNode *ptr = trie->root;
    int len = strlen(word);
    for(int i = 0; i < len; i++) {
        int idx = word[i] - 'a';
        if(ptr->children[idx] == NULL) {
            // Assume trie_create_node() initializes children to NULL and flag to 0
            ptr->children[idx] = trie_create_node(); 
        }
        ptr = ptr->children[idx];
    }
    ptr->is_end_of_word = 1;    
}
```

**Simple String Hash Function (C Snippet)**
```c
int string_to_int(char *str) {
    int sum = 0;
    for (int i = 0; str[i] != '\0'; i++) {
        sum += str[i];
    }
    return sum;
}

int hash_function(int key, int m) {
    return key % m; // Division method
}
```

## 4. Skills & Pitfalls

### Must-Know Skills
- **Choosing Hash Table Size**: Ideally, $m$ should be a prime number not too close to an exact power of 2. For Quadratic Probing, $m$ must be prime and the table should be at least half empty (load factor $< 0.5$) to guarantee finding an open slot and avoiding infinite loops.
- **Handling Strings in Hash Tables**: Converting strings to integers (e.g., summing ASCII values) allows them to be hashed using mathematical functions like the division method.
- **Trie Prefix Search**: Tries excel at prefix matching. Iterating through the trie path matching the prefix string character by character will land the pointer at the subtree containing all words with that prefix.

### Common Pitfalls
- **Clustering in Open Addressing**: Linear probing often leads to *primary clustering*, where blocks of occupied slots build up, increasing search times. Quadratic probing mitigates this but can still suffer from *secondary clustering*.
- **Premature Search Termination (Open Addressing)**: When deleting an item in an open addressing table, you must not simply clear the slot. Doing so breaks the probe sequence for elements that collided and were stored further down. You must use a special "tombstone" or `DELETED_MARKER` to indicate a slot is empty for insertion but should be bypassed during a search.
- **Trie Memory Leaks & Over-deletion**: When removing a word from a trie, care must be taken to only delete nodes recursively upwards if they have no other children. Deleting a shared prefix node breaks other words stored in the trie. Completely freeing a trie requires a post-order traversal to prevent memory leaks.
