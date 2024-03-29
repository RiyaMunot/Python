'''Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice.
Perform the calculation and display the result.'''
def add(num1, num2):
    return "Addition is", num1 + num2

def sub(num1, num2):
    return "Subtraction is", num1 - num2

def mul(num1, num2):
    return "Multiplication is", num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Please Enter Valid Number.\n Error: Not Divisible by Zero"
    else:
        return "Division is", num1 / num2

condition = 'Y'
while condition.lower() != 'n':
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print("Choose one of these operators for Performing Arithmetic Operations:\n + for addition \n - for subtraction \n * for multiplication \n / for division")
    operation = input("Enter Operation You Want To Perform: ")
    # Operations
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = sub(num1, num2)
    elif operation == '*':
        result = mul(num1, num2)
    elif operation == '/':
        result = div(num1, num2)
    else:
        result = "Please Enter Correct Operation...."
    print(result)
    condition = input("Do you Still Want to continue?(Enter Y for Yes and N for no): ")
