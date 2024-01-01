# List Slicing

amazon_cart = ['Notebooks', 'Sunglasses', 'Toys', 'Grapes']

print(amazon_cart[0])
print(amazon_cart[1])

print(amazon_cart[0:2])

#  [start:stop:stepover]
print(amazon_cart[0::3])

# Lists are mutable
amazon_cart[0] = 'Laptop'

new_cart = amazon_cart[0:3]
new_cart[0] = "macbook"
print(new_cart) # Everytime we do List Slicing we create a new copy of that List
print(amazon_cart)


# cart = amazon_cart
# cart[0] = 'TV'
# print(cart)
# print(amazon_cart)
# This is not how u copy a list....here u had just assign two variables to same list

# Copying a List
copy_cart = amazon_cart[:]  
copy_cart[0] = 'TV'
print(copy_cart)
print(amazon_cart)