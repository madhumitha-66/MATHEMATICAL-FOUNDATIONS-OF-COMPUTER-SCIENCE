A = {"Laptop", "Mobile", "Tablet"}
B = {"UPI", "Card"}

cartesian = {
    (a, b) for a in A for b in B
}

print("CARTESIAN PRODUCT")

for item in sorted(cartesian):
    print(item)

print("\nCardinality:", len(cartesian))

print("Expected Cardinality:", len(A) * len(B))
