# binary_search.py

from BubbleSort import bubbleSort

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1

n = int(input("Enter the size of the list: "))
l = []
for i in range(n):
    elem = int(input(f'Enter the {i+1}th element: '))
    l.append(elem)

print("Original List:")
print(l)

bubbleSort(l, n)

print("List After Bubble Sort:")
print(l)

target = int(input("Enter the element to search for: "))
result = binary_search(l, target)

if result != -1:
    print(f"Element is present at index {result}")
else:
    print("Element is not present in array")
