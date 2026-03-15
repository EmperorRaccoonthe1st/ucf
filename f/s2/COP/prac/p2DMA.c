// strcpy is (destination, source)
//
// in scanf's for %s you can just use the name of an array, it will do the logic for you.
//
// Double Check your work!!!!!!!
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 101

typedef struct Book_s {
    char *title;
    int pages;
} Book;

typedef struct Library_s {
    Book *collection;
    int bookCount;
} Library;


void intitializeLibrary(Library *lib);


int main(void) {

    Library *lib = malloc(sizeof(Library));

    intitializeLibrary(lib);

    free(lib);

    return 0;
}


void intitializeLibrary(Library *lib) {
    int n = 0;
    scanf("%d", &n);

    Book *books = malloc(n * sizeof(Book));

    lib->collection = books;
    lib->bookCount = n;
    
    for (int i = 0; i < n; i++) {
        Book b;

        char buff[MAX_LEN];
        scanf("%s", &buff);

        char *title = malloc((strlen(buff) + 1) * sizeof(char) );
        strcpy(buff, title);
    
        book.title = title;
        scanf("%d", &book.pages);

        lib->collection[i] = book;
    }
}
