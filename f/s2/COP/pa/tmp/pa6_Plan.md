# Main
    Read # of commands
    Run a for loop for N times -> Event Loop

# Helper Functions

##    Cat *create_cat(Shelter *S, Char *name, char *breed, int age, int friendliness, int health)

    create Cat *c
    malloc for sizeof(cat)
    copy over the provided info
    
    give arrival_id from S->next_arrival_id then increment it
    give quarentine 0
    set key to 0

    return c

## void free_Cat(Cat *c)
        free(c->name);
        free(c->breed);
        free(c);

## void swapIndex(Shelter *S, int d, int s)
    int tmp = S->heap->arr[d];
   
    S->heap->arr[d] = S->heap->arr[s]; 
    S->heap->arr[s] = tmp;

## int insert_Heap(Shelter *S, Cat *c)
    if param's NULL return
    check if S->heap->size == S->heap->capacity, if so then return -1

    add c to S->heap->arr[S->heap->size]
    increment S->heap->size

    use percolate_up(S, S->heap->size-1) on cat
    return 0 for success.

##  void remove_from_heap(Shelter *S, int index)
        free_Cat(S->heap->arr[index]);

        S->heap->arr[index] = S->heap->arr[S->heap->size];

        (S->heap->size)--;

        percolate_down(S, index);
        percolate_up(S, index);

## void build_Heap(Shelter *S)
    compute leaf node int leaf = (s->heap->size/2) - 1

    while (leaf != -1)
        percolate_down(S, leaf);
        leaf--;

## void percolate_down(Shelter *S, int index)
    if param's NULL return
   
    compute childL (n * 2)+1
    compute childR (n * 2)+2

    if childL and childR are > S->heap->size return

    if childL < S->heap->size && childR > S->heap->size
        ADOPTION:
            if s->heap->arr[index]->key > s->heap->arr[childL]->key swap
            percolate_down(S, childL);
        TRIAGE: 
            if s->heap->arr[index]->key < s->heap->arr[childL]->key swap
            percolate_down(S, childL);

    ADOPTION:
        if S->heap->arr[childL]->key > S->heap->arr[childR]->key
            swap childL w/ index
            percolate_down(S, childL);
        else
            swap childR w/ index
            percolate_down(S, childR);
    TRIAGE: 
        if S->heap->arr[childL]->key < S->heap->arr[childR]->key
            swap childL w/ index
            percolate_down(S, childL);
        else
            swap childR w/ index
            percolate_down(S, childR);

## void percolate_up(Shelter *S, int index)
    if param's NULL return
   
    if index == 0 return

    compute parent (index/2)-1

    ADOPTION:
        if S->heap->arr[parent]->key < S->heap->arr[index]->key, then swap
        percolate_up(S, parent);
        else return
    TRIAGE: 
        if S->heap->arr[parent]->key > S->heap->arr[index]->key, then swap
        percolate_up(S, parent);
        else return
    
# Main Event Loop
    Read Command string:
        Allocate N length char array, read into array

    Switch operator to route commands.
    Inside switch cases will read whatever parameters & feed to commands
    Eventually program exit...

# Commands
    
## find_cat_index(const CatHeap *heap, const char *name)
    Have index start as 0
    Uses a for loop from 0 -> heap->size and compares heap->arr[i]->name to name w/strcmp
   If found update index var
    Return index 

## compute_adoption_key(const Cat *c, const Shelter *S)
    double base = (c->friendliness * 1.6) + (c->health * 1.1) - (S->age * 0.7);

    if strcmp S->breed == c->featured_breed then double mult = S->alpha
    else double mult = 1

    double adoption_key = (base) * (mult + -10e-6 * c->arrival_id);
    return adoption_key;

## compute_triage_key(const Cat *c)
    return (100 - c->health) * (2 + max(0, (c->age - 12))) * (1 - (0.05 * c->friendliness));

## recompute_all_keys_and_build(Shelter *S)
    linear walk through array running the correct function on each object (i < S->heap->size)

    run build_Heap(S)
    

## cmd_add(Shelter *S, const char *name, const char *breed, int age, int friendl, int health)
    if find_cat_index(S->heap, name) is not -1 print "Name <name> already exists\n" 

    Cat *c = create_cat(S, name, breed, age, friendliness, health)

    Compute key based on S->mode; either compute_adoption_key or compute_triage_key
    set c->key to key

    insert_heap(S, c);
    
## cmd_update(Shelter *S, const char *name, const char *field, int new_value)
    int index =  find_cat_index(S->heap, name)
    if find_cat_index(S->heap, name) is -1 print "Cat <name> not found\n" 
    
    have a switch statement for every value of field
    cannot update BREED spit out error message
    update S->heap->arr[index]->trait = new_value

    if AGE/FREINDLINESS/HEALTH then recompute_all_keys_and_build(S)
    print "Updated <name>: <FIELD>=<value>. Priority Adjusted.\n"

    if QUARANTINE then also print "Updated <name>: <QUARANTINE>=<0_or_1>\n"

    if unreconized print "Unknown field <FIELD>\n"

## cmd_remove(Shelter *S, const char *name)
    int index = find_cat_index(S->heap, name)
    if find_cat_index(S->heap, name) is -1 print "Cat <name> not found\n" 

    remove_from_heap(S, index)

    print "Removed <name>\n"

## cmd_peek(const Shelter *S)
    if S->heap->size == 0 print "No Cats available\n"

    Cat *c = S->heap->arr[0];

    print "TOP[<MODE>]: [<MODE>] (key=XX.YY, name=<name>, breed=<breed>, age=<age>, friend=<friendliness>, health=<health>)\n"

## cmd_serve(Shelter *S)
    if S->heap->size == 0 print "No Cats available\n"

    ADOPTION:
        run for loop over (i < S->heap->size):
            if not S->heap->arr[i]->quarantine then 
                print "Serve now: <name> (key=XX.YY, name=<name>, breed=<breed>, age=<age>, friend=<friendliness>, health=<health>)\n"        
                remove_from_heap(S, i);
                return
            else continue

        if loop ends then print "No adoptable cats available.\n"

        free_cat(c);
    TRIAGE:
        print "Serve now: <name> (key=XX.YY, name=<name>, breed=<breed>, age=<age>, friend=<friendliness>, health=<health>)\n"        
        remove_from_heap(S, 0);

## cmd_mode(Shelter *S, const char *mode_str)
    if strcpy mode_str to "ADOPTION" true then 
        S->mode = Mode.MODE_ADOPTION
        recompute_all_keys_and_build(S);
        print "Mode set to <MODE>. Rebuilding priorities...\n"
    else if strcpy mode_str to "TRIAGE" then
        S->mode = Mode.MODE_TRIAGE
        recompute_all_keys_and_build(S);
        print "Mode set to <MODE>. Rebuilding priorities...\n"
    else 
        print "Unkown mode <unknown>.\n"

## cmd_featured(Shelter *S, const char *breed, double alpha))

## cmd_print(const Shelter *S, int k)


