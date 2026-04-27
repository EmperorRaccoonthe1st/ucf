#include <stdlib.h>
#include <string.h>
#include "q1.h"

/*
    COP 3502C Q1
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
    compiler or an IDE while completing this file.

    You may submit multiple times on Gradescope before the submission 
    deadline. Only the final submission before the deadline will be graded.
*/


#ifdef T1
Point **transform_points(int *arr1, int *arr2, int size) {
    // TODO: Complete this function
    // TODO 1 BEGIN
    Point **points = malloc(size * sizeof(Point *));

    for (int i = 0; i < size; i++) {
        Point *p = malloc(sizeof(Point));
        p->x = arr1[i];
        p->y = arr2[i];
        points[i] = p;
    }

    return points;
        
    // TODO 1 END
}
#endif


#ifdef T2
Student *create_student(char *name, char courses[][101], int count, int year) {
    // TODO: Complete this function
    // TODO 2 BEGIN

    Student *s = malloc(sizeof(Student));
    
    // Name
    char *n = malloc((strlen(name) + 1 ) * sizeof(char));
    strcpy(n, name);
    s->name = n;

    char **cs = malloc(count * sizeof(char *)); 
    for (int i = 0; i < count; i++) {
        char *course = malloc((strlen(courses[i]) + 1 ) * sizeof(char));
        strcpy(course, courses[i]); 
        cs[i] = course;
    }
    s->courses = cs;

    s->courseCount = count;
    s->yearLevel = year;

    return s;

    // TODO 2 END
}
#endif


#ifdef T3
void destroy_student(Student *s) {
    // TODO: Complete this function
    // TODO 3 BEGIN

    free(s->name);

    for( int i = 0; i < s->courseCount; i++) {
        free(s->courses[i]);
    } 
    free(s->courses);

    free(s);

    // TODO 3 END
}
#endif


#ifdef T4
Account *merge_accounts(const Account *a1, const Account *a2) {
    // TODO: Complete this function
    // TODO 4 BEGIN

    Account *a = malloc(sizeof(Account));

    char *name = malloc((strlen(a1->name) + strlen(a2->name) + 6) * sizeof(char));
    name[0] = '\0';    
    strcat(name, a1->name);
    strcat(name, " and ");
    strcat(name, a2->name);
    a->name = name;

    a->amount = a1->amount + a2->amount;

    a->id = a2->id;

    return a;

    // TODO 4 END
}
#endif

