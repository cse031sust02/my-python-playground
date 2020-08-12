# List is a collection which is :
# - Mutable (Changeable)
# - Ordered
# - Allows duplicate members

countries = ["Bangladesh", "India", "Pakistan"]
print("Country List : ", countries)

#    Accessing Items
# ========================

print("First item of the list is : ", countries[0])
print("Last item of the list is : ", countries[-1])
print("Second & Third items of the list is : ", countries[1:3])

# looping through list
print("Items in the list : ")
for country in countries:
    print(country)

total = len(countries)
print("Total Items : ", total)

is_bd = "Bangladesh" in countries
print("Is Bangladesh in the list? :", is_bd)

#    Changing Items
# ======================

print("Changing the second item")
countries[1] = "Afganistan"

print("Adding Bhutan to the list")
countries.append("Bhutan")

print("Removing Pakistan from the List")
countries.remove("Pakistan")

# when we create a new list from another like this : list2 = list1,
# any changes made in list1 will automatically be made in list2.
# Because list2 is only a reference to list1

countries2 = countries
print("Adding Nepal to second list")
countries2.append("Nepal")
print("New Country List : ", countries)

#     Copy a List
# ====================

countries_copy = countries.copy()
# or we can use, list(countries)
print("New Copied List : ", countries_copy)

# note : We can now made changes to the new `countries_copy` list,
# It will NOT affect the original `countries` list
