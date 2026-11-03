count = 0

def hanoi(n, source, auxiliary, destination):
    global count

    if n == 1:
        count += 1
        print("Move disk 1 from", source, "to", destination)
        return

    hanoi(n - 1, source, destination, auxiliary)

    count += 1
    print("Move disk", n, "from", source, "to", destination)

    hanoi(n - 1, auxiliary, source, destination)


n = int(input("Enter number of disks: "))

if n <= 0:
    print("Enter a positive number.")
else:
    hanoi(n, 'A', 'B', 'C')

    print("\nTotal Moves:", count)
    print("Minimum Moves:", 2 ** n - 1)
