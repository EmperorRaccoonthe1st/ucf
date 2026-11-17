1. We store the number within the _Credit Card_ struct as a string rather than an integer due to size constraints of the integer type in C.
A standard C integer can hold up to 10 digit long values, while a credit card number is 16 digits long.
Therefor you cannot store an entire credit card number in a single standard integer, and instead we utilize a string can hold an arbitrary amount of digits.

Additionally this decision allows for ease of access for single digits within the card.
Luhn's algorithm requires repeated access of an arbitrary single digit, a process when implemented on an integer uses a series of verbose mathematical manipulations.
It is simpler to store the number as a string & access each digit using an index, completely bypassing the mathematical manipulations required of the former solution.

2. The variable described named `card` is a `CreditCard` struct saved in memory.
This struct has three members: an `int` month, an `int` year, & and `int` array char[].
The assignment instructs us to allocate each struct within the main function and insert the information from a file into it, and within each function the struct is _passed by value_.
As a result, within the our function and in the main function we are accessing the structure directly.

To directly access the contents of a struct we use the _dot operator_ (`.`), like so:
```c
card.number;
card.month;
card.year;
```

If we were to instead access the struct through a pointer we would utilize the _arrow operator_ (`->`).

3. **No**, it does not.
 When _passing a structure by value_ C creates a copy of the struct and provides it to the function.
This copy is a completely different object in memory, residing further down in the _function call stack_.
If the function did alter this copy then the change would not affect the original in any capacity.
When the function returns, all memory held within the _function stack frame_ is released, which removes all changes to the copy of the struct which occurred during the execution of the function.

4. **No**, it cannot.
The function receives the struct through _pass-by-value_ in the standard manner, but if the `const` keyword is applied to the parameter the copied struct becomes immutable.
As the local copy of the struct within the _function stack frame_ is now immutable, each member within the struct is now immutable as well.
You are unable to reassign nor alter an variable that is immutable, and attempting to do so will result in a compilation error.
Thus assigning a new value to `card.month` or changing a character in `card.number` becomes impossible as long at the struct `card` is immutable.

5. A credit card expires when the current date is greater than the month and year marked on the back of the card.
To check a date in this manner requires comparing both the month and the year to the one listed.
Only checking a single value would result in an incomplete comparison.
For example with the following values:

- Current Date: 7-09-2026
- Expiration: 8-2025

Only checking the month in this scenario would result in a false positive.
Even though the expiration month is greater than the current month, it's actually an entire year behind and the card has been expired **for a whole year**.

6. This calculation functions identically to the familiar `alpha - 'a'` equation that we use to find the offset of characters within the alphabet.
Each numeric character utilizes an _ASCII Code_ when represented as `char`.
The series of numeric characters begins with '0' and runs until the character '9', so the first character '0' has an offset of 0 and every following numeric character increases their offset by 1.
In this manner, each character has an offset that directly maps to their numeric value.

When attempting to find the offset, or numeric value, of the character '7' we find the difference between that 'char' and the first object in the sequence, '0'.
Thus the calculation '7':55 - '0':48 = 7.

7. The _dot_ operator accesses the value of a member in a certain struct, it does not return the address of that member in memory.
As `fscanf()` requires addresses to locations in memory to store file input, the members receiving data must utilize the _address-of_ operator to conform the requirements of the function.

In our program we attempt to place two integers from the input file into the members `c.month` and `c.year`, both of these evaluate to their integer value when accessed through the _dot_ operator and thus require the use of the _address-of_ operator.

Within `fscanf()` the `c.number` member also evaluates to the value stored in memory, which is a pointer to the first element of the number character array.
The `c.number` member automatically decays to a pointer to the first element within the numbers array, and therefore there is no need to utilize the _address-of_ operator when attempting to place input into it.
