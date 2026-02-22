# Day 3 - String Methods and Operations

fname="nish"
lname="Aradhya"
# Concatenating first and last name
print (fname + " " + lname)

# String repetition
name ="nishitha   " * 10
print(name)

x=10
y=20
print(x+y)

# Basic arithmetic with user input
a=int(input("enter a number: "))
b=int(input("enter b number: "))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)

# String methods
print(fname.upper())
print(lname.lower())
print(fname.capitalize())
print(fname.split())
print(fname.islower())
print(fname.isupper())
print(fname.replace("nish","nishitha"))

# String indexing and slicing
print(fname[0])
print(lname[0:2])
print(lname[2:])
print(lname[:3])
print(lname[-2])
print(lname[:-3])

# Length of string
print(len(lname))
