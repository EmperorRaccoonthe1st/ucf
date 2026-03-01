#include "q4.h"

/*
    COP 3502C Q4
    This program is written by: Owen Manuel Lopez

    This file is intentionally incomplete to simulate a written exam.
    Further, you will not be provided the contents of the q4.h file.

    You should first work out your solution using pencil and paper.
    Once you are confident in your answer, type the final solution
    into this file.

    You may ONLY write code inside the bodies of the required functions.
    Do NOT modify function signatures, include directives, or any other
    part of this file.

    Write your answers using a plain text editor only. Do NOT use a
    compiler or an IDE while completing this file. Save your file as q4.c

    You may submit multiple times on Gradescope before the submission 
    deadline. Only the final submission before the deadline will be graded.
*/


#ifdef T1
const char *solve(void) {
    // TODO: Complete this function
    // TODO 1 BEGIN

    // Put your answers between the double quotes.
    // Note: The autograder is sensitive to whitespaces.
    // An example is provided for reference.
    
    // Assuming your answer is: 1 2 3
    return "3 18 58 23 12 31 19 26 3 ";

    // TODO 1 END
}
#endif


#ifdef T2
void battle_game(Queue *gameQueue) {
    // TODO: Complete this function
    // TODO 2 BEGIN

    while (size(gameQueue) > 1) {

        Player *p1 = dequeue(gameQueue);
        Player *p2 = dequeue(gameQueue);

        if (p2->hp >= p1->hp) {
            enqueue(gameQueue, p2);
            delete_player(p1);
        } else {
            enqueue(gameQueue, p1);
            delete_player(p2);
        }

    }
    
    printf("%s", front(gameQueue)->name);

    delete_player(front(gameQueue));

    // TODO 2 END
}
#endif


#ifdef T3
int is_balanced(char *exp) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    Stack s;
    initialize(&s);

    int i = 0;
    char currentChar = exp[i];
    while (currentChar != '\0') {
        switch (currentChar) {
            case '(':
                push(&s, currentChar);
                break;

            case '{':
                push(&s, currentChar);
                break;

            case ')':
                if (peek(&s) == '(') {
                     pop(&s);
                } else {
                    return 0;
                }
                break;

            case '}':
                if (peek(&s) == '{') {
                     pop(&s);
                } else {
                    return 0;
                }
                break;
        }

        i++;
        currentChar = exp[i];
    }

    return is_empty(&s);

    // TODO 3 END
}
#endif

