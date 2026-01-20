#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Person_s {
    char *name;
    int age;
} Person;

Person *create_person(const char *name, int age);
void destroy_person(Person *p);

int main(void) {
    int age;
    char name[256];

    printf("Enter a name and age: ");
    scanf("%s%d", name, &age);

    Person *p = create_person(name, age);

    printf("%s is %d years old\n", p->name, p->age);
    
    return 0;
}

Person *create_person(const char *name, int age) {
    Person *p = malloc(sizeof(Person));

    if (p == NULL) {
        free(p);
        return NULL;
    }

    p->name =  malloc(sizeof(char) * (strlen(name)+1));

    if (p->name == NULL) {
        free(p->name);
        return NULL;
    }

    strcpy(p->name, name);
        
    p->age = age;

    return p;
}

void destroy_person(Person *p) {
    free(p->name);

    free(p);
}
