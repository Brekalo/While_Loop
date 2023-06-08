
print("Calculator for calculating the average of entered numbers!\n")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Oops! No number were entered! Try again!")


def main():
    numbering = 0
    total_entries = 0

    while True:
        user_input = get_int("Enter any number:\n > ")

        if user_input == -1:
            break
        numbering += 1
        total_entries += user_input

    if numbering != 0:
        average = total_entries / numbering
        print(
            f"In total, {numbering} numbers have been entered and the average is {average:.2f}.\n")
    else:
        print("The negative number were entered!")

    print("Goodbye!\n")


if __name__ == "__main__":
    main()
