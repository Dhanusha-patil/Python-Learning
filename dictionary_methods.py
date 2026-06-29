# Python Dictionary Methods: clear() and copy()

# Create the original dictionary
student = {
    "name": "Dhanusha",
    "age": 22,
    "city": "Bangalore"
}

print("Original Dictionary:")
print(student)

# -----------------------------
# copy() Method
# -----------------------------
student_copy = student.copy()

print("\nCopied Dictionary:")
print(student_copy)

# -----------------------------
# clear() Method
# -----------------------------
student.clear()

print("\nOriginal Dictionary after clear():")
print(student)

print("\nCopied Dictionary after original is cleared:")
print(student_copy)
