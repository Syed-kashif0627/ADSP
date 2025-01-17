
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
    l,h = 0,len(arr) - 1

    while l<=h:
        mid=l+(h-l)//2

        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            l=mid+1
        else:
            h=mid-1

    return -1

def recBinSearch(arr,l,h,key):
    if l>h:
        return -1
    else:
        m=(l+h)//2

        if arr[m]==key:
            return m
        elif arr[m]<key:
            return recBinSearch(arr,m+1,h,key)
        else:
            return recBinSearch(arr,l,m-1,key)
        


target = int(input("Enter the element to search for: "))
result = binary_search(l, target)

if result != -1:
    print(f"Element {target} is present at position {result+1}")
else:
    print("Element is not present in array")

k=int(input("Enter The Key element to be searched Recursively: "))
index=recBinSearch(l,0,n-1,k)

if index==-1:
    print(f"The Element {k} is Not Found in the List !!")
else:
    print(f'The Element {k} is Found at index {index}')

