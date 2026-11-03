def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        mid = (low + high) // 2
        count += 1

        if arr[mid] == key:
            return mid, count

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1, count


n = int(input("Enter number of elements: "))

arr = list(range(1, n + 1))

key = int(input("Enter element to search: "))

position, comparisons = binary_search(arr, key)

print("\nPosition:", position)
print("Comparisons:", comparisons)

if position != -1:
    print("Element Found")
else:
    print("Element Not Found")
