#user defined function
#no argument no return type
def jay():
    print("Hello how are you")

jay()    #you can use as many time you want to print
jay()
jay()

#argument with return type
def jack(name):
    return name

name = jack("pirates caribian")
print(name)

#argument with no return type
def sparrow(book):
    print("print that", book)

sparrow("i'm your fan")

#multiple rerturn statement
def michel():
    name = "Jaypatel"
    contact = 345345345
    return name, contact

name, contact = michel()
print("name: ", name)
print("contact: ", contact)


#default arguments

def sum(a = 6 , b = 5):
    print(a + b)
sum(10, 20)
sum()

#keyword arguments

def num(a, b):
    print(a + b)

num(b = 10, a = 30)



#Non keyword arguments

def men(*num):
    sum = 0

    for k in num:
        sum = sum + k
        print("sum", sum)



men(10, 50)
men(10, 50, 60)

#*args arguments non key word arguments

def add(*num):
    sum = 0

    for n in num:
        sum = sum + n
    print("sum", sum)

add(10, 20)
add(10, 20, 30)

#**kwargs keyword arguments

def my_function(**args):
    for i, j in args.items():
        print(i, j)

my_function(name = "jay patel", age = "20",)

#global variable

def my_fun():
    x = 20
    print("value inside function", x)

x = 30
my_fun()
print("value outside function", x)




