# Dictionary is a collection which is :
# - Mutable (Changeable)
# - Ordered*
# - Allow duplicate members

# *Python’s dictionary has been unordered up until Python 3.6
# more details : https://softwaremaniacs.org/blog/2020/02/05/dicts-ordered/

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

print("Changing studentent's section to B")
student['section'] = 'B'
print("New value of student dict : ", student)

print("Adding new item to student dict")
student['gender'] = 'male'
print("New value of student dict : ", student)

print('removing a item (roll) from student dict')
student.pop('roll')
print("New value of student dict : ", student)


#    MISC
# ===========

# We can use immutubale data structures as key in a dictionart
dict_key_example = {1: "sample number",
                    "str": "sample string", (1, 2, 3): "sample tuple"}
print("Dictionary with different types of keys : ", dict_key_example)
for key in dict_key_example:
    print(key, " : ", type(key))
