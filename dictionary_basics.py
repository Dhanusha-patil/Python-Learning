student = {
    "name": "Dhanusha",
    "age": 22,
    "city": "Bangalore"
}

print("Original Dictionary:")
print(student)

student["course"] = "Python"

student["age"] = 23

student.pop("city")

print("\nUpdated Dictionary:")
print(student)

print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
print("Name:", student.get("name"))
