def  perform_operation(num1, num2,):
    add = num1 + num2
    subtract = num1 - num2
    multiply = num1 * num2
    divide = num1 / num2 if num2 !=0 else "Division by zero is not allowed"
    return add, subtract, multiply, divide  
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation(add, subtract, multiply, divide): ")
    result = perform_operation(num1, num2=)
    print(f"Result: {result}")


