class cal1:

    def setdata(self,n1,n2,n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def display(self):
        sum = self.n1 + self.n2 + self.n3
        print("Sum is : " , sum)

obj = cal1()
obj.setdata(10,20,30)
obj.display()

print("---------------------------------------------------------------")

class cal2:
    def setdata(self):
        self.r = int(input("Enter radius :"))

    def area(self):
        self.ar = 3.14 * (self.r**2)
        
    def display(self):
        print("Area of square : ",self.ar)

obj = cal2()
obj.setdata()
obj.area()
obj.display()

print("---------------------------------------------------------------")

class cal3:
    def __init__(self, p , r, n):
        self.p = p
        self.r = r
        self.n = n
    
    def callinterest(self):
        self.inte = (self.p*self.r*self.n)/100

    def display(self):
        print("Interest : ",self.inte)

obj = cal3(5000,5,1)

obj.callinterest()
obj.display()

print("---------------------------------------------------------------")

class cal4:
    def setdata(self,num):
        self.num = num

    def display(self):
        return self.num**2
        

obj = cal4()
obj.setdata(10)
print(obj.display())

print("---------------------------------------------------------------")

class cal5:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    
    def calArea(self):
        self.ar = self.l * self.b

    def display(self):
        print("Area of Rectangle : ",self.ar)

obj = cal5(10,20)
obj.calArea()
obj.display()

print("---------------------------------------------------------------")

class cal6:
    def setdata(self):
        self.len = int(input("Enter length :"))

    def area(self):
        self.ar = (self.len**2)
        
    def display(self):
        print("Area of square : ",self.ar)

obj = cal6()
obj.setdata()
obj.area()
obj.display()

print("---------------------------------------------------------------")

class employee:
    name = ""
    designation = ""


class subclass(employee):

    def fun1(self, name, designation):
        self.name = name
        self.designation = designation
        print("Name: ",self.name)
        print("Designation: ",self.designation)

    def fun2(self,salary):
        self.salary = salary
        print("Salary : ",self.salary)

c = subclass()
c.fun2(50000)
c.fun1("Jhanvi","SE")

print("---------------------------------------------------------------")

class publisher:
    def fun(self,title):
         self.title = title
         print("Title : ",self.title)

class book(publisher):
   
    def fun1(self, pageno):
        self.pageno = pageno
        print("pageno: ",self.pageno)

class tape(publisher):
    def fun2(self,time):
        self.time = time
        print("time: ",self.time)

obj1 = tape()
obj2 = book()
obj1.fun("Wings of fire")
obj1.fun2("150minutes")
obj2.fun1("300")

print("---------------------------------------------------------------")

class scheme:
    scheme_id= outgoing_rate = message_charge = 0
    scheme_name=""
class customer(scheme):
    cust_id=mobile_no=0
    name=""
    def setdata(self,scheme_id,name,rate,charge,cust_id,mno):
        self.scheme_id = scheme_id
        self.scheme_name = name
        self.outgoing_rate = rate
        self.message_charge = charge
        self.cust_id = cust_id
        self.mobile_no = mno
    def display(self):
        print("The scheme id is ",self.scheme_id)
        print("The name of scheme is",self.name)
        print("The outgoing rate is ",self.outgoing_rate)
        print("The message charge is ",self.message_charge)
        print("The customer id is ",self.cust_id)
        print("The customer mobile number is ",self.mobile_no)
obj = customer()
obj.setdata(201,"Business plan","13","10","77",9876543210)
obj.display()

print("---------------------------------------------------------------")

class arith:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        sum = self.n1 + self.n2
        return sum 

    def subract(self):
        sub = self.n1-self.n2
        return sub

    def multiply(self):
        mul = self.n1*self.n2
        return mul

obj = arith(10,5)
print(obj.add())
print(obj.subract())
print(obj.multiply())