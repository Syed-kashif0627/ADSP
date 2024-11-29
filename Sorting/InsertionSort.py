
def insertionSort(l,n):
    for i in range(1,n):
        t=l[i]
        j=i-1
        while j>=0 and t<l[j]:
            l[j+1]=l[j]
            j-=1;

        l[j+1]=t;


n=int(input("Enter the Size of List: "))
l=[]
for i in range(n):
    elem=int(input(f'Enter The {i+1} th Element:'))
    l.append(elem)

print("Original List:")
print(l)

insertionSort(l,n)

print("List After Insertion Sort:")

print(l)

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

target = int(input("Enter the element to search for: "))
result = binary_search(l, target)

if result != -1:
    print(f"Element is present at position {result+1}")
else:
    print("Element is not present in array")

