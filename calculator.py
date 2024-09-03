def calculator():
    while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /) or type 'exit' to quit: ")

        
        if operation == 'exit':
            print("thanks !!!!")
            break
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero.")
                continue
        else:
            print("Invalid operation.")
            continue
        
        print(f"Result: {result}")


        
calculator()
