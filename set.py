# A set is an unordered collection with no duplicate elements.  👉 ️▶️
# 'set' object is not subscriptable
# https://docs.python.org/3/tutorial/datastructures.html#sets
# IT TAKE CURLY BRACKETS
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("Remove duplicate 👉 ", basket)  # show that duplicates have been removed
print("fast membership testing 👉  ", 'orange' in basket)

i = 0
for i in basket:
    print("Looping 👉 ", i)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print("Remove duplicate - unique letters in a 👉  ", a)
print("letters in a but not in b 👉  ", a - b)

# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.

# ADD NEW ITEM
basket.add('guava')
print("Add a item 👉 ", "guava" in basket)





