/* COP 3502C PA6
This program is written by: Owen Manuel Lopez */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INPUT_FILE "adopt.txt"

typedef enum { 
    MODE_ADOPTION = 0,
    MODE_TRIAGE   = 1
} Mode;

typedef struct Cat {
    char *name;
    char *breed;
    int age;
    int friendliness;
    int health;
    int arrival_id;
    int quarantine;
    double key;
} Cat;

typedef struct {
    Cat **arr;
    int size;
    int capacity;
    Mode mode;
} CatHeap;

typedef struct {
    Mode mode;
    char *featured_breed;
    double alpha;
    int next_arrival_id;
    CatHeap heap;
} Shelter;

// Function Prototypes
void myMain(FILE *f);
Cat *create_Cat(char *name, char *breed, int age, int friend, int health, int arrival_id);
void free_Cat(Cat *c);
Shelter *create_Shelter();
void free_Shelter(Shelter *s);
CatHeap create_CatHeap(int capacity);
void free_CatHeap(CatHeap *h);
int find_cat_index(CatHeap *h, char *name);
double compute_adoption_key(Cat *c, Shelter *s);
double compute_triage_key(Cat *c);
int isBetter(Cat *c1, Cat *c2, Mode m);
void percolate_up(CatHeap *h, int i);
void percolate_down(CatHeap *h, int i);
void recompute_all_keys_and_build(Shelter *s);
void cmd_add(Shelter *s, char *name, char *breed, int age, int friend, int health);
void cmd_update(Shelter *s, char *name, char *field, int num);
void cmd_remove(Shelter *s, char *name);
void cmd_peek(Shelter *s);
void cmd_serve(Shelter *s);
void cmd_mode(Shelter *s, char *mode_name);
void cmd_featured(Shelter *s, char *breed, double alpha);
void cmd_print(Shelter *s, int k);

#ifndef MAIN_FUNCTION
int main(void) {
    FILE *f = fopen(INPUT_FILE, "r");
    if (f == NULL) {
        printf("File Does Not Exist!\n");
        return 1;
    }
    myMain(f);
    fclose(f);
    return 0;
}
#endif

void myMain(FILE *f) {
    int n, i;
    char cmd[256];
    Shelter *s;
    
    s = create_Shelter();

    if (fscanf(f, "%d", &n) != 1) {
        free_Shelter(s);
        return;
    }

    for (i = 0; i < n; i++) {
        if (fscanf(f, "%s", cmd) != 1) break;

        int cmd_type = 0;
        if (strcmp(cmd, "ADD") == 0) cmd_type = 1;
        else if (strcmp(cmd, "UPDATE") == 0) cmd_type = 2;
        else if (strcmp(cmd, "REMOVE") == 0) cmd_type = 3;
        else if (strcmp(cmd, "PEEK") == 0) cmd_type = 4;
        else if (strcmp(cmd, "SERVE") == 0) cmd_type = 5;
        else if (strcmp(cmd, "MODE") == 0) cmd_type = 6;
        else if (strcmp(cmd, "FEATURED") == 0) cmd_type = 7;
        else if (strcmp(cmd, "PRINT") == 0) cmd_type = 8;
        else if (strcmp(cmd, "QUIT") == 0) cmd_type = 9;

        switch (cmd_type) {
            case 1: {
                char name[256], breed[256];
                int age, friend, health;
                fscanf(f, "%s %s %d %d %d", name, breed, &age, &friend, &health);
                cmd_add(s, name, breed, age, friend, health);
                break;
            }
            case 2: {
                char name[256], field[256];
                int num;
                fscanf(f, "%s %s %d", name, field, &num);
                cmd_update(s, name, field, num);
                break;
            }
            case 3: {
                char name[256];
                fscanf(f, "%s", name);
                cmd_remove(s, name);
                break;
            }
            case 4:
                cmd_peek(s);
                break;
            case 5:
                cmd_serve(s);
                break;
            case 6: {
                char mode_name[256];
                fscanf(f, "%s", mode_name);
                cmd_mode(s, mode_name);
                break;
            }
            case 7: {
                char breed[256];
                double alpha;
                fscanf(f, "%s %lf", breed, &alpha);
                cmd_featured(s, breed, alpha);
                break;
            }
            case 8: {
                int k;
                fscanf(f, "%d", &k);
                cmd_print(s, k);
                break;
            }
            case 9:
                i = n; 
                break;
            default:
                break;
        }
        if (cmd_type == 9) break;
    }
    
    free_Shelter(s);
}

// Function Definitions
int find_cat_index(CatHeap *h, char *name) {
    int val = 0;
    for (int i = 0; i < h->size; i++) {
        int tmp = strcmp(h->arr[i]->name, name);
        if (tmp == 0) {
            val = i;
            return val;
        }
    }
    val = -1;
    return val;
}

double compute_adoption_key(Cat *c, Shelter *s) {
    double y, val;
    double x = 1.6 * c->friendliness;
    x = x + 1.1 * c->health;
    x = x - 0.7 * c->age;
    y = 1.0;
    if (s->featured_breed != NULL) {
        int tmp = strcmp(c->breed, s->featured_breed);
        if (tmp == 0) {
            y = s->alpha;
        }
    }
    val = x * y;
    val = val - 0.000001 * c->arrival_id;
    return val;
}

double compute_triage_key(Cat *c) {
    double val, x, y;
    x = c->age - 12;
    if (x < 0) {
        x = 0;
    }
    y = 100 - c->health;
    val = y * 2.0;
    val = val + x * 1.0;
    val = val - 0.05 * c->friendliness;
    return val;
}

int isBetter(Cat *c1, Cat *c2, Mode m) {
    int tmp;
    int val = 0;
    if (m == MODE_ADOPTION) {
        if (c1->key > c2->key + 0.0000001) {
            val = 1;
            return val;
        } else if (c2->key > c1->key + 0.0000001) {
            val = 0;
            return val;
        }
    } else {
        if (c1->key < c2->key - 0.0000001) {
            val = 1;
            return val;
        } else if (c1->key > c2->key + 0.0000001) {
            val = 0;
            return val;
        }
    }
    
    tmp = strcmp(c1->name, c2->name);
    if (tmp < 0) {
        val = 1;
        return val;
    } else if (tmp > 0) {
        val = 0;
        return val;
    } else {
        if (c1->arrival_id < c2->arrival_id) {
            val = 1;
            return val;
        } else {
            val = 0;
            return val;
        }
    }
}

void percolate_up(CatHeap *h, int i) {
    if (i == 0) {
        return;
    }
    
    int tmp;
    int parent = (i - 1) / 2;
    tmp = isBetter(h->arr[i], h->arr[parent], h->mode);
    
    if (tmp == 1) {
        Cat *c = h->arr[i];
        h->arr[i] = h->arr[parent];
        h->arr[parent] = c;
        percolate_up(h, parent);
    }
}

void percolate_down(CatHeap *h, int i) {
    int x, y, val, tmp;
    x = 2 * i + 1;
    y = 2 * i + 2;
    val = i;
    
    if (x < h->size) {
        tmp = isBetter(h->arr[x], h->arr[val], h->mode);
        if (tmp == 1) {
            val = x;
        }
    }
    
    if (y < h->size) {
        tmp = isBetter(h->arr[y], h->arr[val], h->mode);
        if (tmp == 1) {
            val = y;
        }
    }
    
    if (val != i) {
        Cat *c = h->arr[i];
        h->arr[i] = h->arr[val];
        h->arr[val] = c;
        percolate_down(h, val);
    }
}

void recompute_all_keys_and_build(Shelter *s) {
    int i;
    for (i = 0; i < s->heap.size; i++) {
        double val;
        if (s->mode == MODE_ADOPTION) {
            val = compute_adoption_key(s->heap.arr[i], s);
        } else {
            val = compute_triage_key(s->heap.arr[i]);
        }
        s->heap.arr[i]->key = val;
    }
    for (i = (s->heap.size / 2) - 1; i >= 0; i--) {
        percolate_down(&(s->heap), i);
    }
}

void cmd_add(Shelter *s, char *name, char *breed, int age, int friend, int health) {
    int i;
    i = find_cat_index(&(s->heap), name);
    if (i != -1) {
        printf("Name %s already exists.\n", name);
        return;
    }
    
    Cat *c = create_Cat(name, breed, age, friend, health, s->next_arrival_id);
    s->next_arrival_id = s->next_arrival_id + 1;
    
    double val;
    if (s->mode == MODE_ADOPTION) {
        val = compute_adoption_key(c, s);
    } else {
        val = compute_triage_key(c);
    }
    c->key = val;
    
    if (s->heap.size == s->heap.capacity) {
        s->heap.capacity = s->heap.capacity * 2;
        s->heap.arr = realloc(s->heap.arr, sizeof(Cat *) * s->heap.capacity);
    }
    s->heap.arr[s->heap.size] = c;
    s->heap.size = s->heap.size + 1;
    percolate_up(&(s->heap), s->heap.size - 1);
    printf("Added %s.\n", name);
}

void cmd_update(Shelter *s, char *name, char *field, int num) {
    int i, val, tmp;
    i = find_cat_index(&(s->heap), name);
    if (i == -1) {
        printf("Cat %s not found.\n", name);
        return;
    }
    Cat *c = s->heap.arr[i];
    val = 0;
    tmp = strcmp(field, "AGE");
    if (tmp == 0) {
        c->age = num;
        val = 1;
    } else {
        tmp = strcmp(field, "FRIEND");
        if (tmp == 0) {
            c->friendliness = num;
            val = 1;
        } else {
            tmp = strcmp(field, "HEALTH");
            if (tmp == 0) {
                c->health = num;
                val = 1;
            } else {
                tmp = strcmp(field, "QUARANTINE");
                if (tmp == 0) {
                    c->quarantine = num;
                    percolate_up(&(s->heap), i);
                    percolate_down(&(s->heap), i);
                    printf("Updated %s: QUARANTINE=%d.\n", name, num);
                    return;
                } else {
                    printf("Unknown field %s.\n", field);
                    return;
                }
            }
        }
    }
    
    if (val == 1) {
        double y;
        if (s->mode == MODE_ADOPTION) {
            y = compute_adoption_key(c, s);
        } else {
            y = compute_triage_key(c);
        }
        c->key = y;
        percolate_up(&(s->heap), i);
        i = find_cat_index(&(s->heap), name);
        percolate_down(&(s->heap), i);
        printf("Updated %s: %s=%d. Priority adjusted.\n", name, field, num);
    }
}

void cmd_remove(Shelter *s, char *name) {
    int i;
    i = find_cat_index(&(s->heap), name);
    if (i == -1) {
        printf("Cat %s not found.\n", name);
        return;
    }
    Cat *c = s->heap.arr[i];
    s->heap.arr[i] = s->heap.arr[s->heap.size - 1];
    s->heap.size = s->heap.size - 1;
    if (i < s->heap.size) {
        percolate_up(&(s->heap), i);
        percolate_down(&(s->heap), i);
    }
    free_Cat(c);
    printf("Removed %s.\n", name);
}

void cmd_peek(Shelter *s) {
    if (s->heap.size == 0) {
        printf("No cats available.\n");
        return;
    }
    Cat *c = s->heap.arr[0];
    char *type;
    if (s->mode == MODE_ADOPTION) {
        type = "ADOPTION";
    } else {
        type = "TRIAGE";
    }
    printf("Top[%s]: [%s] (key=%.2f, name=%s, breed=%s, age=%d, friend=%d, health=%d)\n",
        type, type, c->key, c->name, c->breed, c->age, c->friendliness, c->health);
}

void cmd_serve(Shelter *s) {
    if (s->heap.size == 0) {
        printf("No cats available.\n");
        return;
    }
    if (s->mode == MODE_ADOPTION) {
        Cat **tmp = malloc(sizeof(Cat *) * s->heap.size);
        int amt = 0;
        int val = 0;
        while (s->heap.size > 0) {
            Cat *c = s->heap.arr[0];
            if (c->quarantine == 1) {
                tmp[amt] = c;
                amt = amt + 1;
                s->heap.arr[0] = s->heap.arr[s->heap.size - 1];
                s->heap.size = s->heap.size - 1;
                percolate_down(&(s->heap), 0);
            } else {
                printf("Serve now: %s (key=%.2f, name=%s, breed=%s, age=%d, friend=%d, health=%d)\n",
                    c->name, c->key, c->name, c->breed, c->age, c->friendliness, c->health);
                s->heap.arr[0] = s->heap.arr[s->heap.size - 1];
                s->heap.size = s->heap.size - 1;
                percolate_down(&(s->heap), 0);
                free(c->name);
                free(c->breed);
                free(c);
                val = 1;
                break;
            }
        }
        if (val == 0) {
            printf("No adoptable cats available.\n");
        }
        int i;
        for (i = 0; i < amt; i++) {
            if (s->heap.size == s->heap.capacity) {
                s->heap.capacity = s->heap.capacity * 2;
                s->heap.arr = realloc(s->heap.arr, sizeof(Cat *) * s->heap.capacity);
            }
            s->heap.arr[s->heap.size] = tmp[i];
            s->heap.size = s->heap.size + 1;
            percolate_up(&(s->heap), s->heap.size - 1);
        }
        free(tmp);
    } else {
        Cat *c = s->heap.arr[0];
        printf("Serve now: %s (key=%.2f, name=%s, breed=%s, age=%d, friend=%d, health=%d)\n",
            c->name, c->key, c->name, c->breed, c->age, c->friendliness, c->health);
        s->heap.arr[0] = s->heap.arr[s->heap.size - 1];
        s->heap.size = s->heap.size - 1;
        percolate_down(&(s->heap), 0);
        free(c->name);
        free(c->breed);
        free(c);
    }
}

void cmd_mode(Shelter *s, char *mode_name) {
    int tmp;
    tmp = strcmp(mode_name, "ADOPTION");
    if (tmp == 0) {
        s->mode = MODE_ADOPTION;
        s->heap.mode = MODE_ADOPTION;
        recompute_all_keys_and_build(s);
        printf("Mode set to ADOPTION. Rebuilding priorities...\n");
    } else {
        tmp = strcmp(mode_name, "TRIAGE");
        if (tmp == 0) {
            s->mode = MODE_TRIAGE;
            s->heap.mode = MODE_TRIAGE;
            recompute_all_keys_and_build(s);
            printf("Mode set to TRIAGE. Rebuilding priorities...\n");
        } else {
            printf("Unknown mode %s.\n", mode_name);
        }
    }
}

void cmd_featured(Shelter *s, char *breed, double alpha) {
    int tmp;
    tmp = strcmp(breed, "NONE");
    if (tmp == 0) {
        if (s->featured_breed != NULL) {
            free(s->featured_breed);
            s->featured_breed = NULL;
        }
        s->alpha = 1.0;
        recompute_all_keys_and_build(s);
        printf("Featured breed cleared. Rebuilding priorities...\n");
    } else {
        if (s->featured_breed != NULL) {
            free(s->featured_breed);
        }
        int amt;
        amt = strlen(breed) + 1;
        s->featured_breed = malloc(amt);
        strcpy(s->featured_breed, breed);
        s->alpha = alpha;
        recompute_all_keys_and_build(s);
        printf("Featured breed set to %s with alpha=%.2f. Rebuilding priorities...\n", breed, alpha);
    }
}

void cmd_print(Shelter *s, int k) {
    if (s->heap.size == 0) {
        printf("No cats available.\n");
        return;
    }
    CatHeap h_tmp;
    int i, n;
    h_tmp.size = s->heap.size;
    h_tmp.capacity = s->heap.size;
    h_tmp.mode = s->heap.mode;
    h_tmp.arr = malloc(sizeof(Cat *) * h_tmp.size);
    for (i = 0; i < h_tmp.size; i++) {
        h_tmp.arr[i] = s->heap.arr[i];
    }
    
    n = k;
    if (h_tmp.size < n) {
        n = h_tmp.size;
    }
    
    for (i = 0; i < n; i++) {
        Cat *c = h_tmp.arr[0];
        char *type;
        if (h_tmp.mode == MODE_ADOPTION) {
            type = "ADOPTION";
        } else {
            type = "TRIAGE";
        }
        printf("[%d] %s (key=%.2f, %s)\n", i + 1, c->name, c->key, type);
        h_tmp.arr[0] = h_tmp.arr[h_tmp.size - 1];
        h_tmp.size = h_tmp.size - 1;
        percolate_down(&h_tmp, 0);
    }
    free(h_tmp.arr);
}


Cat *create_Cat(char *name, char *breed, int age, int friend, int health, int arrival_id) {
    Cat *c = malloc(sizeof(Cat));
    int amt;

    amt = strlen(name) + 1;
    c->name = malloc(amt);
    strcpy(c->name, name);
    
    amt = strlen(breed) + 1;
    c->breed = malloc(amt);
    strcpy(c->breed, breed);
    
    c->age = age;
    c->friendliness = friend;
    c->health = health;
    c->arrival_id = arrival_id;
    c->quarantine = 0;
    c->key = 0.0;
    
    return c;
}

void free_Cat(Cat *c) {
    if (c == NULL) return;
    free(c->name);
    free(c->breed);
    free(c);
}

CatHeap create_CatHeap(int capacity) {
    CatHeap h;
    h.size = 0;
    h.capacity = capacity;
    h.arr = malloc(sizeof(Cat *) * h.capacity);
    h.mode = MODE_ADOPTION;
    return h;
}

void free_CatHeap(CatHeap *h) {
    int i;
    for (i = 0; i < h->size; i++) {
        free_Cat(h->arr[i]);
    }
    free(h->arr);
}

Shelter *create_Shelter() {
    Shelter *s = malloc(sizeof(Shelter));
    s->mode = MODE_ADOPTION;
    s->featured_breed = NULL;
    s->alpha = 1.0;
    s->next_arrival_id = 0;
    s->heap = create_CatHeap(10);
    return s;
}

void free_Shelter(Shelter *s) {
    if (s == NULL) return;
    free_CatHeap(&(s->heap));
    if (s->featured_breed != NULL) {
        free(s->featured_breed);
    }
    free(s);
}
