/* COP 3502C PA5
This program is written by: Owen Manuel Lopez */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define INPUT_FILE "tournament.txt"
#define MAX_NAME 25
#define MAX_LEN 26
#define NUM_TRAITS 5
#define EXISTS -2 
#define REPLACED -1 

typedef struct Cat_s {
    char *name;                 // dynamically allocated cat name
    char *breed;                // dynamically allocated cat breed
    int charm;                  // unique charm score
    int traits[NUM_TRAITS];     // values corresponding to TRAITS
} Cat;

typedef struct BSTNode_s {
    Cat *cat;
    struct BSTNode_s *left;
    struct BSTNode_s *right;
    int subtree_size;           // size of this subtree, not height
} BSTNode;

const char TRAITS[NUM_TRAITS][MAX_LEN] = {
    "friendly", "grumpy", "playful", "lazy", "curious"
};

void myMain(FILE *ifile);
char **filterByTrait(BSTNode *root, int traitIndex, int traitValue, int *resultSize);

char *readWord(FILE *ifile);
Cat *readCat(FILE *ifile);
void freeCat(Cat *c);
void cpyCat(Cat *d, Cat *s);
BSTNode *createNode();
void freeNode(BSTNode *n);
void deleteNode(BSTNode *n);
void freeTree(BSTNode *root);

int insert(BSTNode **root, Cat *cat);
int insertRec(BSTNode *root, Cat *cat);
BSTNode *searchForCat(BSTNode *root, char *name);
BSTNode *searchForCatParent(BSTNode *root, char *name);
BSTNode *findSuccessor(BSTNode *n);
void walk(BSTNode *root);
void delete(BSTNode **root, BSTNode *n);
void pruneSubtreeSize(BSTNode *root, char *name);
BSTNode *findKth(BSTNode *root, int k);
void findTraits(BSTNode *root, int traitIndex, int traitValue, char **names, int *amt);

void query1(FILE *ifile, BSTNode **root);
void query2(FILE *ifile, BSTNode **root);
void query3(FILE *ifile, BSTNode *root);
void query4(FILE *ifile, BSTNode *root);
void query5(FILE *ifile, BSTNode **root);
void query6(FILE *ifile, BSTNode *root);

#ifndef MAIN_FUNCTION
int main(void) {
    FILE *ifile = fopen(INPUT_FILE, "r");
    
    if (ifile == NULL) {
        printf("File Does Not Exist!\n");
        return 1;
    }
    
    myMain(ifile);
    fclose(ifile);
    
    return 0;
}
#endif

void myMain(FILE *ifile) {
    BSTNode *root = NULL;
    int num;

    if (fscanf(ifile, "%d", &num) != 1) {
        return;
    }

    for (int i = 0; i < num; i++) {
        int query;
        if (fscanf(ifile, "%d", &query) != 1) {
            break;
        }

        switch (query) {
            case 1: 
                query1(ifile, &root); 
                break;
            case 2: 
                query2(ifile, &root); 
                break;
            case 3: 
                query3(ifile, root);  
                break;
            case 4: 
                query4(ifile, root);  
                break;
            case 5: 
                query5(ifile, &root); 
                break;
            case 6: 
                query6(ifile, root);  
                break;
        }
    }

    freeTree(root);
}

void freeTree(BSTNode *root) {
    if (root == NULL) {
        return;
    }
    freeTree(root->left);
    freeTree(root->right);
    deleteNode(root);
}

char **filterByTrait(BSTNode *root, int traitIndex, int traitValue, int *resultSize) {
    if (root == NULL) {
        return NULL;
    }

    char **names = malloc(root->subtree_size * sizeof(char *));
    int amt = 0;

    findTraits(root, traitIndex, traitValue, names, &amt);
    *resultSize = amt;

    if (amt == 0) {
        free(names);
        return NULL;
    }

    char **finalNames = realloc(names, amt * sizeof(char *));
    return finalNames;
}

Cat *readCat(FILE *ifile) {
    Cat *c = malloc(sizeof(Cat));
    c->name = readWord(ifile);
    c->breed = readWord(ifile);
    fscanf(ifile, "%d", &c->charm);
    for (int i = 0; i < NUM_TRAITS; i++) {
        fscanf(ifile, "%d", &c->traits[i]);
    }
    return c;
}

char *readWord(FILE *ifile) {
    char buff[MAX_NAME + 1];
    if (fscanf(ifile, "%s", buff) != 1) {
        return NULL;
    }
    
    char *word = malloc((strlen(buff) + 1) * sizeof(char));
    strcpy(word, buff);
    return word;
}

void freeCat(Cat *c) {
    if (c == NULL) {
        return;
    }
    free(c->name);
    free(c->breed);
    free(c);
}

BSTNode *createNode() {
    BSTNode *n = malloc(sizeof(BSTNode));
    n->left = NULL;
    n->right = NULL;
    n->subtree_size = 1; 
    return n;
}

void freeNode(BSTNode *n) {
    free(n);
}

void deleteNode(BSTNode *n) {
    if (n == NULL) {
        return;
    }
    freeCat(n->cat);
    freeNode(n);
}

void query1(FILE *ifile, BSTNode **root) {
    Cat *c = readCat(ifile);
    int depth = insert(root, c);

    if (depth == EXISTS) {
        freeCat(c);
    } else if (depth == REPLACED) {
        printf("Replaced\n");
    } else {
        printf("Insert: %d\n", depth);
    }
}

int insert(BSTNode **root, Cat *cat) {
    if (*root == NULL) {
        BSTNode *n = createNode();
        n->cat = cat;
        *root = n;
        return 0;
    }

    BSTNode *n = searchForCat(*root, cat->name);
    if (n != NULL) {
        int c1 = 0, c2 = 0;
        for (int i = 0; i < NUM_TRAITS; i++) {
            if (n->cat->traits[i] == 1) {
                c1++;
            }
            if (cat->traits[i] == 1) {
                c2++;
            }
        }

        if (c2 > c1) {
            freeCat(n->cat);
            n->cat = cat;
            return REPLACED;
        } else {
            return EXISTS;
        }
    }

   return insertRec(*root, cat); 
}

int insertRec(BSTNode *root, Cat *cat) {
    root->subtree_size++; 
    
    if (strcmp(cat->name, root->cat->name) > 0) {
        if (root->right != NULL) {
            return insertRec(root->right, cat) + 1;
        } else {
            BSTNode *n = createNode();
            n->cat = cat;
            root->right = n;
            return 1;
        }
    } else {
        if (root->left != NULL) {
            return insertRec(root->left, cat) + 1;
        } else {
            BSTNode *n = createNode();
            n->cat = cat;
            root->left = n;
            return 1;
        }
    }
}

BSTNode *searchForCat(BSTNode *root, char *name) {
    if (root == NULL || name == NULL) {
        return NULL; 
    }
    
    int cmp = strcmp(name, root->cat->name);
    if (cmp == 0) {
        return root;
    }
    if (cmp > 0) {
        return searchForCat(root->right, name);
    }
    return searchForCat(root->left, name);
}

BSTNode *searchForCatParent(BSTNode *root, char *name) {
    if (root == NULL || name == NULL || strcmp(root->cat->name, name) == 0) {
        return NULL; 
    }

    int cmp = strcmp(name, root->cat->name);
    if (cmp > 0) {
        if (root->right != NULL && strcmp(root->right->cat->name, name) == 0) {
            return root;
        }
        return searchForCatParent(root->right, name);
    } else {
        if (root->left != NULL && strcmp(root->left->cat->name, name) == 0) {
            return root;
        }
        return searchForCatParent(root->left, name);
    }
}

void pruneSubtreeSize(BSTNode *root, char *name) {
    if (root == NULL || name == NULL) {
        return; 
    }
    root->subtree_size--;

    int cmp = strcmp(name, root->cat->name);
    if (cmp == 0) {
        return;
    }
    if (cmp > 0) {
        pruneSubtreeSize(root->right, name);
    } else {
        pruneSubtreeSize(root->left, name);
    }
}

BSTNode *findSuccessor(BSTNode *n) {
    if (n == NULL) {
        return NULL;
    }
    BSTNode *curr = n;
    while (curr->left != NULL) {
        curr = curr->left;
    }
    return curr;
}

void query2(FILE *ifile, BSTNode **root) {
    char *name = readWord(ifile);
    BSTNode *n = searchForCat(*root, name);
    if (n != NULL) {
        delete(root, n);
    }
    
    free(name);
    printf("Deletion Complete\n");
}

void query3(FILE *ifile, BSTNode *root) {
    int k;
    fscanf(ifile, "%d", &k);

    if (root == NULL || k > root->subtree_size) {
        printf("NO SMALLEST ELEMENT FOUND\n");
    } else {
        BSTNode *kth = findKth(root, k);
        printf("%s %s %d\n", kth->cat->name, kth->cat->breed, kth->cat->charm);
    }
}

void query4(FILE *ifile, BSTNode *root) {
    int traitIndex, traitValue;
    fscanf(ifile, "%d %d", &traitIndex, &traitValue);

    if (root == NULL) {
        printf("NONE FOUND\n");
        return;
    }

    int resultSize = 0;
    char **names = filterByTrait(root, traitIndex, traitValue, &resultSize);

    if (names == NULL || resultSize == 0) {
        printf("NONE FOUND\n");
    } else {
        printf("%s:", TRAITS[traitIndex]);
        for (int i = 0; i < resultSize; i++) {
            printf(" %s", names[i]);
            free(names[i]);
        }
        printf("\n");  
        free(names); 
    }
}

void query5(FILE *ifile, BSTNode **root) {
    int traitIndex, traitValue;
    fscanf(ifile, "%d %d", &traitIndex, &traitValue);

    int matches = 0;
    char **deletes = filterByTrait(*root, traitIndex, traitValue, &matches);

    if (deletes == NULL || matches == 0) {
        printf("NONE REMOVED\n");
        return;
    }
    
    for (int i = 0; i < matches; i++) {
        BSTNode *c = searchForCat(*root, deletes[i]);
        if (c != NULL) {
            delete(root, c);
        }
        free(deletes[i]);
    } 
    free(deletes);
    printf("%d\n", matches);
}

void query6(FILE *ifile, BSTNode *root) {
    (void)ifile;
    if (root == NULL) {
        printf("EMPTY\n");
    } else {
        walk(root);
    }
}

void delete(BSTNode **root, BSTNode *n) {
    if (*root == NULL || n == NULL) {
        return; 
    }

    if (n->left != NULL && n->right != NULL) {
        BSTNode *successor = findSuccessor(n->right);
        Cat *succCat = successor->cat;
        
        pruneSubtreeSize(*root, succCat->name);
        BSTNode *parent = searchForCatParent(*root, succCat->name);
        BSTNode *child = successor->right;

        if (parent == NULL) {
            *root = child;
        } else {
            if (parent->left == successor) {
                parent->left = child;
            } else {
                parent->right = child;
            }
        }

        freeCat(n->cat);
        free(successor);
        n->cat = succCat;
        return;
    }

    pruneSubtreeSize(*root, n->cat->name);
    BSTNode *parent = searchForCatParent(*root, n->cat->name);
    BSTNode *child = NULL;
    if (n->left != NULL) {
        child = n->left;
    } else {
        child = n->right;
    }

    if (parent == NULL) {
        *root = child;
    } else {
        if (parent->left == n) {
            parent->left = child;
        } else {
            parent->right = child;
        }
    }

    deleteNode(n);
}

BSTNode *findKth(BSTNode *root, int k) {
    if (root == NULL) {
        return NULL;
    }
    int lSize = 0;
    if (root->left != NULL) {
        lSize = root->left->subtree_size;
    } else {
        lSize = 0;
    }

    if (k <= lSize) {
        return findKth(root->left, k);
    } else if (k == lSize + 1) {
        return root;
    } else {
        return findKth(root->right, k - (lSize + 1)); 
    }
}

void findTraits(BSTNode *root, int traitIndex, int traitValue, char **names, int *amt) {
    if (root == NULL) {
        return;
    }
    findTraits(root->left, traitIndex, traitValue, names, amt);
    
    if (root->cat->traits[traitIndex] == traitValue) {
        char *name = malloc((strlen(root->cat->name) + 1) * sizeof(char));
        strcpy(name, root->cat->name);    
        names[*amt] = name;
        *amt = *amt + 1;
    }
    
    findTraits(root->right, traitIndex, traitValue, names, amt);
}

void walk(BSTNode *root) {
    if (root == NULL) {
        return;
    }
    walk(root->left);
    printf("%s %d %d\n", root->cat->name, root->cat->charm, root->subtree_size);
    walk(root->right);
}
