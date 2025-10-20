import random
print("BOOLEAN LOGIC EXAMPLE")
age = int(input("Enter your age: "))
has_id = input("Do you have an ID? (yes/no): ").lower() == "yes"

if age >= 18 and has_id:
    print("✅ You are allowed to enter.")
elif age >= 18 and not has_id:
    print("You are old enough but need an ID.")
else:
    print("You are not allowed to enter.")

print("\n=== NUMBER GUESSING GAME ===")
secret = random.randint(1, 20)
attempts = 0

print("I'm thinking of a number between 1 and 20!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print("fCorrect! You guessed it in {attempts} tries.")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("\n=== FIZZBUZZ ===")
for i in range(1, 21):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


def right_triangle(n):
    print("\nRight Triangle Pattern:")
    for i in range(1, n + 1):
        print("*" * i)


def pyramid(n):
    print("\nPyramid Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def diamond(n):
    print("\nDiamond Pattern:")
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


# Call pattern functions
right_triangle(5)
pyramid(5)
diamond(5)

print("\n All tasks completed successfully!")
