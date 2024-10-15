# Creating a dictionary using curly braces
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Creating a dictionary using the dict() constructor
another_dict = dict(name="Bob", age=25, city="Los Angeles")

# Printing the dictionaries
print(my_dict)
print(another_dict)

# Accessing values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30


#Adding and Modifying Key-Value Pairs
# Adding a new key-value pair
my_dict["job"] = "Engineer"

# Modifying an existing key-value pair
my_dict["age"] = 31

# Printing the updated dictionary
print(my_dict)
