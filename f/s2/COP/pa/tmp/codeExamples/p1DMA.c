// Make sure to when summing, start base value at 0
// If you know the entire value at the beginning then save it the struct, do not try to compute
//  When asked to make an array of structs, it does not always have to be an array of struct pointers
// it can be a flat array.
// The correct way to catch a double is through "%lf"
// 
int main(void) {
    
    int n;
	scanf("%d", &n);

    Item *items = malloc(sizeof(Item) * n);
    cart->items = items;
    cart->totalPrice = 0;

    for (int i = 0; i < n; i++) {
        Item item;

        char buff[101];
        fscanf("%s", buff);

        Char *name = malloc((strlen(buff) + 1)*sizeof(char));
        strcpy(buff, name);

        item.name = name;

        scanf("%ld", &item.price);

        cart->items[i] = &item;  

        cart->itemCount++;

        cart->totalPrice += item.price;
    }

    return 0;
}
