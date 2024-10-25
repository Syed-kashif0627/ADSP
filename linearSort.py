

def linearSort(l,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if(l[j]<l[i]):
                l[i],l[j]=l[j],l[i]


n=int(input("Enter the SIze of List "))
l=[]
for i in range(n):
    elem=int(input(f'Enter The {i+1} th Element:'))
    l.append(elem)

print("Original List:")
print(l)

linearSort(l,n)

print("List After Linear Sort:")

print(l)