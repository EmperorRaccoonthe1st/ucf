#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_CHILD_COUNT 26

typedef struct TrieNode_s {
    struct TrieNode_s *children[MAX_CHILD_COUNT];
    int is_end_of_word;
} TrieNode;

typedef struct Trie_s {
    TrieNode *root;
} Trie;

// Function Prototypes (Existing)
TrieNode *trie_create_node();
void trie_destroy_node(TrieNode *node);
Trie *trie_create();
void trie_destroy(Trie *trie);
void trie_destroy_recursive(TrieNode *node);
void trie_insert(Trie *trie, char *word);
int has_children(TrieNode *node);

// Coding Exercise Prototypes
int count(TrieNode *node);
int count_starts_with(TrieNode *node, char *prefix);

// Wrapper for professor's style
int trie_count(Trie *trie); 

int main(void) {
    Trie *testTrie;
    
    // ---------------------------------------------------------
    // TEST CASE 1: Lab Manual words [cite: 11]
    // Words: cat, car, cart, carbon, dog, dove, dot, apple, app, ape
    // ---------------------------------------------------------
    testTrie = trie_create();
    char *words1[] = {"cat", "car", "cart", "carbon", "dog", "dove", "dot", "apple", "app", "ape"};
    for(int i = 0; i < 10; i++) trie_insert(testTrie, words1[i]);
    
    printf("--- Test Case 1 ---\n");
    printf("Total Words (Expected 10): %d\n", trie_count(testTrie));
    printf("Starts with 'ca' (Expected 4): %d\n", count_starts_with(testTrie->root, "ca"));
    printf("Starts with 'do' (Expected 3): %d\n", count_starts_with(testTrie->root, "do"));
    printf("Starts with 'ap' (Expected 3): %d\n", count_starts_with(testTrie->root, "ap"));
    trie_destroy(testTrie);

    // ---------------------------------------------------------
    // TEST CASE 2: Programming Languages
    // Words: c, cpp, java, javascript, python, php
    // ---------------------------------------------------------
    testTrie = trie_create();
    char *words2[] = {"c", "cpp", "java", "javascript", "python", "php"};
    for(int i = 0; i < 6; i++) trie_insert(testTrie, words2[i]);
    
    printf("\n--- Test Case 2 ---\n");
    printf("Total Words (Expected 6): %d\n", trie_count(testTrie));
    printf("Starts with 'j' (Expected 2): %d\n", count_starts_with(testTrie->root, "j"));
    printf("Starts with 'p' (Expected 2): %d\n", count_starts_with(testTrie->root, "p"));
    printf("Starts with 'c' (Expected 2): %d\n", count_starts_with(testTrie->root, "c"));
    trie_destroy(testTrie);

    // ---------------------------------------------------------
    // TEST CASE 3: Common Prefixes
    // Words: pre, prefix, prepare, press, pressure, preheat
    // ---------------------------------------------------------
    testTrie = trie_create();
    char *words3[] = {"pre", "prefix", "prepare", "press", "pressure", "preheat"};
    for(int i = 0; i < 6; i++) trie_insert(testTrie, words3[i]);
    
    printf("\n--- Test Case 3 ---\n");
    printf("Total Words (Expected 6): %d\n", trie_count(testTrie));
    printf("Starts with 'pres' (Expected 2): %d\n", count_starts_with(testTrie->root, "pres"));
    printf("Starts with 'preh' (Expected 1): %d\n", count_starts_with(testTrie->root, "preh"));
    trie_destroy(testTrie);

    // ---------------------------------------------------------
    // TEST CASE 4: Overlapping Short Words
    // Words: a, ab, abc, abcd, abcde
    // ---------------------------------------------------------
    testTrie = trie_create();
    char *words4[] = {"a", "ab", "abc", "abcd", "abcde"};
    for(int i = 0; i < 5; i++) trie_insert(testTrie, words4[i]);
    
    printf("\n--- Test Case 4 ---\n");
    printf("Total Words (Expected 5): %d\n", trie_count(testTrie));
    printf("Starts with 'abc' (Expected 3): %d\n", count_starts_with(testTrie->root, "abc"));
    trie_destroy(testTrie);

    // ---------------------------------------------------------
    // TEST CASE 5: Empty/Non-existent
    // Words: banana, berry, blue
    // ---------------------------------------------------------
    testTrie = trie_create();
    char *words5[] = {"banana", "berry", "blue"};
    for(int i = 0; i < 3; i++) trie_insert(testTrie, words5[i]);
    
    printf("\n--- Test Case 5 ---\n");
    printf("Starts with 'z' (Expected 0): %d\n", count_starts_with(testTrie->root, "z"));
    printf("Starts with 'blue' (Expected 1): %d\n", count_starts_with(testTrie->root, "blue"));
    trie_destroy(testTrie);

    return 0;
}

// ---------------------------------------------------------
// Coding Exercise 1: Count Words in Trie [cite: 19-23]
// ---------------------------------------------------------
int count(TrieNode *node) {
    int val = 0;

    if (node->is_end_of_word) val += 1;
      
    for (int i = 0; i < MAX_CHILD_COUNT; i++) {
        if (node->children[i] != NULL) {
            val += count(node->children[i]);
        }
    } 
    
    return val; // Placeholder
}

// ---------------------------------------------------------
// Coding Exercise 2: Count Words starting with Prefix [cite: 26-32]
// ---------------------------------------------------------
int count_starts_with(TrieNode *node, char *prefix) {
    TrieNode *root = node; 
    int amt = 0;

    int i = 0;
    while (prefix[i] != '\0') {
        int index = prefix[i] -  97;
    
        if (root->children[index] != NULL) {
             root = root->children[index];
        } else {
            return 0;
        }
    
        i++;
    }

    amt = count(root);

    return amt;
}

// ---------------------------------------------------------
// Helper & Utility Functions (Professor's Style)
// ---------------------------------------------------------

int trie_count(Trie *trie) {
    if (trie == NULL) return 0;
    return count(trie->root);
}

TrieNode *trie_create_node() {
    TrieNode *node = malloc(sizeof(TrieNode));
    if(node == NULL) return NULL;
    node->is_end_of_word = 0;
    for(int i = 0; i < MAX_CHILD_COUNT; i++)
        node->children[i] = NULL;
    return node;
}

Trie *trie_create() {
    Trie *trie = malloc(sizeof(Trie));
    if(trie == NULL) return NULL;
    trie->root = trie_create_node();
    return trie;
}

void trie_insert(Trie *trie, char *word) {
    TrieNode *ptr = trie->root;
    int len = strlen(word);
    for(int i = 0; i < len; i++) {
        int idx = word[i] - 'a';
        if(ptr->children[idx] == NULL) {
            ptr->children[idx] = trie_create_node();
        }
        ptr = ptr->children[idx];
    }
    ptr->is_end_of_word = 1;    
}

void trie_destroy_recursive(TrieNode *node) {
    if(node == NULL) return;
    for(int i = 0; i < MAX_CHILD_COUNT; i++) {
        trie_destroy_recursive(node->children[i]);
    }
    free(node);
}

void trie_destroy(Trie *trie) {
    if (trie == NULL) return;
    trie_destroy_recursive(trie->root);
    free(trie);
}

int has_children(TrieNode *node) {
    for(int i = 0; i < MAX_CHILD_COUNT; i++) {
        if(node->children[i]) return 1;
    }
    return 0;
}
