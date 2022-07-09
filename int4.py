
#conditional statement
#if statement
x = 23
y = 45
if x > y:
    print("x is greater than y")
if y > x:
    print("y is greater than x")
#if else statement
x = 45
y = 22

if x > y:
    print("x is grater than y")
else:
    print("y is greater than x")
#if elif else statement
x = 98
y = 98
if x > y:
    print("x is grater than y" )
elif x == y:
    print("x and y is same")
else:
    print("y is greater than x")
#nested if statement
x = 30
if x >= 0:
    if x == 0:
        print("x is zero")
    else:
        print("x is positive number")
else:
    print(" x is negative number")

#loop statement
#while loop
i = 0

while i <= 6:
    print("value of i", i)
    i += 2

#For loop
#example 1

for i in "Jay":
    print("Value:", i)

#example 2  in list
list = [3, 6, 45, 6, 37, 65, 77]
for f in list:
    print("value of", f)

#nested for loop
a = ["red", "big", "tasty"]
b = ["apple", "banana", "cherry"]

for x in a:
  for y in b:
    print(x, y)

# The range() function

for x in range(10):
    print(x)
for y in range(5, 9):
    print("y is ", y)
for y in range(5, 8, 3):
    print("Take jump of 3 ", y)

# len() function

i = [3, 7, 8, 87, 65, 54, 34, 67, 75, 66]
for z in range(len(i)):
    print(i[z])

#loop with else

i = [3, 7, 8, 87, 65, 54, 34, 67, 75, 66]

for s in range(len(i)):
     print(i[s])
else:
     print("no elements left")

#break and continue while

m = 0
while m < 67:
    print(m)
    m += 2
    if m > 5:
        break


for y in range(20):
    if y % 9 == 0:
        continue
    print(y)

#pass

g = {2, 5, 7, 8}
for val in g:
    pass