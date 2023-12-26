#  formatted Strings

name = 'John'
age = 55

print('Hi ' + name + '!. You are ' + str(age) + 'years old...') #  this is not a formatted string
#  you can only cancatenate strings with strings not with integers or floatsx

print(f'Hi {name}!. You are {age} years old...') #  f is used to format the string

# print('Hi {}!. You are {} years old...').format("name", "age") --> error because of the paranthesis because .format works on strings and print() is not a string....hence paranthesis should be inside the print() function

print('Hi {}!. You are {} years old...'.format(name, age))

print('Hi {1}!. You are {0} years old...'.format(name, age)) #  this is also correct

print('Hi {new_name}!. You are {new_age} years old...'.format(new_name = 'Sally', new_age = 100)) #  this is also correct   