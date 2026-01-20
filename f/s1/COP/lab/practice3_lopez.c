#include <stdio.h>
#include <ctype.h>


int main(void) {
    int inputAmt;
    
    scanf("%d", &inputAmt);
    
    for (int i = 0; i < inputAmt; i++) {
        char alpha;
        scanf(" %c", &alpha);
        if (tolower(alpha) < 97 || tolower(alpha) > 122) {
            printf("%d: Invalid\n", i);
            continue;
        } 
        printf("%d: %d\n", i+1, tolower(alpha) - 96);
    }
    return 0;
}
