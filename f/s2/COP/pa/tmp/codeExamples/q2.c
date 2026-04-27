#include "q2.h"

/*
    COP 3502C Q2
    This program is written by: Owen Lopez

    This file is intentionally incomplete to simulate a written exam.
    Further, you will not be provided the contents of the q1.h file.

    You should first work out your solution using pencil and paper.
    Once you are confident in your answer, type the final solution
    into this file.

    You may ONLY write code inside the bodies of the required functions.
    Do NOT modify function signatures, include directives, or any other
    part of this file.

    Write your answers using a plain text editor only. Do NOT use a
    compiler or an IDE while completing this file. Save your file as q2.c

    You may submit multiple times on Gradescope before the submission 
    deadline. Only the final submission before the deadline will be graded.
*/


#ifdef T1
int sum(int n) {
    // TODO: Complete this function
    // TODO 1 BEGIN

    if (n == 0) {
        return n;
    }

    int num = sum(n-1);

    return n+num;

    // TODO 1 END
}
#endif

#ifdef T2
void reverse(char *str, int left, int right) {
    // TODO: Complete this function
    // TODO 2 BEGIN
    
    if ( left >= right) return;

    char tmp;
    
    tmp = str[left];
    str[left] = str[right];
    str[right] = tmp;
    
    reverse(str, left+1, right-1);

    // TODO 2 END
}
#endif


#ifdef T3
int max(int *arr, int n) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    if (n == 1) return arr[0];

    int num = max(arr, n-1);

    if (num > arr[n-1]) {
        return num;
    } else {
        return arr[n-1];
    }

    // TODO 3 END
}
#endif
