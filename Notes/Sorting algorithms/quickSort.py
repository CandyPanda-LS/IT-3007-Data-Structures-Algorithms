A = []
for x in range (5):
    A.append(int(input("Enter number:")))
    print(A)

def Partition(A,p,r):
# r is the last index of the array and p is the first index of the array
    x = A[r]
    i = p -1

    for j in range (p,r):
        if A[j] <= x:
            i = i+1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return (i+1)

def Quicksort(A,p,r):
    if p < r:
        q = Partition(A,p,r)
        Quicksort(A,p,q-1)
        Quicksort(A,q+1,r)



Quicksort(A,0,len(A)-1)
print(A)
