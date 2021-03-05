
"""
phrase = "Welcome to Python world"
print(phrase.upper().isupper())  # runs upper func tion n gives u the value true or false

phrase1 = "Welcome to Python"
print(len(phrase))   # length of the whole thin

# indexing starts with 0
        #  0123...
phrase1 = "Welcome to Python"
print(phrase1[0])

phrase1 = "Welcome to Python"
print(phrase1[3])

# returns the index of capital W
phrase1 = "Welcome to Python"
print(phrase1.index("W"))
print(phrase1.index("o"))

print(phrase1.replace("Python", "world"))

for x in "bananna":
    print(x)

print(3*4.5 )

num = 5
print(pow(3, 2)) # like 3 square

print(round(6.4))

from math import *   # to use below math functions we need to impoert the math

print(floor(3.7))
print(ceil(4.5)) # rounds value up
print(sqrt(64))

# to store whtever user inputed into variable
#name = input("Enter your name:")
#print("Hello " + name)

#more than one piece of information

#name = input("Enter your name:")
#age = input("Enter your age:")
#print("Hello " + name + "! You are " + age)

# basic calculator

num1 = input("enter the number:");
num2 = input("enter another number ")
#result = num1 + num2
#print(result)    # 12 + 1=result came as 121
# python considrng it as stroing and conctinating ,,we need to convert it to numbrs
# give int

result = int(num1) + int(num2)
print(result)

#List functions..
myList = [4, 8, 12, 34]
new = ["Jack", "Rosy", "Kelvin", "Kevin"]
new.remove("Rosy")
print(new)

"""
#To add two numbers
"""
x = input("enter a numbr: ")

y = input("enter anothe rnumber: ")
sum = float(x) + float(y)
print(sum)
"""
# OR

# print('The sum is %.1f' %(float(input('enter first number: ')) + float(input('Enter second number: '))))

#traingle area
"""
a = 4
b = 5
c = 6

#calclte the semi-prmeter
s = (a+b+c)/2

#calculate the area

area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("the area of triangle is %0.2f" %area)

#SWPING TWO VARBLES

x = 5
y = 10
# crtng tempry vrble n swping
temp = x
x = y
y = temp

print('The value of x after swppng: {}'.format(x))
print('The value of y after swppng: {}'.format(y))

#swping withou using temp varble

x = 5
y = 10

x, y = y, x
print("x =",x)
print("y =",y)

"""
"""
if 5>2:
    print("five is greater than 2")
# if true prints first print stmnt otherwise nxt print statmnt.
is_hot = True

if is_hot:
    print("Its'a hot day")
    print('drink plenty of water')
else:
    print('enjoy ur day')

###########33333333

x = ["ant","bat","cat"]
print(type(x))

y = ("ant","bat","cat")
print(type(y))

z = {'name' : "john", 'age':36}
print(type(z))

txt = 'best things in life are free'
if 'expensive' not in txt:
    print("yes,'expensve' not present")

a = '  hello   '
print(a.strip())



# friends = ['kevin', 'kevin', 'smith','john','oscar']
# friends.insert(1, 'stupid')
# print(friends.index('kevin'))  # index of kevin
# print(friends.count('kevin'))  # counts how mant times it has kevin

"""
"""
# tuple is immmutable= cant be chnged or modified
first_tuple = (4, 5, 6)
#trying to chnge the objct in tuple(u will get an error can't chnge/modify)
#first_tuple[1] = 10

print(first_tuple[2])

x = [(4, 5), (6, 7), (78, 90)]
print(x[2])
"""
# FUNCTIONS

def func1():
    print('hello user')

print('top')
func1()
print('bottom')
"""
OUTPUT LUKS L.IKE
top
hello user
bottom
"""

"""
def tuples():
    if 5 > 2:
        print('five is greater  than two')
    else:
        print('five is not greater than two')

tuples()

def func2(name, age):
    print("Hello " + name + ", you are " + age)

func2("kreepy", "23")



tuple = ("apple", "banana", "polity")
for i in range(len(tuple)):
    print(tuple[i])

a = 'hello world!'
x = 0
for b in a:
    print(a[x])
    x+=1
"""

a = 'hello world!'
b = a[0:]
c = a[6:12]
print(b, '+' ,c)











