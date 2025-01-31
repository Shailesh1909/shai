# Tuple Operations
# Create a tuple of numbers and:
# Find the maximum and minimum values.
# Calculate the sum of all elements.
# Count how many times a specific number appears.

thistuple = (10, 20, 30, 40, 50)
print(min(thistuple))
print(max(thistuple))
print(sum(thistuple))

# Write a program that:
# Creates two sets of students enrolled in "Python" and "Data Science" courses.
# Finds the students who are enrolled in both courses (intersection).
# Lists students who are in either of the courses but not both (symmetric difference).

python = {"shailesh", "Dev", "manish", "riya", "preksha"}
ds= {"shiv", "yashu", "gandhi", "Dev", "riya"}

python.intersection_update(ds)
print(python)
python.symmetric_difference_update(ds)
print(python)

# Write a program that takes a list of integers with duplicates and returns a list with unique values, maintaining the original order.

set = {1, 2, 3, 4, 11, 15, 2, 3, 15}
print(set)

# Set Methods
# Create a set of integers and:
# Add a new element to the set.
# Remove an existing element.
# Check if a specific element exists in the set.

setl = {1, 2, 3, 4, 5, 6}
mylist = [1, 5, 10]

setl.update(mylist)
print(setl)

# Basic Operations
# Create a dictionary with keys as country names and values as their capitals. Write a program that:
# Adds a new country-capital pair.
# Updates the capital of an existing country.
# Removes a country from the dictionary.

set = {"India", "Pakistan", "Austrialia"}
mylist = ["nepal", "china"]


set.update(mylist)
print(set)
set.remove("nepal")
print(set)
