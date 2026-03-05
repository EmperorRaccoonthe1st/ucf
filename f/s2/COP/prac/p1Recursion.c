// When returning an int, do not use the increment operator instead just use an expression.
int count(int *arr, int size, int target) {

    if (size == 0) {
        return 0;
    }

    int num = 0; 
    
    num = count(arr, size-1, target);
    
    if (arr[size-1] == target) return num + 1;

    return num;
}
