#include <stdio.h>

int main(void) {
    int numa, r, r1;
    int numb = 0; 
    
    printf("Enter Number: ");
    scanf("%d", &numa);
     
    if (numa < 100 || numa > 999) {
         printf("Invalid Input\n");
         return 1;
    }

    // Flipping the numbers..
    //Get last 2 digits 
    r = (numa)-((numa/100)*100);
    //Get 3rd digit
    r1 = (r)-((r/10)*10);
    numb += 100*r1;
    // And there goes the 2nd
    numb += r-r1;
    // Get 1st digit
    numb += numa/100;

    printf("Reversed: %d\n", numb);
    printf("Sum: %d\n", numb+numa);

    printf("Hidden Code: %c%c%c\n", (char)(r1+65), (char)(((r-r1)/10)+65), (char)((numa/100)+65));
     
    return 0;
}
