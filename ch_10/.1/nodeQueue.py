#queue implemented with nodes
#FIFO/LILO

class Node():

    def __init__(self,value):
        self.value = value
        self.next = None

class Queue():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def nq(self, x):
        if self.isEmpty():
            self.head = x
        else:
            self.tail.next = x
        self.tail = x
        self.size +=1
        
    def dq(self):
        if self.isEmpty():
            print("can't dequeue from an empty queue!")
            return 0
        else:
            a = self.head
            self.head = self.head.next
            self.size -=1
            return a

    def isEmpty(self):
        return self.size == 0

    def traverse(self):
        a = self.head
        print("___starting traverse.___")
        while a:
            print(a.value)
            a = a.next
        print("___Done.___\n")


def main():
    a = Node("h")
    b = Node("i")
    c = Node("!")
    q = Queue()
    q.nq(a)
    q.nq(b)
    q.nq(c)
    q.traverse()
    q.dq()
    q.traverse()
    


if __name__ == "__main__":
    main()
