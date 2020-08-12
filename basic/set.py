# Set is a collection which is :
# - Unindexed
# - Unordered
# - Do NOT allow duplicate members

education_items = {"pen", "pencil", "bag"}
print("Set of Education Items : ", education_items)
# Note : Sets are unordered, so we cannot be sure in which order the items will appear.

#    Accessing Items
# ========================

# Since sets are unordered, the items has no index. So we cannot access items
# in a set by referring to an index

print("Items in the set :")
for item in education_items:
    print(item)

is_pen = "pen" in education_items
print("is pen in the education_items set? : ", is_pen)


#    Changing Items
# ========================

food_items = {"chocolate", "chips"}
print("Set of Food Items : ", food_items)

# Add Item (one item)
food_items.add("biscuit")
print("New set of Food Items after adding one item : ", food_items)

# Add Items (multiple item)
food_items.update(["fanta", "7up"])
print("New set of Food Items after adding multiple items : ", food_items)

# Remove Item (using remove() method)
food_items.remove("7up")
print("New set of Food Items after removing a item : ", food_items)

# Remove Item (using discard() method)
food_items.discard("7up")
print("New set of Food Items after removing a item : ", food_items)

# There is differenece between remove() & discard() methods.
# If the item to remove does not exist :
# - remove() will raise an error.
# - discard() will NOT raise an error.


#    Union &  Intersection
# =============================

# Union
union_set = education_items | food_items
# or we can use, education_items.union(food_items)
print("Union of two sets : ", union_set)

# Intersection
union_set = education_items & food_items
# or we can use, education_items.intersection(food_items)
print("Intersection of two sets : ", union_set)

#   Multiple Ways to Create a Set
# ==================================

# We can create set from list
my_empty_set = ()
print("Empty Set  : ", my_empty_set)

# We can create set from list
my_list = [1, 2, 2, 3, 5, 5]
set_from_list = set(my_list)
print("Set from List : ", set_from_list)

# We can create set from tuple
my_tuple = (1, 2, 2, 3, 5, 5)
set_from_tuple = set(my_tuple)
print("Set from Tuple : ", set_from_tuple)
