#include <stdio.h>
/*
   COP3223C Fall 2025
   Programming Assignment 1
   Student Name: Owen Lopez
   File Name: pa1_lopez.c
   NOTE: I hereby certify that this submission is my original work.
   It was completed independently by me without unauthorized assistance.
   I affirm that all sources consulted have been properly acknowledged.
   No part of this work was copied or plagiarized from any other source/s.
*/

int main(void) {
   int priceC, numC, priceP, numP, partySize;
    
   printf("==== RECEIPT ====\n");
   printf("Coffee price: ");
   scanf("%d", &priceC);
   printf("\n");
   printf("Number of coffees: ");
   scanf("%d", &numC);
   printf("\n");
   printf("Pastry price: ");
   scanf("%d", &priceP);
   printf("\n");
   printf("Number of pastries: ");
   scanf("%d", &numP);
   printf("\n");
   printf("Party size: ");
   scanf("%d", &partySize);
   printf("\n");

   printf("Total before tax: $ %d\n", (priceC*numC)+(priceP*numP));
   printf("Florida tax (6%%): $ %0.2f\n", ((priceC*numC)+(priceP*numP))*0.06);
   printf("Total with tax: $ %0.2f\n", ((priceC*numC)+(priceP*numP))*1.06);
   printf("For a party size of %d, each person pays: $ %.2f\n", partySize, (((((priceC*numC)+(priceP*numP))*(1.06)))/partySize));
   printf("=== THANK YOU ===\n");
}
