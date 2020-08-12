# Dictionary is a collection which is :
# - Mutable (Changeable)
# - Unordered
# - Allow duplicate members

student = {
    "name": "Talha",
    "roll": 102,
    "section": "A"
}
print("Student : ", student)

#    Accessing Items
# ========================

# using [key]
print("Name of the Student : ", student['name'])
# note : It will raise a KeyError if the key does not exist

# using get() method
print("Roll Number of the Student :", student.get('roll'))
# note : If the key does not exist : 
# - It will NOT raise any error
# - It will return None

is_section = "section" in student
print("Does section key exist? : ", is_section)

print("Number of items in the dictionary : ", len(student))


#    Looping Through
# ========================
# When looping through a dictionary, the return value are the keys of the dictionary
print("Keys in the dictionary :")
for item in student:
    print(item)

# get only values using values() method
print("Values of the dictionary :")
for value in student.values():
    print(value)

# get key and values using items() method
print("Keys and Values of the dictionary :")
for key, value in student.items():
    print(key, value)

#    Changing Items
# ========================



#    MISC
# ===========

# We can use immutubale data structures as key in a dictionart
dict_key_example = {1: "sample number",
                    "str": "sample string", (1, 2, 3): "sample tuple"}
print("Dictionary with different types of keys : ", dict_key_example)
for key in dict_key_example:
    print(key, " : ", type(key))
