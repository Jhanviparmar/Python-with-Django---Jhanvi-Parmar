def myfun():
    print("Hello world")
myfun() #calling function

def myfunction(name):
    print("My name is : ",name)
myfunction("Jhanvi")

def my_fun(name):
    return name
name = my_fun("Jhanvi Parmar")
print(name)

def my_function():
    name = "Jhanvi Parmar"
    collage = "LJIET"
    return name,collage
name,collage = my_function()
print("name : ",name)
print("collage : ",collage)
print("--------------------------------------------------")

def sum(a=5,b=10): #default arguments
    print(a+b)
sum(10,20) #calling with new arguments
sum() #calling with default arguments

def sum(a,b):
    print("Sum is : ",a+b)
sum(b=10, a=5) #keyword arguments

def add(*num): #variable length non-keyword arguments
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum : ",sum)
add(10,20) 
add(10,20,30)

def myfun(**arg): #variable length non-keyword arguments
    for i,j in arg.items():
        print(i,j)
myfun(Name = "Jhanvi", Surname = "Parmar") 

def myfun():
    x = 10 #local variable
    print("Value inside the function: ",x)
x = 20 #global variable
myfun()
print("Value outside the function: ",x)
print("----------------------------------------------------")
x = 13
y = 4
print("x+y : ",x+y) #arithmetic operators
print("x-y : ",x-y)
print("x*y : ",x*y)
print("x/y : ",x/y)
print("x//y : ",x//y)
print("x**y : ",x**y)
print("----------------------------------------------------")
print(">+y : ",x>y) #comparision operators
print("x<y : ",x<y)
print("x==y : ",x==y)
print("x!=y : ",x!=y)
print("x<=y : ",x<=y)
print("x>=y : ",x>=y)
print("----------------------------------------------------")
x = 1 
y = 0
print(x and y) #logical operators
print(x or y)
print("----------------------------------------------------")
print(x is y) #identity operator
print("----------------------------------------------------")
x = [10,20,30]
print(10 in x) #membership operator
print(30 not in x)
