class taxi(object):
    def __init__(self,name,pickloc,droploc):
        self.name=name
        self.pickloc=pickloc
        self.droploc=droploc
    def getname(self):
        return self.name
    def getpickloc(self):
        return self.pickloc
    def getdroploc(self):
        return self.droploc
class travel(taxi):
    def __init__(self,name,pickloc,droploc,seat,p2,p3):
        taxi.__init__(self,name,pickloc,droploc)
        self.seat=seat
        self.p2=p2
        self.p3=p3
    def seat(self):
        var=input("enter the number of seats:")
        print(var)
    def p2(self):
        var1=input("enter the total km of travel:")
        print(var1*7)
    def p3(self):
        var2=input("enter the total km of travel:")
        print(var2*21)
class end(travel):
    def __init__(self,name,pickloc,droploc,seat,p2,p3):
        travel.__init__(self,name,pickloc,droploc,seat,p2,p3)
        self.seat()
        if self ==4:
            self.p2()
        elif self ==6:
            self.p3()
obj=end("YUVI","tondiarpet","crossroad",4,2,2)
print(obj.getname(),obj.getpickloc(),obj.getdroploc(),obj.seat(),obj.p2(),obj.p3())

