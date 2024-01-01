birth_year = input('What year you were born? ')
# input() --> this returns type <class 'str'>
print(type(birth_year))

age = 2023 - int(birth_year)

print(f"Your age is: {age}")