n = int(input("Enter number of generations: "))

f = [0, 1]

for i in range(2, n + 1):
    f.append(f[i - 1] + f[i - 2])

print("\nPOPULATION SEQUENCE")

for i in range(n + 1):
    print("Generation", i, ":", f[i])

print("\nFinal Population:", f[n])
