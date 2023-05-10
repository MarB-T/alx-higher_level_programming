	Python if else loops functions
0-positive_or_negative.py: Checks if a randomly generated number is +ve or -ve
1-last_digit.py: Gets the last digit of a randomly generated number
2-print_alphabet.py: Prints ASCII alphabet in lowercase
3-print_alphabt.py: Prints lowercase ASCII characters except "q" and "e"
4-print_hexa.py: Prints numbers in decimal and hexadecimal from 0 to 98
5-print_comb2.py: Prints numbers 00-99 separated by comma and space
6-print_comb3.py: Prints all possible combinations of two digits without repetition
7-islower.py: Function to check if pass character is lowercase
8-uppercase.py: Fuction that prints a string in uppercase followed by new line
9-print_last_digit.py: function to print the last digit of a number
10-add.py: function to add two integers and return sum
11-pow.py: function that computes a to the power of b and return the value.
12-fizzbuzz.py: function that prints numbers 1 to 100 replacing multiples of 3 by Fizz and those of 5 by FizzBuzz
13-insert_number.c: Inserts a node in an ordered linked list
100-print_tebahpla.py: prints ASCII alphabet in reverse and alternating upper and lower cases
101-remove_char_at.py: function that creates a copy of the string, removing the character at the position n
102-magic_calculation.py: python funtion to do the same thing as bytecode bellow

	 Bytecode

3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
