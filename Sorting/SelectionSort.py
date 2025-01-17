

def selectionSort(l,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if(l[j]<l[i]):
                l[i],l[j]=l[j],l[i]

def binSearch(arr,key):
    l,h=0,len(arr)-1

    while l<=h:
        m=l+(h-l)//2

        if arr[m]==key:
            return m
        elif arr[m]<key:
            l=m+1
        else:
            h=m-1
    
    return -1

n=int(input("Enter the Size of List: "))
l=[]
for i in range(n):
    elem=int(input(f'Enter The {i+1} th Element: '))
    l.append(elem)

print("Original List:")
print(l)

selectionSort(l,n)

print("List After selection Sort:")

print(l)

k=int(input("Enter Key Element to be searched in the List: "))

index=binSearch(l,k)

if index!=-1:
    print(f"The element {k} is found at index {index} !!")
else:
    print(f"The element {k} is not present in the given List !!")
