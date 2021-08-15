#mergesort (✓)
import math

def mergesort(array, l, r):

    if (l < r):
        mid = ((l+r)//2)
        mergesort(array, l, mid)
        mergesort(array, mid + 1, r)
        merge(array, l, mid, r)


def merge(array, l, mid, r):
        
    n1 = mid - l + 1
    n2 = r - mid
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)
    for i in range (0, n1):
        L[i] = array[l + i]
    for j in range (0, n2):
        R[j] = array[mid + j + 1]
    L[n1] = math.inf
    R[n2] = math.inf
    
    i = 0
    j = 0
    
    for k in range (l,r+1):
        if(L[i] <= R[j]):
            array[k] = L[i]
            i = i + 1
        else:
            array[k] = R[j]
            j = j + 1
    
def main():
    array = [8,2,1]
    mergesort(array, 0, 2)
    print(array)

if __name__ == "__main__":
    main()
    
