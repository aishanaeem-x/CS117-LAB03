def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def divide(a, b):
    if b == 0:
        return "Error! Division by zero"
    return a / b
def multiply(a, b):
    return a * b
def percentage(part, total):
    if total == 0:
        return "Error! Division by zero"
    return (part / total) * 100
def odd_or_even(a):
    if a % 2 == 0:
        return "Number is Even"
    else:
        return "Number is Odd"
while True:
    print("calculator\n")
    print("1. ADDITION")
    print("2. SUBTRACTION")
    print("3. DIVISION")
    print("4. MULTIPLICATION")
    print("5. PERCENTAGE")
    print("6. CHECK EVEN/ODD")
    print("7. EXIT")

    choice = input("Enter your choice: ")

    if choice == "7":
        print("Exiting calculator...")
        break

    if choice == "6":
        a=int(input("Enter a number: "))
    else:
        a=float(input("Enter first number: "))
        b=float(input("Enter second number: "))


    if choice == "1":
        print("Answer:", add(a, b))
    elif choice == "2":
        print("Answer:", subtract(a, b))
    elif choice == "3":
        print("Answer:", divide(a, b))
    elif choice == "4":
        print("Answer:", multiply(a, b))
    elif choice == "5":
        print("Answer:", percentage(a, b))
    elif choice == "6":
        print(odd_or_even(a))
    else:
        print("Invalid choice. Try again.")
