A = {1, 2, 3, 4}
B = {"IT", "CSE", "ECE"}

f = {
    1: "IT",
    2: "CSE",
    3: "ECE",
    4: "CSE"
}

print("STUDENT DEPARTMENT MAPPING")
print("--------------------------")

for student in sorted(A):
    print(student, "->", f[student])

# Find range
range_set = set(f.values())

# Check injective and surjective
injective = len(range_set) == len(A)
surjective = range_set == B

print("\nRange:", range_set)
print("Injective:", injective)
print("Surjective:", surjective)
