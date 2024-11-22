def partition(A,l,h):
    i=l
    j=h
    p=A[l]
    while(i<j):
        while A[i]<=p and i<h:
            i+=1
        while A[j]>p:
            j-=1
        
        if i<j:
            A[i],A[j]=A[j],A[i]
        
    A[l]=A[j]
    A[j]=p
    return j

def QuickSort(A,l,h):
    if(l<h):
        pos=partition(A,l,h)
        QuickSort(A,l,pos-1)
        QuickSort(A,pos+1,h)

n=int(input("Enter the the number of elements: "))
A=[]
for i in range(n):
    elem=int(input(f'Enter the {i+1}th element: '))
    A.append(elem)

print("List before Quick sort: ",A)

QuickSort(A,0,n-1)

print("List After Quick SOrt:",A)
