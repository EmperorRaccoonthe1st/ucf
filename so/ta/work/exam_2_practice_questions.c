#include <stdio.h>
#include <ctype.h>

//Name of Contributor: Owen Lopez
//Topic: Functions
//Question: What should the function prototype be for the following function. The return type has been omitted.
//
//secretCode(int varA, long varB) {
//
    //varA = (varA  5) % 5;
    //varB =/ 0.33;
//
    //char newVar = varA  + ((int)(varB % 26 ) + 'a');
//
    //return newVar;
//}
//
//Answer: char secretCode(int varA, long varB);


//Name of Contributor: Owen Lopez
//Topic: Functions
//Question: Trace the following code & enter the output of the program

//int functionA(int a, int b);
//int functionC(int a);
//
//int main(void) {
    //int num = 2;
//
    //num = functionA(num, 2);
    //printf("%c\n", functionC(num));
//
    //return 0;
//}
//
//
//int functionA(int a, int b) {
    //int c = a;
    //c += a + c + b;
    //a = c;
//
    //return a;
//}
//
//int functionC(int a) {
    //int alpha = 'A';
//
    //alpha = a + 2; 
    //alpha /= a;
//
    //return alpha;
//}
//
//Answer: I
//Name of Contributor: Owen Lopez
//Topic: Functions
//Question: Trace the following code & enter the output of the program

//int functionA(int a, int b);
//int functionC(int a);
//
//int main(void) {
    //int num = 2;
//
    //num = functionA(num, 2);
    //printf("%c\n", functionC(num));
//
    //return 0;
//}
//
//
//int functionA(int a, int b) {
    //int c = a;
    //c += a + c + b;
    //a = c;
//
    //return a;
//}
//
//int functionC(int a) {
    //int alpha = 'A';
//
    //alpha = a + 2; 
    //alpha /= a;
//
    //return alpha;
//}
//
//Answer: I

//Name of Contributor: Owen Lopez
//Topic: Array
//Difficulty: Easy
//Question: Provide the indexes to the provided arrays to output the following string: "Hello exam 2"
 //Answer in this format: array_name[index] array_name[index] etc...
//
//char a[5] = {'a', 'e', 'i', 'o', 'u'};
//int b[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
//char c[6] = {'h', 't', 'L', 'H', 'k', ' '};
//char d[5] = {c[1]+b[3], c[1], c[0]+b[3], c[4]+b[1], c[4]};
//
//Answer: c[3] a[1] d[2] d[2] a[3] c[5] a[1] d[0] a[0] d[3] c[5] b[1]
//
//
//Name of Contributor: Owen Lopez
//Topic: Array
//Difficulty: Hard
//Questions: Finish the given functions. The function "swap_arrays" should swap the values of each array between each other, & the function "sort_array" should perform selection sort ascending.
//
//#define SIZE 5
//void swap_arrays(int arrA[], int arrB[]);
//void sort_array(int arr[]);
//
//int main(void) {
    //int arrA[SIZE] = {4, 5, 2, 6, 88};
    //int arrB[SIZE] = {8, 3, 11, 1, 8};
//
    //swap_arrays(arrA, arrB);
//
    //sort_array(arrA);
    //sort_array(arrB);
//
    //return 0;
//}
//
//void swap_arrays(int arrA[], int arrB[]) {
    //
//}
//void sort_array(int arr[]) {
    //
//}
//
////Answer:
//void swap_arrays(int arrA[], int arrB[]) {
    //for (int i = 0; i < SIZE; i++) {
        //int tmp = arrA[i];
        //arrA[i] = arrB[i];
        //arrB[i] = tmp;
    //}
//}
//
//
//void sort_array(int arr[]) {
    //for (int i = 0; i < SIZE-1; i++) {
        //int minIdx = i;
//
        //for (int j = i+1; j < SIZE; j++) {
            //if (arr[j] < arr[minIdx]) minIdx = j;
        //}
//
        //int tmp = arr[i];
        //arr[i] = arr[minIdx];
        //arr[minIdx] = tmp;
    //}    
//}
//


//Name of Contributor: Owen Lopez
//Topic: Pointers
//Difficulty: Easy
//Question: Determine the type and value of each expression when evaluated:

//int a = 5;
//char b = 'd';
//char c[6] = {'H', 'e', 'l', 'l', 'o', '\n'};
//int d[5] = {0, 1, 2, 3, 5};
//int *e[4] = {&d[2], &d[1], &d[4], &d[3]};
//
//1. *(&b)
//2. *(c + *(&a))
//3. *(c + **(e + 2))

//Name of Contributor: Owen Lopez
//Topic: Pointers
//Difficulty: Easy
//Question: What is the output of the given program?

//int main(void) {
    //int arr[6] = {1, 2, 3, 4, 5, 6};
//
    //for (int i = 0; i < 6; i++) {
        //if (arr[i] % 2 == 0) {
            //printf("%d ", arr[i]);
        //} else if (arr[i] % 3 == 0) {
            //int num = *(arr + i + *(arr + i - 1));
            //printf("%d ", num);
        //} else {
            //int *num = &arr[i];
            //num += (i/-2);
            //printf("%d ", *num);
        //}
    //}
//
    //return 0;
//}

// Answer

//Name of Contributor: Owen Lopez
//Topic: Problem Solving
//Difficulty: Easy
//Question: What is the output of the given program? If there is an error, mark "error" & explain.

//#define SIZE 10
//
//int sum_even(int arr);
//
//int main(void) {
    //int arr[SIZE] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
//
    //int num = sum_even(arr); 
//
    //printf("%d\n", num);
    //
    //return 0;
//}
//
//int sum_even(int arr) {
    //int sum = 0;
//
    //for (int i = 0; i < SIZE; i++) {
        //if (arr[i] % 2 == 0) sum += arr[i];
    //} 
    //
    //return sum; 
//}
//
//Answer: Error, the function uses the incorrect call signature, it should be int arr[].


//Name of Contributor: Owen Lopez
//Topic: Problem Solving
//Difficulty: Hard
//Question: Complete the given program. It should divide an array into two smaller arrays of even numbers & odd numbers.

#define MAX_CAPACITY 20

// This function fills an array of size with random integers 0 <= N <= 100. You do not need to implement it.
int[] generate_random_array(int size);
int[] select_even(int arr[], int capacity);
int[] select_odd(int arr[], int capacity);

int main(void) {

    int arr[MAX_CAPACITY] = generate_random_array[MAX_CAPCITY];

    int even[MAX_CAPACITY] = select_even(arr, MAX_CAPCITY);
    int odd[MAX_CAPACITY] = select_odd(arr, MAX_CAPCITY);

    return 0;
}


int[] select_odd(int arr[], int capacity) {

}


int[] select_even(int arr[], int capacity) {

}

Answer

int[] select_odd(int arr[], int capacity) {
    int size = 0;

    int evens[MAX_CAPACITY];

    for (int i = 0; i < MAX_CAPACITY; i++) [
        if (arr[i] % 2 == 0) {
            evens[size] = arr[i];
            size++;
        }
    }

    return evens;
}


int[] select_even(int arr[], int capacity) {
    int size = 0;

    int odds[MAX_CAPACITY];

    for (int i = 0; i < MAX_CAPACITY; i++) [
        if (arr[i] % 2 != 0) {
            odds[size] = arr[i];
            size++;
        }
    }

    return odds;
}
