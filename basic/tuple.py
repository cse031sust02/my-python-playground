# Tuple is a collection which is :
# - Immutable (Unchangeable)
# - Ordered
# - Allows duplicate members

my_tuple = (1, 3, 4)
print("My first tuple : ", my_tuple)

#    Accessing Items
# ========================

print("Second Item : ", my_tuple[1])

is_one = 1 in my_tuple
print("Does 1 exists? : ", is_one)

# looping through tuple
print("All items in the tuple :")
for item in my_tuple:
    print(item)

print("Total Items : ", len(my_tuple))

#    Changing Items
# ========================

# Tuple is immutable, we cannot change its values after it is created
# my_numbers[2] = test
# will raise an Error

#    Tuple <---> Variables
# =============================

# extracting multiple variables from a tuple
first, second, third = my_tuple
print("Values of the variables named `first`, `second` & `third` is : ")
print(first, second, third)

# creating a tuple from multiple variables
my_tuple2 = second, third
print("My second tuple : ", my_tuple2)
