#include "q6.h"

/*
    COP 3502C Q6
    This program is written by: Owen Manuel Lopez

    This file is intentionally incomplete to simulate a written exam.
    Further, you will not be provided the contents of the q6.h file.

    You should first work out your solution using pencil and paper.
    Once you are confident in your answer, type the final solution
    into this file.

    You may ONLY write code inside the bodies of the required functions.
    Do NOT modify function signatures, include directives, or any other
    part of this file.

    Write your answers using a plain text editor only. Do NOT use a
    compiler or an IDE while completing this file. Save your file as q6.c

    You may submit multiple times on Gradescope before the submission 
    deadline. Only the final submission before the deadline will be graded.
*/


#ifdef T1
int isBalanced(BTNode *r) {
    // TODO: Complete this function
    // TODO 1 BEGIN

    if (r == NULL) return 1;

    int val = 1;

    if (r->left == NULL && r->right == NULL) return 1;

    if (r->left != NULL) val = isBalanced(r->left);
    if (r->right != NULL && val != 0) val = isBalanced(r->right);
     
    int lHeight, rHeight;

    lHeight = (r->left != NULL) ? height(r->left) : -1;
    rHeight = (r->right != NULL) ? height(r->right) : -1;

    if (abs(lHeight - rHeight) < 2) {
        return val;
    } else {
        return 0;
    }
    
    // TODO 1 END
}
#endif


#ifdef T2
void twoChildren(BTNode *r) {
    // TODO: Complete this function
    // TODO 2 BEGIN

    if (r == NULL) return 0;



    if (r->left != NULL) twoChildren(r->left);
    if (r->right != NULL) twoChildren(r->right);
     
    int lHeight, rHeight;

    lHeight = (r->left != NULL) ? height(r->left) : -1;
    rHeight = (r->right != NULL) ? height(r->right) : -1;

    if (lHeight == 0 && rHeight == 0) {
        if (r->left-data >= l->right->data) {
            return prinwf("%d\n%d\n", r->left-data, r->right->data);
        } else {
            return prinwf("%d\n%d\n", r->right-data, r->left->data);
        }
    }

    return;

    // TODO 2 END
}
#endif


#ifdef T3
int treeHeightDelete(void) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    // What is the height of the binary search tree
    // after deleting the node?
    // An example is provided for reference.
    
    // Assuming your answer is: 0
    return 0;

    // TODO 3 END
}
#endif


#ifdef T4
int fooAnswer(void) {
    // TODO: Complete this function
    // TODO 4 BEGIN

    // What is the return value?
    // An example is provided for reference.
    
    // Assuming your answer is: 0
    return 0;

    // TODO 4 END
}
#endif


#ifdef T5
int treeHeight(void) {
    // TODO: Complete this function
    // TODO 5 BEGIN

    // What is the height of the binary search tree?
    // An example is provided for reference.
    
    // Assuming your answer is: 0
    return 0;

    // TODO 5 END
}
#endif
