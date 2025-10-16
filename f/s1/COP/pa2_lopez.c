#include <stdio.h>
/*
   COP3223C Fall 2025
   Programming Assignment 2
   Student Name: Owen Lopez
   File Name: pa2_lopez.c
   NOTE: I hereby certify that this submission is my original work.
   It was completed independently by me without unauthorized assistance.
   I affirm that all sources consulted have been properly acknowledged.
   No part of this work was copied or plagiarized from any other source/s.
*/

int main(void) {
    double watts, bill;

    // Some user input
    printf("Enter usage (kWh): ");
    scanf("%lf", &watts);
    
    // And its validation..
    if (watts < 0) {
        printf("Invalid Input\n");
        return 1;
    }

    // Calculating base bill - not dynamically :(
    if (watts > 500) {
        watts -= 500;
        bill += 0.3*watts;
        bill += 60;
    } else if (watts > 300) {
        watts -= 300;
        bill += 0.2*watts;
        bill += 20;
    } else if (watts > 100) {
        watts -= 100;
        bill += 0.1*watts;
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

