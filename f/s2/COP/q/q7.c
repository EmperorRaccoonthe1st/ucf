#include "q7.h"

/*
    COP 3502C Q7
    This program is written by: Your Full Name

    This file is intentionally incomplete to simulate a written exam.
    Further, you will not be provided the contents of the q7.h file.

    You should first work out your solution using pencil and paper.
    Once you are confident in your answer, type the final solution
    into this file.

    You may ONLY write code inside the bodies of the required functions.
    Do NOT modify function signatures, include directives, or any other
    part of this file.

    Write your answers using a plain text editor only. Do NOT use a
    compiler or an IDE while completing this file. Save your file as q7.c

    You may submit multiple times on Gradescope before the submission 
    deadline. Only the final submission before the deadline will be graded.
*/


#ifdef T1
int heapInsert(int heapArr[], int *heapSize, int heapCapacity, int item) {
    // TODO: Complete this function
    // TODO 1 BEGIN

    if (*heapSize == heapCapacity) return 0;

    heapArr[*heapSize] = item;
    
    (*heapSize)++;

    percolateUp(heapArr, *heapSize, *heapSize - 1);

    return 1; 

    // TODO 1 END
}
#endif


#ifdef T2
int hasPrefixPlusOne(TrieNode *root, char *prefix) {
    // TODO: Complete this function
    // TODO 2 BEGIN

    if (root == NULL) return 0;
    
    if (prefix[0] == '\0') {
        for (int i = 0; i < 26; i++) {
            if (root->children[i] != NULL && root->children[i]->is_end_of_word) return 1;
        }

        return 0;
    }

    int val = 0;

    int index = prefix[0] - 'a';
    val = hasPrefixPlusOne(root->children[index], prefix + 1);

    return val;

    // TODO 2 END
}
#endif

