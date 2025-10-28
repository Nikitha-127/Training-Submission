def factorial_recursive(f):
    if f <= 1:
        return 1
    else:
        return f * factorial_recursive(f - 1)


try:

    num = int(input("Enter a non-negative integer: "))

    if num < 0:
        print("Factorial is not defined")
    else:
        result = factorial_recursive(num)
        print(f"The factorial of {num} is: {result}")

except ValueError:
    print("Invalid input. Please enter a whole number.")
