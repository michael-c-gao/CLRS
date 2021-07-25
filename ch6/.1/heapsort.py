#heapsort 
#O(nlgn)
#sorts in place


def parent(i):
    return ((i-1)//2)

def left(i):
    return ((2*i)+1)

def right(i):
    return ((2*i)+2)


def maxheapify(array,i, heapsize):
    l = left(i)
    r = right(i)
    if ((l <= heapsize) and (array[l] > array[i])):
        largest = l
    else:
        largest = i
    if((r <= heapsize) and (array[r] > array[largest])):
       largest = r
    if (largest != i):
       temp2 = array[i]
       array[i] = array[largest]
       array[largest] = temp2
       maxheapify(array, largest, heapsize)

def buildmaxheap(array, heapsize):
    #heapsize = len(array)
    for i in range((len(array)//2),-1,-1):
        maxheapify(array,i, heapsize)

def heapsort(array):
    heapsize = len(array)-1
    
    buildmaxheap(array,heapsize)
    for i in range(heapsize,0,-1):
        
        temp1 = array[i]
        array[i] = array[0]
        array[0] = temp1
        heapsize = heapsize -1
        maxheapify(array,0,heapsize)
    print(array)

def main():
    a = [5,4,3,2,1,6,5,8,4,1,321,12,4,4,31,1,3232,2,3,321,1232,132]
    b = [1,2,3,4,5]
    heapsort(a)


if __name__ == '__main__':
    main()
