A = []
for x in range (6):
    A.append(int(input("Eneter number :")))
    # to gt the element as a list
    print (A)

def selectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        min = j

        for i in range (j+1,n):
            if A[i] < A[min]:
                min = i
        A[j],A[min] = A[min],A[j]
selectionSort(A)
print('Sorted Array :')
print (A)
                
