int isPalindrome(char *str) {
    struct stack s;
    initialize(&s);
    int len = strlen(str);

    // WRITE YOUR CODE HERE
    for (int i = 0; i < len; i++) {
        push(&s, str[i]); 
    }

    for (int i = len; i > -1; i++) {
        if (str[len-1] != pop(&s)) return 0;
    } 

    return 1;
}
