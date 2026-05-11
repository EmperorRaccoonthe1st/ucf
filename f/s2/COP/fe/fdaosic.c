struct present {
    char *present_name;
    float price;
};

struct present* delete_present_list(struct present* present_list, int num) {
    
    // WRITE YOUR CODE HERE
    for (int i = 0; i < num; i++) {
        free(present_list[i].present_name);
    }    

    free(present_list);

    return NULL;
}
