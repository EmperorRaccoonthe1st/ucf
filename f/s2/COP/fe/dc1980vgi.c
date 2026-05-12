// Struct representing video game information
typedef struct {
    char * name;
    int year;
    double price;
} videogame_t;

videogame_t* getClassicGames(videogame_t * inventory, int n, int* ptrNumGames) {
    videogame_t* res = malloc(n * sizeof(videogame_t));
    int nG = 0;

    

    // WRITE YOUR CODE HERE
    
    for (int i = 0; i < n; i++) {
        if (inventory[i].year > 1979 && inventory[i].year < 1990) {
            res[nG].year = inventory[i].year;
            res[nG].price = inventory[i].price;

            char *str = malloc((strlen(inventory[i].name) + 1) * sizeof(char));
            strcpy(str, inventory[i]);
            res[nG].name = str;
            
            nG++; 
        }
    } 
    
    res = realloc(res, nG * sizeof(videogame_t));
    *ptrNumGames = nG;
    return res;
}
