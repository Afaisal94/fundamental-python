'''
--- NOTES PYTHON ---
'''

# Hello world
print('Hello world')

print('-' * 20)

# IF
if 5 > 2:
  print('Five is greater than two!')

print('-' * 20)

# Variables
x = 5
y = "John"
print(x)
print(y)


'''
Penulisan variable yang baik
Camel Case => myVariableName
Pascal Case => MyVariableName
Snake Case => my_variable_name
'''

print('-' * 20)

# Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print('-' * 20)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

print('-' * 20)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print('-' * 20)


# Output Variables
x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z = x + y
print(z)

print('-' * 20)


# Function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


print('-' * 20)


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

print('-' * 20)

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

print('-' * 20)


# Random Number
import random
print(random.randrange(1, 10))

print('-' * 20)

# String Length
a = "Hello, World!"
print(len(a))

print('-' * 20)

# Check String
txt = "The best things in life are free!"
print("free" in txt)



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



txt = "The best things in life are free!"
print("expensive" not in txt)



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("Yes, 'expensive' is NOT present.")

print('-' * 20)

# Slicing
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
b = "Hello, World!"
print(b[:5])

# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative slicing
b = "Hello, World!"
print(b[-5:-2])


'''
Modify Strings

print(a.upper())
print(a.lower())
'''

# Remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)



a = "Hello"
b = "World"
c = a + " " + b
print(c)

print('-' * 20)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))



quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Boolean Values
print(10 > 9)
print(10 == 9)
print(10 < 9)



a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

