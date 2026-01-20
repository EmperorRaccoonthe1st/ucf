#include <stdio.h>
#include <string.h>

#define MAX_LEN 101

typedef struct Card_s {
  int value;  
  char suit[MAX_LEN];
} Card;

void print_card(Card *c);

int main(void) {
    Card exampleCard;

    exampleCard.value = 3;
    strcpy(exampleCard.suit, "Spade");

    print_card(&exampleCard);
    
    return 0;
}


void print_card(Card *c) {
    printf("%d %s\n", c->value, c->suit);
}
