#queue
#FIFO

class Queue():

    def __init__(self,array):
        self.array = array
        self.size = len(array) - 1

    def nq(self, item):
        self.size +=1
        self.array.append(item)

    def dq(self):
        
        if self.size > -1:
            self.size -=1
            return self.array.pop(0)
            
        else:
            print("can't dq an empty array!")
            return 0
def main():
    q = Queue([1,2,3])
    q.nq(4)
    q.nq(5)
    q.nq(6)
    q.dq()
    q.dq()
    print(q.array)

if __name__ == '__main__':
    main()
