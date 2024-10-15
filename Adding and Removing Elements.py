# Creating a set using curly braces
my_set = {1, 2, 3, 4, 5}

# Creating a set using the set() constructor
another_set = set([1, 2, 3, 4, 5])

# Printing the sets
print(my_set)
print(another_set)


# Adding elements
my_set.add(6)  # Add an element
print(my_set)   # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(2)  # Remove an element (raises KeyError if not found)
print(my_set)      # Output: {1, 3, 4, 5, 6}

# Using discard() - does not raise an error if the element is not found
my_set.discard(10)  # Does nothing, no error

