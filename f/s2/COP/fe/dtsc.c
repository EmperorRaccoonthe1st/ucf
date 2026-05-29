int ** triangularSum(int * base, int n) {
    
    // WRITE YOUR CODE HERE
    
    int **arr = malloc(n * sizeof(int *));    

    for (int i = 0; i < n; i++) {
        arr[i] = malloc((n-i) * sizeof(int));
    }

    for (int i = 0; i < n; i++) {
        arr[0][i] = i +1;
    )

    for (int i = 1; i < n; i++) {
        for (int x = 0; x < 5-n; x++) {
            arr[n][x] = arr[n-1][x] + arr[n-1][x+1];
        }
    }

    return arr;
}
