# immutability

name = "Sam"
# name[0] = "P" --> error because strings are immutable

name = "John" #  this is correct
print(name)
# The only way to change is, completely reassign the value

name = name + "Yash"
print(name)
