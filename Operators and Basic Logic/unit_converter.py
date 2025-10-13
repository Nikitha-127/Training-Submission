def unit_converter():
    print("Choose options : ")
    print("1-Kilometer to Miles")
    print("2-Miles to kilometer")
    print("3-Celsius to Fahrenheit")
    print("4-Fahrenheit to Celsius")
    try:
        choice = int(input("Enter choice (1/2/3/4): "))

        if choice not in [1, 2, 3, 4]:
            raise ValueError("Invalid option. Please choose 1, 2, 3, or 4.")

        value = float(input("Enter the value to convert: "))
        if choice == 1:
            result = value * 0.621371
            print(f"{value} km = {result:.2f} miles")
        elif choice == 2:
            result = value / 0.621371
            print(f"{value} miles = {result:.2f} km")
        elif choice == 3:
            result = (value * 9/5) + 32
            print(f"{value}°C = {result:.2f}°F")
        elif choice == 4:
            result = (value - 32) * 5/9
            print(f"{value}°F = {result:.2f}°C")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Something went wrong: {e}")


# Run the program
unit_converter()
