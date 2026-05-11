typedef struct Employee
{
    char *first; // Employee's first name.
    char *last;  // Employee's last name.
    int ID;      // Employee ID.
} Employee;

Employee *makeArray(char **firstNames, char **lastNames, int *IDs, int n)
{
    int i;
    Employee *array = malloc(sizeof(Employee) * n);

    for (i = 0; i < n; i++)
    {
        array[i].first = malloc((strlen(firstNames[i])+1) * sizeof(char));
        array[i].last = malloc((strlen(lastNames[i])+1) * sizeof(char));

        strcpy(array[i].first, firstNames[i]);
        strcpy(array[i].last, lastNames[i]);
        array[i].ID = IDs[i];
    }

    return array;
}

// Write the function that takes a pointer to the array created by the makeArray() function, 
// along with the number of employee records in that array (n) and frees all the dynamically allocated
// memory associated with that array. The function signature is as follows:

void freeEmployeeArray(Employee *array, int n)
{
    
    // WRITE YOUR CODE HERE
    
    for (int i = 0; i < n; i++) {
        free(array[i].first);
        free(array[i].last);
    }

    free(array);
}
