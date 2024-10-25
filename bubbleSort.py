
def bubbleSort(l,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if(l[j]>l[j+1]):
                l[j],l[j+1]=l[j+1],l[j]



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