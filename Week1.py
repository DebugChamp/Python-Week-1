num1 = input("Enter the first number: "))
num2 = input("Enter the second number: "))
operation = input("Enter an operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
        result = num1 / num2
else:
    result = "Invalid"

print("Result:", result)
