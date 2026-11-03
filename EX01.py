from itertools import product

print("RAILWAY SIGNALLING SYSTEM")
print("-------------------------")
print("P Q R | Entry Permission")

for P, Q, R in product([False, True], repeat=3):
    result = (P and Q) or R

    print(int(P), int(Q), int(R), "|", int(result))
