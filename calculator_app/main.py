from calculator import calculate

def main():
    print("Simple Calculator")
    print("Available operations: add, subtract, multiply, divide")

    while True:
        try:
            operation = input("Enter operation (add, subtract, multiply, divide) or 'quit' to exit: ").lower()
            if operation == 'quit':
                break

            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                print("Invalid operation. Please choose from 'add', 'subtract', 'multiply', 'divide'.")
                continue

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            result = calculate(operation, num1, num2)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
