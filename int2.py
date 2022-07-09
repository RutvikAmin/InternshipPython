
#comments in python

#this is comment

'''
this is
multiline 
comment
'''

"""
this 
is also 
multiline 
comment

"""

#declaring variable

a = 10
b = 20
c = 30

print(a)
print(b)
print(c)


#changing the value of variable
#here we change value of a
#example 1
a = 30
b = 20

print(a)

#example 2

Name = "Jay Patel"
print(Name)

#here we change the value of Name

Name = "Meet Patel"
print(Name)

#Assigning multiple values to multiple variables

a,b,c = 10,20,"Jay Patel"

print('1st element number is', + a)
print("2nd element number is",b)
print("my name is :", c)


#Assign same value to multiple variable

a=b=c = 13
print(a,b,c)

#Datatypes

#Number Data types
#Int, Float, Complex

#1 int

a = 10
print(a)
print('variable type is : ', type(a))

#2 float

f = 2.3
print(f)
print('variable type is : ', type(f))

#3 complex Numbers

c = 10+20j
print(c)
print('variable type is : ',  type(c))

#String Datatypes

name = 'JayPatel'
print('want first letter:', name[0])
print('want second  letter : ', name[1])
print('third letter:',name[2])
print('full name:', name)
print(name[1:4])
print(name[:1])
print(name[2:])
print(name[:])
print('type two times:', name * 2)

#list data types

l = [1, 2, 'jay', 3, 'Mahendra', 4, 'Patel', 5, 6, 7]
print(l)
print(type(l))
print(l[1])
print(l[2:5])
print(l[5:])





#tuple data types  we can't change the value of variable in tuple after assigning it will show error

t = (1, 2, 3, 'Jay', 4, 'Patel', 5, 6)
print(t)
print(type(t))
print(t[4])
print(t[2:5])
print(t[2:])
print(t[:4])

#Dictionary Data types

d = {1: "Mahendra",  3: 'Jay', 4:'Patel'}
print(d)
print(type(d))
print(d[3])

# Taking value from user in List

# Creating empty list
lst = []

# number of element as input
n = int(input("enter number of elements: "))

# iterating till the range
for i in range(0, n):
    ele = input("Enter value of elements")

    lst.append(ele)  # adding the element

    print(lst)

# Taking the value from user in tuple

tst = []

n = int(input("Enter the number of element: "))

for i in range(0, n):
    ele = input("Enter the value: ")
    tst.append(ele)

    tup1 = tuple(tst)
    print(tst)
    print(tup1)

# Taking value from user in dictionary

d1 = {}

n = int(input("Enter number of element: "))

for i in range(0, n):
    a, b = input("Enter key value pair data").split()
    d1[a] = [b]
    print(d1)
