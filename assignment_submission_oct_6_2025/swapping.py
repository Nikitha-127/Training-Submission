# Python program to swap two numbers without using a temporary variable
a, b = map(int, input("Enter numbers : ").split())
a, b = b, a
print(a, b)
