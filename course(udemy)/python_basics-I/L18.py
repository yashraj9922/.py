# string index

selfish = "me me me"
         # 01234567

print(selfish[0]) #  prints m
print(selfish[7]) #  prints e
print(selfish[-1]) #  prints e

#  [start:stop:stepover]
print(selfish[0:2]) #  prints me
print(selfish[0:3]) #  prints me 
print(selfish[0:8]) #  prints me me me

print(selfish[0:8:1]) #  prints me me me
print(selfish[0:8:2]) #  prints m m m


selfish = "01234567"

print(selfish[0]) # prints 0
print(selfish[7]) # prints 7
print(selfish[-1]) # prints 7   #  negative index starts from the end

print(selfish[0:2]) # prints 01
print(selfish[0:3]) # prints 012
print(selfish[0:8]) # prints 01234567

print(selfish[0:8:1]) # prints 01234567
print(selfish[0:8:2]) # prints 0246x


# reverse a string
print(selfish[::-1]) #  prints 76543210