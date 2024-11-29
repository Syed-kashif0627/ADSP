
def insertionSort(l,n):
    for i in range(1,n):
        t=l[i]
        j=i-1
        while j>=0 and t<l[j]:
            l[j+1]=l[j]
            j-=1;

        l[j+1]=t;


n=int(input("Enter the SIze of List "))
l=[]
for i in range(n):
    elem=int(input(f'Enter The {i+1} th Element:'))
    l.append(elem)

print("Original List:")
print(l)

insertionSort(l,n)

print("List After Insertion Sort:")

print(l)
