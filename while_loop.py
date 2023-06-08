
print("Calculator for calculating the average of entered numbers!")

# variables
numbering = 0
total_entries = 0

# while loop repetition structure until user enters -1
while True:
    enter_num = int(input("Enter any number:\n > "))

    # if the user entered -1, the loop will be terminated using the break statement
    if enter_num == -1:
        break

    # update variables
    numbering += 1
    total_entries += enter_num

# calculating the average, and then a message is printed
if numbering > 0:
    average = total_entries / numbering
    print(
        f"In total, {numbering} numbers have been entered and the average is {average:.2f}.")

# if user has not entered any numbers, a message is printed
else:
    print("The negative number or no numbers were entered!")
