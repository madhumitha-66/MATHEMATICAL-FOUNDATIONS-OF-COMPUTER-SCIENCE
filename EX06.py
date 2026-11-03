A = {1, 2, 3}

R = {
    (1, 1), (2, 2), (3, 3),
    (1, 2), (2, 3), (1, 3)
}

print("STUDENT PREREQUISITE RELATION")
print("-----------------------------")

print("Relation:", R)

# Check reflexivity
reflexive = all((a, a) in R for a in A)

# Check symmetry
symmetric = all(
    (b, a) in R for a, b in R
)

# Check antisymmetry
antisymmetric = all(
    a == b or (b, a) not in R
    for a, b in R
)

# Check transitivity
transitive = all(
    (a, c) in R
    for a, b in R
    for x, c in R
    if b == x
)

print("\nReflexive:", reflexive)
print("Symmetric:", symmetric)
print("Antisymmetric:", antisymmetric)
print("Transitive:", transitive)

# Check partial order
partial_order = (
    reflexive and antisymmetric and transitive
)

print("Partial Order:", partial_order)
