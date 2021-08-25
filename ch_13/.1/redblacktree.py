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
        #O(lgn) time
        y = self.sentinel
        x = self.root
        while(x != self.sentinel):
            y = x
            if(z.value < x.value):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if(y == self.sentinel):
            self.root = z
        elif (z.value < y.value):
            y.left = z
        else:
            y.right = z
        z.left = self.sentinel
        z.right = self.sentinel
        z.color = "red"
        self.RBinsertfixup(z)

    def RBinsertfixup(self,z):
        while(z.parent.color == "red"):
            if(z.parent == z.parent.parent.left):
                y = z.parent.parent.right
                if(y.color == "red"):
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if(z == z.parent.right):
                        z = z.parent
                        self.leftRotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.rightRotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if(y.color == "red"):
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent
                else:
                    if(z == z.parent.left):
                        z = z.parent
                        self.rightRotate(z)
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.leftRotate(z.parent.parent)
        self.root.color = "black"

    def RBtransplant(u,v):
        if(u.parent == self.sentinel):
            self.root = v
        elif( u == u.parent.left):
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RBdelete(self,z):
        y = z
        originalYcolor = y.color
        if(z.left == self.sentinel):
            x = z.right
            RBtransplant(z,z.right)
        elif (z.right == self.sentinel):
            x = z.left
            self.RBtransplant(z,z.left)
        else:
            y = self.treemin(z.right)
            originalYcolor = y.color
            x = y.right
            if(y.parent == z):
                x.parent = y
            else:
                self.RBtransplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.RBtransplant(z,y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if(originalYcolor == "black"):
            RBdeletefixup(x)

    def treemin(self,x):
        while(x.left is not None):
            x = x.left
        return x

    def inorderTraversal(self,x):
        if x is not self.sentinel:
            self.inorderTraversal(x.left)
            print(x.value)
            print(x.color)
            print("___")
            self.inorderTraversal(x.right)

    def preorderTraversal(self,x):
        if x is not self.sentinel:
            print(x.value)
            print(x.color)
            print("___")
            self.preorderTraversal(x.left)
            self.preorderTraversal(x.right)

    def postorderTraversal(self,x):
        if x is not self.sentinel:
            self.postorderTraversal(x.left)
            self.postorderTraversal(x.right)
            print(x.value)
            print(x.color)
            print("___")
            

    def RBdeletefixup(self,x):
        while((x != self.root) and (x.color == "black")):
            if(x == x.parent.left):
                w = x.parent.right
                if(w.color == "red"):
                    w.color == "black"
                    x.parent.color = "red"
                    self.leftRotate(x.parent)
                    w = x.parent.right
                if((w.left.color == "black") and (w.right.color == "black")):
                    w.color = "red"
                    x = x.parent
                else:
                    if(w.right.color == "black"):
                        w.left.color = "black"
                        w.color = "red"
                        self.rightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if(w.color == "red"):
                    w.color == "black"
                    x.parent.color = "red"
                    self.rightRotate(x.parent)
                    w = x.parent.left
                if((w.right.color == "black") and (w.left.color == "black")):
                    w.color = "red"
                    x = x.parent
                else:
                    if(w.left.color == "black"):
                        w.right.color = "black"
                        w.color = "red"
                        self.leftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.rightRotate(x.parent)
                    x = self.root
        x.color = "black"

    def leftRotate(self,x):
        #O(1) time
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
        #O(1) time
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
    a = Node(7)
    b = Node(2)
    c = Node(11)
    d = Node(1)
    e = Node(5)
    f = Node(4)
    g = Node(8)
    h = Node(14)
    i = Node(15)
    rbt.RBinsert(a)
    rbt.RBinsert(b)
    rbt.RBinsert(c)
    rbt.RBinsert(d)
    rbt.RBinsert(e)
    rbt.RBinsert(f)
    rbt.RBinsert(g)
    rbt.RBinsert(h)
    rbt.RBinsert(i)
    rbt.postorderTraversal(rbt.root)
    

if __name__ == "__main__":
    main()
