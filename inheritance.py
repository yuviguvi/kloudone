class base(object):
    def __init__(self,name):
        self.name=name
    def getname(self):
        return self.name
class child(base):
    def __init__(self,name,age):
        base.__init__(self,name)#initiating of parent to child
        self.age=age
    def getage(self):
        return self.age
class grandchild(child):
    def __init__(self,name,age,address):
        child.__init__(self,name,age)#initiating process
        self.address=address
    def getaddress(self):
        return self.address
obj=grandchild("Yuvi",21,"divya")
print(obj.getname(),obj.getage(),obj.getaddress())
