#include <stdio.h>

int main()
{

	char r_signal;
	int all_letters = 1;
	int uppercase_letters = 0;
	int count = 0;
    
    // Signals the beginning of the transmission //
	printf("BEGIN TRANSMISSION\n");
    
    // User enters desired character //
	printf("Enter Character: ");
	scanf(" %c", &r_signal);
    
    /* Keeps tracks of any uppercase letters present, keeps track of how many characters 
    were inserted and registers when the '#' is entered as a sign to stop running the program */
	
	while(r_signal != '#') {
		count++;
		if((r_signal >= 'A' && r_signal <= 'Z') || (r_signal >= 'a' && r_signal <= 'z')) {
			if(r_signal >= 'A' && r_signal <= 'Z') {
				uppercase_letters = 1;
			}
		}
		else {
			all_letters = 0;

		}
		printf("Enter Character: ");
		scanf(" %c", &r_signal);
	}
	
	// Displays the end of the transmission //
	printf("END TRANSMISSION\n\n");
    
    /* A summary of everything in the transmission from 
    the character count, if all inputs were english letters 
    exclusively and if any of the inputs were uppercase letters */
    
	printf("SUMMARY\n");

	printf("Character Count: %d\n", count);

    printf("all_letters: %d\n", all_letters);

	if(all_letters && count > 0) {
		printf("Recognized Signal: Yes\n");
	}
	else {
		printf("Recognized Signal: No\n");
	}

	if(uppercase_letters) {
		printf("Priority Signal: Yes\n");
	}
	else {
		printf("Priority Signal: No\n");
	}

	return 0;
}
