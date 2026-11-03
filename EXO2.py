from itertools import product

equivalent = True

print("LOGICAL EQUIVALENCE VERIFICATION")
print("--------------------------------")
print("P Q | E1 | E2")

for P, Q in product([False, True], repeat=2):

    E1 = not (P and Q)
    E2 = (not P) or (not Q)

    print(int(P), int(Q), "|", int(E1), "|", int(E2))

    if E1 != E2:
        equivalent = False

print("\nEquivalent:", equivalent)
