# age caluclator
from datetime import date
birth_year = int(input("Enter youy birth year : "))
current_year = date.today().year
age = current_year - birth_year
print(age)
