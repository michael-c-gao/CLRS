#doubly linked list

class Node():
    
    def __init__(self,key):
        self.key = key
        self.next = None
        self.prev = None


class LL():

    def __init__(self):
        self.head = None
        self.tail = None
        self.currSize = 0

    def insert(self,x):
        newnode = Node(x)
        newnode.next = self.head
        
        if self.head is None:
            self.tail = newnode
            
        else:
            self.head.prev = newnode
            
        self.head = newnode
        newnode.prev = None
        self.currSize += 1
            
    def traverse(self):
        print("___starting head to tail traverse___")
        
        currnode = self.head
        while currnode:
            print(currnode.key)
            currnode = currnode.next
            
        print("___done___")
        print("\n")

    def raverse(self):
        #the spelling mistake in the declaration is on purpose
        
        print("___starting tail to head traverse___")
        
        currnode = self.tail
        while currnode:
            print(currnode.key)
            currnode = currnode.prev
            
        print("___done___")
        print("\n")              

    def search(self, k):
        x = self.head
        while ((x is not None) and (x.key != k)):
            x = x.next
        return x
        
    
    def headdelete(self):
        if self.currSize < 1:
            print("Can't remove from empty linked list")
            return 0
        if self.currSize > 1:
            newhead = self.head.next
            newhead.prev = None
            self.head.next = None
            self.head = newhead
            
        else:
            self.head = None
            self.tail = None
            
        self.currSize -=1

    def taildelete(self):
        if self.currSize < 1:
            print("Can't remove from empty linked list")
            return 0
        if self.currSize > 1:
            newtail = self.tail.prev
            newtail.next = None
            self.tail.prev = None
            self.tail = newtail
            
        else:
            self.tail = None
            self.head = None
            
        self.currSize -=1 

    def specificdelete(self,y):
        if self.currSize < 1:
            print("Can't remove from empty linked list")
            return 0
        a = self.search(y)
        if a == self.tail:
            self.tail = a.prev
        if a.prev is not None:
            a.prev.next = a.next
        else:
            self.head = a.next
        if a.next is not None:
            a.next.prev = a.prev
        self.currSize -=1

    def numElements(self):
        return self.currSize

    def tailKey(self):
        return self.tail.key

    def headKey(self):
        return self.head.key


def main():
    x = LL()
    x.insert("a")
    x.insert("b")
    x.insert("c")
    x.insert("d")
    x.insert("e")
    x.insert("f")
    x.insert("g")
    x.insert("h")
    x.headdelete()
    x.taildelete()
    x.specificdelete("c")
    x.specificdelete("e")
    x.raverse()
    x.traverse()


if __name__ == "__main__":
    main()
