void cleanUp(book_t * lib, int numBooks){

    // WRITE YOUR CODE HERE
    
    for (int i = 0; i < numBooks; i++) {
        for (int x = 0; x < lib[i]->numSentences; x++) {
            free(lib[i]->sentences[x]);
        }
        free(lib[i]->sentences);

        free(lib[i]->title);
        free(lib[i]->author);
    }    
}
