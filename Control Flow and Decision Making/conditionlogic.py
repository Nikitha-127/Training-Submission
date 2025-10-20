print("Student Grades")
# input of 3 subjects
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

# Calculate average
avg = (math + science + english) / 3

print(f"\nAverage Marks: {avg:.2f}")

if avg >= 90:
    grade = "A"
    print("Excellent performance!")
elif 75 <= avg < 90:
    grade = "B"
    print("Very good! Keep improving.")
elif 60 <= avg < 75:
    grade = "C"
    print("Good, but can do better.")
elif 50 <= avg < 60:
    grade = "D"
    print("You passed, but need to work harder.")
else:
    grade = "F"
    print("Failed. Please study more and try again.")

if avg >= 90 and (math == 100 or science == 100 or english == 100):
    print("Class topper")
elif avg < 50 and (math < 40 or science < 40 or english < 40):
    print("Failed")

print(f"\nFinal Grade: {grade}")
