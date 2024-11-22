def MergeSort(A, l, h):
    if l < h:
        m = (l + h) // 2
        MergeSort(A, l, m)
        MergeSort(A, m + 1, h)
        Merge(A, l, m, h)

def Merge(A, l, m, h):
    i = l
    j = m + 1
    k = 0
    B = [0] * (h - l + 1)
    while i <= m and j <= h:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1
    
    while i <= m:
        B[k] = A[i]
        i += 1
        k += 1
    
    while j <= h:
        B[k] = A[j]
        j += 1
        k += 1
    
    for k in range(len(B)):
        A[k + l] = B[k]

n = int(input("Enter the number of elements: "))
A = []
for i in range(n):
    elem = int(input(f'Enter the {i+1}th element: '))
    A.append(elem)

print("List before Merge sort: ", A)

MergeSort(A, 0, n - 1)

print("List after Merge sort: ", A)
