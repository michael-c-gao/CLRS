#stack
#LIFO

class Stack():
    def __init__(self,array):
        self.array = array
        self.top = len(array) - 1

        
    def stackEmpty(self):
        return (self.top < 0)

    def push(self, item):
        self.top +=1
        self.array.append(item)

    def pop(self):
        if self.stackEmpty():
            print("can't pop an empty stack!")
            return 0
        popped = self.array.pop(self.top)
        self.top -=1
        return popped


     
def main():
    stax = Stack([1,2])
    b = stax.stackEmpty()
    print(b)
    stax.push(3)
    c = stax.pop()
    stax.pop()
    print(c)
    print(stax.array)


if __name__ == '__main__':
    main()
        
        
