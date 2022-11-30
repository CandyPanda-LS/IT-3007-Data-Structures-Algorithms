A = []
for x in range (5):
    A.append(int(input("Enter number: ")))
    print(A)

def insertionSort(A) :
    n = len(A)
    print(n)
    for i in range (1,n):
        key = A[i]
        j = i -1

        while j >= 0 and A[j]> key:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = key

insertionSort(A)
print("Sorted array:")
print(A)
        
