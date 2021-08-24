#red-black tree
"""
Properties:
1. A node's color is either red or black
2. The root is black
3.All leaves are black
4.Red nodes have black children
5. For all nodes, all simple paths from the node
to descendant leaves contain the
same number of black nodes.
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = "black"


class RBT():
    def __init__(self):
        self.sentinel = Node(-1)
        self.sentinel.color = "black"
        self.root = self.sentinel


    def RBinsert(self,z):
        pass

    def RBinsertfixup(self,z):
        pass

    def RBtransplant(u,v):
        pass

    def RBdelete(self,z):
        pass

    def RBdeletefixup(self,x):
        pass

    def leftRotate(self,x):
        y = x.right
        x.right = y.left
        if(y.left != self.sentinel):
            y.left.parent = x
        y.parent = x.parent
        if(x.parent == self.sentinel):
            self.root = y
        elif (x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    
        

    def rightRotate(self,x):
        y = x.left
        x.left = y.right
        if(y.right != self.sentinel):
            y.right.parent = x
        y.parent = x.parent
        if(x.parent == self.sentinel):
            self.root = y
        elif (x == x.parent.right):
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
        

def main():
    rbt = RBT()


if __name__ == "__main__":
    main()
