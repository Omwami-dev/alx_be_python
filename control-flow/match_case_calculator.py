
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
print(input("Choose the operation (+, -, *, /): "))
match "operation":
    case "add":
        result = num1 + num2
        print("The result is",(result) )
    case "subtract":
        results = num1 - num2
        print("The reult is",(result))
    case "multiplication":
        results = num1 * num2
        print("The result is",(result))
        
