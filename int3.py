#python class
#i/ofunctions&operations

#input and output #Example 1

n1 = input("Enter number : ")   #it is for input
print("Value of user input:", n1)

#Example 2

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

ans = n1+n2

print("Addition of two number:" , ans)

#operators in python

#1 Arithmetic operators

x = 50
y = 20

print("Addition of two numbers:", x+y)
print("Substraction of two numbers:", x-y)
print("Multiply two numbers:", x*y)
print("Divide two numbers:", x/y)
print("power of x^y:", x**y)
print("divide and output in not decimal, only int:", x//y)
print("remainder of x%y:", x%y)





#2 comparison operators

x = 45
y = 7

print("x is greater than y:", x>y)
print("x is greater than y or equal to zero:", x>=y)
print("Y is greater than x", y>x)
print("Y is greater than x or equal to zero:", x<=y)
print("x is not equal to y:", x!=y)
print("x is equal to y:", x==y)



#logical operators

#and

a = 10
b = 25
c = 45

if a > b and a > c:
  print("a  largest number")
if b > a and b > c:
  print("b  largest nummber")
if c > a and c > b:
  print("c  largest number")

#or

n1 = input("Enter any english letter")

if (n1 == 'd' or n1 == 'b' or n1 == 'c' or n1 == 'd' or  n1 == 'e' or n1 == 'f'):
   print(n1, "I like it")

else:
   print("I do not like it")


#not

a = 20

if not a > 12:
 print("its true")
else:
 print("its false")


#assignment operators

x=5
print(x)

x+=3
print(x)

x-=3
print(x)

x*=3
print(x)

x/=3
print(x)

x%=3
print(x)

x = 15

x//=2
print(x)

x**=3
print(x)


#Membership operators

x = 10
y = 34

list = [13, 23, 34, 24]
print(x in list)
print(y in list)
print(x not in  list)
print(y not in list)



#identity operators

x = 23
y = 23

print(x is y)
print(x is not y)
