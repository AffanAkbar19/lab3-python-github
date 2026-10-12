
def add(num1, num2):
   print(num1 + num2)

def sub(num1, num2):
   print(num1 - num2)

def mul(num1, num2):
    print(num1 * num2)

def div(num1, num2):
    try:
        print(num1 / num2)
    except ZeroDivisionError:
        print("Number cannot be divided by zero")

def fact(num1):
    x = num1
    for i in range(num1, 1, -1):
       x = x * (i - 1)
    print(f"Factorial of {num1} is", x)

def even_odd(num1):
    if num1 % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

def per(num1, num2):
    try:
        print((num1 / num2) * 100, "%")
    except ZeroDivisionError:
        print("Cannot calculate percentage with zero")

def prime(num1):
    cnt = 0
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            cnt += 1
    if cnt == 2:
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

while True:
    print("\nChoose Operation you want to execute:")
    print("1. Addition\n2. Subtraction\n3. Multiplication")
    print("4. Division\n5. Check if funtion is Even or Odd\n6. Calculate Percentage")
    print("7. Factorial\n8. Check Prime Number\n9. Exit")

    operation = int(input("Operation (1 to 9): "))

    if operation == 9:
        print("Calculator closed")
        break

    if operation in (1, 2, 3, 4, 6):
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
    elif operation in (5, 7, 8):
        num1 = int(input("Enter a number: "))

    if operation == 1:
        add(num1, num2)
    elif operation == 2:
        sub(num1, num2)
    elif operation == 3:
        mul(num1, num2)
    elif operation == 4:
        div(num1, num2)
    elif operation == 5:
        even_odd(num1)
    elif operation == 6:
        per(num1, num2)
    elif operation == 7:
        fact(num1)
    elif operation == 8:
        prime(num1)
    else:
        if operation not in range(1, 10):
            print("Invalid operation")

