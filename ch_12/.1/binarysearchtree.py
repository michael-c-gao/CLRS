#binary search tree


class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class BST():

    def __init__(self):
        self.root = None

    def inorderwalk(self,x):
        if x is not None:
            self.inorderwalk(x.left)
            print(x.value)
            self.inorderwalk(x.right)

    def postorderwalk(self,x):
        if x is not None:
            self.postorderwalk(x.left)
            self.postorderwalk(x.right)
            print(x.value)

    def preorderwalk(self,x):
        if x is not None:
            print(x.value)
            self.postorderwalk(x.left)
            self.postorderwalk(x.right)

    def treesearch(self, x, k):
        while((x is not None) and (k != x.value)):
            if(k < x.value):
                x = x.left
            else:
                x = x.right
        return x

    def treemin(self,x):
        while(x.left is not None):
            x = x.left
        return x

    def treemax(self,x):
        while(x.right is not None):
            x = x.right
        return x

    def treesuccessor(self,x):
        if x.right is not None:
            return self.treemin(x.right)
        y = x.parent
        while((y is not None) and (x == y.right)):
            x = y
            y = y.parent
        return y

    def insert(self,z):
        y = None
        x = self.root
        while(x is not None):
            y = x
            if(z.value < x.value):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if(y is None):
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z
            

    def transplant(self,u,v):
        if(u.parent is None):
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if(v is not None):
            v.parent = u.parent

    def delete(self,z):
        if(z.left is None):
            self.transplant(z,z.right)
        elif (z.right is None):
            self.transplant(z,z.left)
        else:
            y = self.treemin(z.right)
            if(y.parent!= z):
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y
        
    
    
def main():
    a = Node(2)
    c = Node(5)
    d = Node(7)
    e = Node(6)
    f = Node(8)
    g = Node(5)

    b = BST()
    b.insert(a)
    b.insert(c)
    b.insert(d)
    b.insert(e)
    b.insert(f)
    b.insert(g)
    b.inorderwalk(a)
    print("___")
    b.delete(a)
    b.delete(d)
    b.inorderwalk(c)


if __name__ == "__main__":
    main()


