print("Problem Statement-01 : Calculate average of 5 numbers.")
n1 = int(input("Enter 1st number: "))
n2 = int(input("Enter 2nd number: "))
n3 = int(input("Enter 3rd number: "))
n4 = int(input("Enter 4th number: "))
n5 = int(input("Enter 5th number: "))
avg = (n1+n2+n3+n4+n5)/5
print("Average of five numbers is :",avg)
print("-----------------------------------"

print("Problem Statement-02 : Check whether number is even or odd.")
n = int(input("Enter a number: "))
if n % 2 == 0:
	print("Given number is even.")
else:
	print("Given number is odd.")
print("-----------------------------------")

print("Problem Statement-03 : Take a year and check whether it is leap year or not")
year = int(input("Enter a year :"))
if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
			print("Giver year is leap year")
else:
	print("Given year is not leap year")

print("-----------------------------------")

print("Problem Statement-04 : Take a number and check whether it is zero, positive or negative.")
n = int(input("Enter a number: "))
if n == 0:
	print("Given number is zero.")
elif n>0:
	print("Given number is positive.")
else:
	print("Given number is negative.")
print("-----------------------------------")
print("Problem Statement-05 : Take 2 numbers and display greatest number. Also check equal number condition")
n1 = int(input("Enter n1 number :"))
n2 = int(input("Enter n2 number :"))
if n1==n2:
	print("Both numbers are eqaul.")
elif n1>n2:
	print("n1 is greater than n2")
else:
	print("n2 is greater than n1")
print("-----------------------------------")
print("Problem Statement-06 : Take a number and find factorial of that number")
n = int(input("Enter a number: "))
fact = 1
while n !=0 :
	fact = fact * n
	n = n-1
print("factorial of given number is =" ,fact)
print("-----------------------------------")
print("Problem Statement-07 : Write a program to swap 2 numbers using third variable.")
n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
print("Before swapping n1= ",n1)
print("Before swapping n2= ",n2)
a = n1
n1 = n2
n2 = a
print("After swapping n1= ",n1)
print("After swapping n2= ",n2)
print("-----------------------------------")
print("Problem Statement-08 : Take 2 numbers and find smallest number.")
n1 = int(input("Enter n1 number :"))
n2 = int(input("Enter n2 number :"))
if n1==n2:
	print("Both numbers are eqaul.")
elif n1<n2:
	print("n1 is smaller than n2")
else:
	print("n2 is smaller than n1")
print("-----------------------------------")
print("Problem Statement-09 : Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.")
n = int(input("Enter a number : "))
if n < 100:
    if n % 2 == 0:
	    print("Given number is even.")
    else:
	    print("Given number is odd.")
else:
	print("Given number is greater than 100")
print("-----------------------------------")
print("Problem Statement-10 : Take a number to print the square of a number if it is less than 10.")
n = int(input("Enter a number : "))
if n < 10:
	sqrt = n * n
	print("Square of number n =", sqrt)
else:
	print("number is greater than 10")
print("-----------------------------------")
print("Problem Statement-11 : Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .")
n = int(input("Enter a number : "))
if n == 0 or n > 0:
	if n == 0:
		print("Given number is zero")
	else:
		print("Given number is positive")
else:
	print("Given number is negative")
print("-----------------------------------")
print("Problem Statement-12 : Take 3 numbers and find greatest number using nested IF….ELSE statement.")
n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))
if n1>n2 : 
	if n1>n3:
		print("n1 is greater")
	else:
		print("n3 is greater")
else:
	if n2>n3:
		print("n2 is greater")
	else:
		print("n3 is greater")
print("-----------------------------------")
print("Problem Statement-13 : Take 3 numbers and find smallest number using logical operator.")
n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
n3 = int(input("Enter n3 : "))
if n1<n2 : 
	if n1<n3:
		print("n1 is smaller")
	else:
		print("n3 is smaller")
else:
	if n2<n3:
		print("n2 is smaller")
	else:
		print("n3 is smaller")
print("-----------------------------------")
print("Problem Statement-14 : Write a program to swap 2 numbers without taking third variable.")
n1 = int(input("Enter n1 : "))
n2 = int(input("Enter n2 : "))
print("Before swapping n1 =",n1)
print("Before swapping n2 =",n2)
n1 , n2 = n2 ,n1
print("After swapping n1 =",n1)
print("After swapping n2 =",n2)
print("-----------------------------------")
print("Problem Statement-15 : Take starting number and ending number from the user and print following series.")
n1 = int(input("Enter starting number :"))
n2 = int(input("Enter ending number : "))
while n1 >= n2:
	print(n1)
	n1 = n1-3'''
