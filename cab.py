class ola:
    def _int_(self,prime_sedan,jeep,toyota,maruti_ritz,maruti_alto):
        self.p=prime_sedan
        self.j=jeep
        self.t=toyota
        self.r=maruti_ritz
        self.a=maruti_alto
    def car_list(self):
        num=input(""" List of the car's available:
                            1.prime_sedan=6 seats
                            2.jeep=6 seats
                            3.toyota=4 seats
                            4.maruti_ritz=4 seats
                            5.maruti_alto=4 seats """)
        print(num)
    def car_name(self):
        var=input("Enter car no:")
        if var=='1':
            print(self.p)
        elif var=='2':
            print(self.j)
        elif var=='3':
            print(self.t)
        elif var=='4':
            print(self.r)
        elif var=='5':
            print(self.a)    
        else:
            print("cars not available")
            exit(0)
class travel(ola):
    def _int_(self,distance):
        self.f=distance
    def km(self):
        num1=int(input("Enter total km to be travel:")
        print(num1*7)         
c=ola('','','','','')
c.car_list()
c.car_name()
cab=travel('')
cab.km()                 
                 
                 


        

