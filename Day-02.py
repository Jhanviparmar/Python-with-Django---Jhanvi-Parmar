#Day-02
print("Day-02")
#PYTHON COMMENTS

print("Hello")

print("------------------------------------------------")
#print("World")
'''This is multiline comment'''

#VARIABLES IN PYTHON
print("VARIABLES IN PYTHON")
a = 10
b = 10.5
c = "aa"
print("a = ",a,"type of a=",type(a))
print("b = ",b,"type of a=",type(b))
print("c = ",c,"type of a=",type(c))

print("------------------------------------------------")

#ASSIGNING VALUES IN SINGLE LINE
print("ASSIGNING VALUES IN SINGLE LINE")
a,b,c = 10, 10.5, "aa"
print("a = ",a,"type of a=",type(a))
print("b = ",b,"type of a=",type(b))
print("c = ",c,"type of a=",type(c))

print("------------------------------------------------")

#ASSIGNING SAME VALUES TO DIIFERENT VARIABLES
print("ASSIGNING SAME VALUES TO DIIFERENT VARIABLES")
a = b = c = 10
print("a = ",a,"b = ",b,"c = ",c)

print("------------------------------------------------")

#CHANGING THE VALUE OF VARIABLE
print("CHANGING THE VALUE OF VARIABLE")
name = "Jhanvi"
print("Name is "+name)

name = "Khushi"
print("Name is "+name)

print("------------------------------------------------")

#PYTHON DATATYPES
print("PYTHON DATATYPES")
#NUMBER DATATYPES
print("NUMBER DATATYPES")
n1 = 10
print(n1, "is type of", type(n1))
n2 = 10.5
print(n2, "is type of", type(n2))
print(n2, "is int number? : ",isinstance(10.5,int))
print("------------------------------------------------")

#STRING DATATYPES
print("STRING DATATYPES")
name = "Python Django"
print("name is: ", name)
print(name[0])
print(name[2:5])
print(name[4:])
print(name[:5])
print(name * 2)
print(name + " framework")
print("------------------------------------------------")

#LIST DATATYPE
print("LIST DATATYPES")
list1 = [10, 20.5, "aa", "##"]
print(list1)
#UPDATING VALUES AS LIST IS MUTABLE
print("UPDATING VALUES AS LIST IS MUTABLE")
list1[1] = 10.5
print(list1)
#SLICING THE LIST
print("SLICING THE LIST")
print(list1[2:4])
print("------------------------------------------------")

#TUPLE DATATYPE
print("TUPLE DATATYPE")
tuple1 = (10, 20.5, "aa", "##")
print(tuple1)
#UPDATING VALUES WILL THROW AN ERROR AS TUPLES ARE IMMUTABLE
print("UPDATING VALUES WILL THROW AN ERROR AS TUPLES ARE IMMUTABLE")
"""tuple1[1] = 10.5
print(tuple1)"""
#SLICING THE TUPLE
print("SLICING THE TUPLE")
print(tuple1[2:4])
print("------------------------------------------------")

#DICTIONARY DATATYPE
print("DICTIONARY DATATYPE")
dict= {1:"aa", "python" : "code", "num" : 2}
print(type(dict))
print("dict[1]= ",dict[1])
print("dict['python']= ",dict["python"])
print("dict['num']= ",dict["num"])
