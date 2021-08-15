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
    i = l-1
    j = l
    for u in range(j,r):
        if array[u] <= x:
            i +=1
            temp = array[i]
            array[i] = array[u]
            array[u] = temp
    temp2 = array[i+1]
    array[i+1] = array[r]
    array[r] = temp2
    return i+1

def main():
    array = [2,3,312,321,3123213,213,123,13,1,321,3123,12,3,2,4,5,4,1,435,5,6,5,5]
    arrayLen = len(array)-1
    quicksort(array,0,arrayLen)
    print(array)

if __name__ == "__main__":
    main()
