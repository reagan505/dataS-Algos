set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a | set_b  # Output: {1, 2, 3, 4, 5}
print("Union:", union_set)

# Intersection
intersection_set = set_a & set_b  # Output: {3}
print("Intersection:", intersection_set)

# Difference
difference_set = set_a - set_b  # Output: {1, 2}
print("Difference:", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b  # Output: {1, 2, 4, 5}
print("Symmetric Difference:", symmetric_difference_set)
