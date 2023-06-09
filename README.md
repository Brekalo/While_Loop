# _Project Name:_ Through the use of a `while loop`, the program calculates the average of the numbers entered

> **Table of Contents:**
>
> - Project description
> - Code description

#### Project description:

The program is a simple calculator, provides users with an interactive way to enter numbers and calculate their average of entered numbers.
It prompts the user to enter numbers one by one, and it calculates the running average of the numbers entered so far. The user can continue entering numbers until they enter "-1", at which point the program terminates and displays the final average.

#### Code description:

1. The code begins by printing a message to introduce the calculator.
2. The `get_int` function is defined to handle user input. It takes a prompt as an argument and repeatedly prompts the user to enter a number until a valid integer is entered. If the input is not a valid integer, it catches the `ValueError` exception and displays an `error message`.
3. The `main` function is defined as the entry point of the program. 
- It initializes two variables, `numbering` and `total_entries`, to keep track of the number of inputs and the sum of the entered numbers, respectively.
- Inside the `main` function, there is a `while True` loop that continuously prompts the user to enter a number using the `get_int` function. The loop continues until the user enters `-1`.
- If the `user_input` is `equal to -1`, the loop breaks and the program continues to the next step.
- Otherwise, the `numbering` variable is `incremented` by `1` to count the new entry, and the `total_entries` variable is updated by adding the `user_input` value.
- After the user enters `-1` and breaks out of the loop, the code checks if `numbering is not equal to 0`. 
- If at least one number was entered, it calculates the average by dividing the `total_entries` by `numbering` and assigns it to the `average` variable. 
- The code displays the total number of entries and the calculated average if numbers were entered. Otherwise, it prints a message indicating that no numbers were entered.
- A "goodbye" message is printed at the end of the program, and it terminates.
- The `if __name__ == "__main__":` condition ensures that the `main` function is only executed when the script is run directly, not when it is imported as a module.