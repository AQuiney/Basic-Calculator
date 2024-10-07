# Calculation functions
def addition(num_1, num_2):    
    answer = num_1 + num_2
    print(f"{num_1} + {num_2} = {answer}")

def multiply(num_1, num_2):    
    answer = num_1 * num_2
    print(f"{num_1} X {num_2} = {answer}")

def divide(num_1, num_2):    
    while True:
        try:
            if num_2 == 0:
                raise ValueError("Cannot divide by 0.")
            answer = num_1 / num_2
            print(f"{num_1} / {num_2} = {answer}") 
            break 
        except ValueError:
            num_2 = int(input("Cannot divide by 0, try again: "))
    
def minus(num_1, num_2):    
    answer = num_1 - num_2
    print(f"{num_1} - {num_2} = {answer}")


# Program starts here
def main():    
    # Ask for calculation type
    user_choice = str(input("What type of calculation would you like to do? +, -, X, or /?: "))   
    
    # Infinitely loops when the input isn't exactly equal to one of the items in the list
    while user_choice not in ["+", "-", "x", "X", "/"]:            
            user_choice = str(input("Invalid input, please enter one of the following: +, -, X, or /: "))
            
    # Once input does match an item in the list, while loop ends
    
    # Ask for first number
    num_1 = input("Enter the first number: ")
    
    # Loops while num_1 is not a valid input
    while True:
        try:
            num_1 = int(num_1)
            break
        except ValueError:
            num_1 = input("Please enter a valid number: ")
            
    # Once num_1 is valid, continue        
            
    # Ask for the second number
    num_2 = input("Enter the second number: ") 

    # Loops while num_2 not a valid input
    while True:
        try:
            num_2 = int(num_2)
            break
        except ValueError:
            num_2 = input("Please enter a valid number: ")

    # Once num_2 is valid, continue
            
    # Assigns user_choice to one of the calculation functions and runs it
    if user_choice == "+":
        addition(num_1, num_2)
    elif user_choice == "-":
        minus(num_1, num_2)
    elif user_choice == "x" or user_choice == "X":
        multiply(num_1, num_2)
    elif user_choice == "/":
        divide(num_1, num_2)

main()