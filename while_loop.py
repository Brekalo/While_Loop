
print("Calculator for calculating the average of entered numbers!")

# this variable will be used as a stopping point for the loop later in the code
stop_num = -1

# these two variables to keep track of the number of times the loop has executed (numbering) and the sum of all the entered numbers (total_entries)
numbering = 0
total_entries = 0

# ask the user to enter a number
enter_num = int(input("Enter any number:\n > "))

# while loop will continue to execute as long as the value of enter_num is not equal to stop_num
while enter_num != stop_num:
    # numbering variable is incremented by 1
    # the total_entries variable is updated to include the new enter_num value
    # user is prompted to enter another number, which is then assigned to enter_num
    numbering += 1
    total_entries += enter_num
    enter_num = int(input("Enter another number:\n > "))

# if numbering is 0, then no numbers were entered, and a message is printed
if numbering == 0:
    print("No numbers were entered!")

else:
    # if numbering is not equal to 0, the average of the entered numbers is calculated by dividing the total_entries by the numbering, and the result/message is printed
    average = total_entries / numbering
    print(f"In total, {numbering} numbers have been entered and the average is {average:.2f}.")
 