Employee* createEmployees(char names[][50], double *salaries, int empCount)
{
    
    // WRITE YOUR CODE HERE
    
    Employee *arr = malloc(sizeof(Employee) * empCount);    

    for (int i = 0; i < empCount; i++) {
        arr[i]->salary = salaries[i];

        arr[i]->name = malloc(sizeof(StringType));

        arr[i]->name->length = strlen(names[i]) + 1;
        char *str = malloc((strlen(names[i]) + 1) * sizeof(char));
        
        strcpy(str, names[i]);
        arr[i]->name->string = str;
    }

    return arr;
}
