# Creating a dictionary to store student information
student = {
    "name": "Charlie",
    "age": 22,
    "courses": ["Math", "Science"]
}

# Adding a new course
student["courses"].append("History")

# Modifying the age
student["age"] = 23

# Printing the student information
print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")
