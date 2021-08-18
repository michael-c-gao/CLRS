#quicksort
#n^2 worst case running time
#nlgn average case running time

def quicksort(array,l,r):
    if (l < r):
        mid = partition(array,l,r)
        quicksort(array,l,mid-1)
        quicksort(array,mid+1,r)

def partition(array,l,r):
    x = array[r]
    i = l
    for u in range(l,r):
        if array[u] <= x:
            temp = array[i]
            array[i] = array[u]
            array[u] = temp
            i +=1
    temp2 = array[i]
    array[i] = array[r]
    array[r] = temp2
    return i

def main():
    array = [8,3,1,6,4]
    arrayLen = len(array)-1
    quicksort(array,0,arrayLen)
    print(array)

if __name__ == "__main__":
    main()
