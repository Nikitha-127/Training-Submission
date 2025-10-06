# program to find the largest of three numbers
num1, num2, num3 = map(int, input("Enter values : ").split())
if num1 > num2 and num1 > num3:
    print("num 1 is largest")
elif num2 > num1 and num2 > num3:
    print("num 2 is largest")
else:
    print("num 3is largest")
