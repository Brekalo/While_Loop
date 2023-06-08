# _Project Name:_ While Loop

<sub>THE PROGRAMME CALCULATES THE AVERAGE OF THE NUMBERS ENTERED</sub>

> **Table of Contents:**
>
> - Project description
> - Code description

Project description:
The program provides users with an interactive way to enter numbers and calculate their averages.
It prompts the user to enter numbers one by one, and after each entry, it calculates the running average of the numbers entered so far. The user can continue entering numbers until they enter `-1`, at which point the program terminates and displays the final average.
This program provides a simple and interactive way for users to enter numbers and calculate their average of entered numbers.

Code description:

1. The code begins by printing a message to introduce the calculator.
2. The `get_int` function is defined, which takes a prompt as input and repeatedly asks the user for input until a valid integer is entered. If a non-integer value is entered, it displays an `error` message and prompts again.
3. The `main` function is defined, which serves as the entry point of the program.

- Inside the main function, two variables are initialized: `numbering` to keep track of the number of entries and `total_entries` to keep track of the sum of all entered numbers.
- The program enters a while loop that continues indefinitely until the user enters `-1`.
- Inside the loop, the `get_int` function is called to prompt the user for a number, and the returned value is stored in the `user_input` variable.
- If the `user_input is `equal`to`-1`, the loop breaks and the program continues to the next step.
- Otherwise, the `numbering` variable is incremented by `1` to count the new entry, and the total_entries variable is updated by adding the `user_input` value.
- After the loop, the code checks if any numbers were entered by comparing `numbering` to `0`.
- If at least one number was entered, it calculates the average by dividing the `total_entries` by `numbering` and assigns it to the `average` variable. It then prints a message displaying the total number of entries and the calculated average.
- If no numbers were entered (i.e., `numbering` is `0`), it prints a message indicating that a negative number was entered.
- A goodbye message is printed at the end of the program, and it terminates.
