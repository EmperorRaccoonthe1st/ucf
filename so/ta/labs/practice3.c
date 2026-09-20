#include <stdio.h>

int main(void) {
    char resp;
    int age;
    int cost = 0;
    int is_weekday = 0;

    printf("Enter Age: ");
    scanf("%d", &age);

    if (age <= 12) {
        cost = 40;    
    } else if (age <= 64) {
        cost = 60;
    } else {
        cost = 45;
    }

    printf("Weekend: ");
    scanf(" %c", &resp);

    if (resp == 'Y') {
        cost += 10;
    } else {
        cost += 5;
        is_weekday = 1;
    }
    
    printf("Meal Plan: ");
    scanf(" %c", &resp);

    if (resp == 'Y') {
        cost += 25;
    } 

    printf("Parking Pass: ");
    scanf(" %c", &resp);

    if (resp == 'Y') {
        cost += 20;
    } 

    if (age >= 18) {
        printf("VIP Upgrade: ");
        scanf(" %c", &resp);

        if (resp == 'Y') {
            cost += 30;
        }
    } else {
        printf("VIP Upgrade Unavailable\n");
    }

    printf("Student: ");
    scanf(" %c", &resp);

    if (is_weekday && resp == 'Y') {
        cost -= 5;
    }

    printf("Cost: $%d\n", cost);

    return 0;
}
