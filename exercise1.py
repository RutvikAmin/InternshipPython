'''
# 1
# calculate area of rectangle
#A = wl
#w= width, v = length

w = 20
v = 30

A = w*v

print("area of rectangle", A)


w = int(input("enter the width of rectangle"))
v = int(input("enter the length of rectangle"))

A = w*v

print("area of rectangle", A)

#2
#calculate area of square
# A = (l*l)

l = 3

A = l*l
print("area of square", A)

k = int(input("enter the value of length"))
A = k**2
print("Area of square", A)


#3
#calculate the area of circle
#A = PI(r**2)

r = 4
pi = 3.14

A = pi*(r**2)

print("Area of circle", A)

r = int(input("Enter the radius"))
pi = float(3.14)

A = pi*(r**2)

print("Area of circle", A)

#4
#calculate average of 5 numbers
a, b, c, d, e = 3, 4, 6, 7, 8

ave = (a+b+c+d+e)/5

print("average", ave)

a = int(input("first number"))
b = int(input("second number"))
c = int(input("third number"))
d = int(input("forth number"))
e = int(input("fifth number"))

Ave = (a+b+c+d+e)/5

print("Average of user 5 numbers", Ave)


#5
#check whether number is even or odd

number = int(input("enter any number"))
if number % 2 == 0:
     print("number is even")
else:
     print("number is odd")


#6take a year and check whether leap year or not

year = int(input("enter thr year : "))

if year % 4 == 0:
    print("Year is leap year")
else:
    print(" it is not leap year")



#7 Take a number check whether it is zero, positive or negative

a = int(input("Enter a number:"))

if a == 0:
    print("it is zero")
if a > 0:
        print("it is positive")
else:
        print("it is negative")

#8 take two numbers and display greatest number

e1 = int(input("First number"))
e2 = int(input("second number"))

if e1 > e2:
    print("e1 number is greater")
else:
    print("e2 number is greater")



#9 Take a number and find factorial of that number

n = int(input("enter a number"))
f = 1
if n == 0:
    print("1")
if n < 0:
    print("factorial does not exist")
if n >= 1:
  for i in range(1, n+1):
      f = f * i
print(f)

#10 write a program to swap 2 numbers

a = 20
b = 30

# before swaping
print("a:", a)
print("b:", b)

c = a
a = b
b = c

# after swaping
print("a:", a)
print("b:", b)

# without third variable
a = 90
b = 60

a = a + b
b = a - b
a = a - b
print(a)
print(b)


#11 take two number and find smallest

n1 = int(input("enter first number"))
n2 = int(input("enter second number"))

if n1 < n2:
    print("n1 is smallest")
else:
    print("n2 is smallest")

#12. Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even

n = int(input("enter a number"))
while n < 100:
    if n % 2 == 0:
        print("even")
        break
    else:
        print("odd")
        break
if n > 100:
    print("no solution")

#13 13. Take a number to print the square of a number if it is less than 10.

s = int(input("enter number"))
k = s * s
if s < 10:
    print("square of number", k)
else:
    print("number is greater than 10")
'''

#14. Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

f = int(input("enter a number"))

if f >= 0:
   if f == 0:
      print("it is zero")
   else:
      print("it is positive")
else:
   print("it is negative")


#15. Write a program to swap 2 numbers without taking third variable

a = 23
b = 34

a = a + b
b = a - b
a = a - b

print("after swaping",a)
print("after swaping",b)

#Take starting number and ending number from the user and print following series.

start = int(input("enter starting number"))
end = int(input("enter ending number"))

#30 27 24 21 18 15 12 9 6 3 0
for i in range(0, 31):
     if i % 3 == 0:
         f = start - i
         print(f)
