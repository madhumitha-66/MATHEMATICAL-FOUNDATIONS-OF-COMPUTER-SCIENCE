def f(x):
    return x + 5000

def g(x):
    return 0.9 * x

salary = float(input("Enter basic salary: "))

gf = g(f(salary))
fg = f(g(salary))

print("\nSALARY PROCESSING")

print("Basic Salary:", salary)
print("After Bonus:", f(salary))
print("g(f(x)):", gf)
print("f(g(x)):", fg)

print("Equal:", gf == fg)
