def calculate (num1, operator, num2):
    if operator == "+":
        return(num1 + num2)
    elif operator == "-":
        return(num1 - num2)
    elif operator == "*":
        return(num1 * num2)
    elif operator == "/":
        if num2 != 0:
            return(num1 / num2)
        else:
            return("Error: Cannot divide by zero.")
    else:
        return("Invalid Operator")

while True:
    num1_str = input("Enter the first number or type 'quit': ")

    if num1_str.lower() == "quit":
        break 
    else:
        num1 = float(num1_str)
        operator = input("Please enter +, -, * or /")
        num2 = float(input("Enter the second number:"))
        result = calculate(num1, operator, num2)
        print(f"The result is {result}")

