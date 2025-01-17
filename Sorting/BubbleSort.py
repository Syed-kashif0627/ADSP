
def bubbleSort(l,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]

def binSearch(arr,key):
    l=0
    h=len(arr)-1

    while l<=h:
        m=(l+h)//2

        if arr[m]==key:
            return m
        elif arr[m]<key:
            l=m+1
        else:
            h=m-1

    return -1



n=int(input("Enter the SIze of List "))
l=[]
for i in range(n):
    elem=int(input(f'Enter The {i+1} th Element:'))
    l.append(elem)


print("Original List:")
print(l)

bubbleSort(l,n)

print("List After Bubble Sort:")

print(l)

k=int(input("Enter Key Value to be Searched: "))

index=binSearch(l,k)

if index==-1:
    print(f"Key {k} not Found in the list!!")
else:
    print(f"Key {k} found at index {index}!!")

