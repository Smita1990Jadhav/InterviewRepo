from classnmethos import cal


class calchild(cal):
    num2=10
    def __init__(self):
        cal.__init__(self,3,3)
    def getcompletedata(self):
        return calchild.num2+self.num+self.add()

obj2=calchild()
print(obj2.getcompletedata())