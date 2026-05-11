#include <string.h>
#include <stdlib.h>

struct juice_case {
    char name[128];
    int num_bottles;
};

struct juice_case* create_case(char *new_name, int new_number) {
    
    // WRITE YOUR CODE HERE

    juice_case *jc = malloc(sizeof(juice_case));
    
    strcpy(&jc->name, new_name);
    jc->num_bottles = new_number

    return jc;
}
