#include <stdio.h>

struct Block {
    double rate;
    int size;
};

int main(void) {
    struct Block blocks[4] = {
        {0, 100},
        {0.1, 200},
        {0.2, 200},
        {0.3, 150},
    };
    double watts, bill;

    // Some user input
    printf("Enter Usage (kWh): ");
    scanf("%lf", &watts);

    // And its validation..
    if (watts < 0) {
        printf("Invalid Input\n");
        return 1;
    }
    
    // Calculating base bill - dynamically!
    for (int i = 0; i < sizeof(blocks)/sizeof(blocks[0]); i++) {
        if (watts > blocks[i].size) {
            watts -= blocks[i].size;
            bill += blocks[i].size*blocks[i].rate;
        } else {
            bill += watts*blocks[i].rate;
            break;
        }
    }
    
     printf("Base bill: $%.2f\n", bill);
    
    // Calculating Surcharge
    if (bill > 100) {
        printf("Surcharge (10%%): $%.2f\n", bill*0.1);
        bill += bill*0.1;
    }
    
    printf("Final bill: $%.2f\n", bill);
    
    return 0;
}
