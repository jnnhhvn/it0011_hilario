def divide(a, b):
    if b == 0:
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        return None
    return a % b

def summation(a, b):
    if b <= a:
        return None
    return sum(range(a, b + 1))

def format_result(result):
    return int(result) if result.is_integer() else round(result, 2)

def main():
    while True:
        print("\nChoose an operation:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[X] - Exit")
        
        choice = input("\nEnter your choice: ").upper()
        
        if choice == 'X':
            return

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue
        
        if choice == 'D':
            result = divide(num1, num2)
            if result is None:
                print("ERROR! Cannot divide by zero.")
            else:
                print(f"Result: {format_result(result)}")
        
        elif choice == 'E':
            result = exponentiation(num1, num2)
            print(f"Result: {format_result(result)}")
        
        elif choice == 'R':
            result = remainder(num1, num2)
            if result is None:
                print("ERROR! Cannot find remainder by zero.")
            else:
                print(f"Result: {format_result(result)}")
        
        elif choice == 'F':
            result = summation(int(num1), int(num2))
            if result is None:
                print("ERROR! The second number must be greater than the first number.")
            else:
                print(f"Result: {result}") 
        
        else:
            print("Invalid choice. Please select a valid operation.")
            
main()
