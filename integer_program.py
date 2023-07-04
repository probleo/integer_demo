"""5.2 Write a program that repeatedly prompts a user for integer numbers 
until the user enters 'done'. Once 'done' is entered, 
print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it 
with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below."""


# create an empty list where the user input will be stored.
num_list = []

while True:
    userNumber = input("Please enter a number. \nType 'Done' if you want to stop: ")
    if userNumber == 'Done':
         break
    try:
        userNumberint = int(userNumber)
    except:
        print("Invalid input.")
        continue

    # the user's input will be appended in num_list.    
    if userNumberint > 0:
        num_list.append(userNumberint)
    else:
        continue

# Added an if statement to check if the list is empty.
if bool(num_list):   
    # If the list is not empty, print the max and min numbers.
    print(f"Maximum is {max(num_list)}")
    print(f"Minimum is {min(num_list)}")
# If the list is empty, run the below code.
else:
    print("\nPlease type some numbers.")
