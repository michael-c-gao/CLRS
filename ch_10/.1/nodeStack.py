#stack implemented w/ nodes
#FILO/LIFO

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None


class Stack():

    def __init__(self):
        self.size = 0
        self.head = None

    def push(self,x):
        
        if not self.isEmpty():
            x.next = self.head
            
        self.head = x
        self.size +=1
            
    
    def pop(self):
        if not self.isEmpty():
            a = self.head
            self.head = self.head.next
            self.size -=1
            return a
            
        else:
            print("cant remove empty stack!")
            return 0

    
    def isEmpty(self):
        return self.size == 0



def main():
    a = Node("h")
    b = Node("i")
    c = Node("!")
    stak = Stack()
    stak.push(a)
    stak.push(b)
    stak.push(c)
    x = stak.pop()
    print(stak.head.value)
    print("_______")
    print(x.value)
    
if __name__ == "__main__":
    main()
