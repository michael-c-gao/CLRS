#priority queue
import math

class PQ():
    def __init__(self, array):
        self.array = array
        self.heapsize = len(array)-1
        
    def parent(self,i):
        return ((i-1)//2)

    def left(self,i):
        return ((2*i)+1)

    def right(self,i):
        return ((2*i)+2)

    def buildmaxheap(self):
        for i in range((len(self.array)//2),-1,-1):
            self.maxheapify(i)


    def heapmaximum(self):
        return self.array[0]


    def maxheapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if ((l <= self.heapsize) and (self.array[l] > self.array[i])):
            largest = l
        else:
            largest = i
        if((r <= self.heapsize) and (self.array[r] > self.array[largest])):
           largest = r
        if (largest != i):
           temp2 = self.array[i]
           self.array[i] = self.array[largest]
           self.array[largest] = temp2
           self.maxheapify( largest)

    def heapextractmax(self):
        if(self.heapsize < 1):
            print("size is less than 1")
            return 0
        maxx = self.array[0]
        self.array[0] = self.array[self.heapsize]
        self.array.pop(self.heapsize)
        self.heapsize -=1
        self.maxheapify(0)
        return maxx

    def heapincreasekey(self, i, key):
        if(key < self.array[i]):
            print("new key smaller than current key")
            return 0
        self.array[i] = key
        while((i >0) and ( self.array[self.parent(i)] < self.array[i])):
            temp = self.array[i]
            self.array[i] = self.array[self.parent(i)]
            self.array[self.parent(i)] = temp
            i = self.parent(i)

    def maxheapinsert(self,key):
        self.array.append(0)
        self.heapsize += 1
        self.array[self.heapsize] = -math.inf
        self.heapincreasekey(self.heapsize,key)
    

def main():
    prioq = PQ([4,5,2,1])
    prioq.buildmaxheap()
    prioq.maxheapinsert(5)
    prioq.maxheapinsert(11)
    print(prioq.array)
    prioq.heapincreasekey(5,25)
    print(prioq.array)
    prioq.heapextractmax()
    print(prioq.array)
    a = prioq.heapmaximum()
    print(a)
    

if __name__ == "__main__":
    main()
