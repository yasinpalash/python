"""
Definition:
A variable is a container used to store data values in memory.

Python is a dynamically typed language, which means:
- You do NOT need to declare the data type explicitly.
- Python automatically determines the data type.

Example:
x = 10

Here:
x = variable name
10 = value stored inside the variable
"""
# ------------------------------------------------------
# 1. Creating Variables
# ------------------------------------------------------

# A variable can store numbers
age=25

# A variable can store text (string)
name="Yasin"
# A variable can store decimal numbers (float)
height=7.56


# Printing variables
print(age)
print(name)
print(height)

# ------------------------------------------------------
# 2. Multiple Variable Assignment
# ------------------------------------------------------

# Python allows assigning multiple variables in one line

x,y,z=1,2,3

print(x)
print(y)
print(z)

# ------------------------------------------------------
# 3. Assign Same Value to Multiple Variables
# ------------------------------------------------------

a=b=c=100

print(a)
print(b)
print(c)

# ------------------------------------------------------
# 4. Variable Naming Rules
# ------------------------------------------------------

"""
Rules for naming variables in Python:

1. Variable names must start with a letter or underscore (_)
2. Variable names cannot start with a number
3. Variable names can contain letters, numbers, and underscores
4. Variable names are case-sensitive

Valid examples:
user_name
_user
age1

Invalid examples:
1age
user-name
"""

user_name = "Yasin"
_user = "Developer"
age1 = 26

# ------------------------------------------------------
# 5. Case Sensitivity
# ------------------------------------------------------

"""
Python variables are case-sensitive.
That means these are different variables:
"""

name = "Yasin"
Name = "Palash"

print(name)
print(Name)

# ------------------------------------------------------
# 6. Checking Variable Type
# ------------------------------------------------------

"""
Python provides the type() function to check the data type
stored in a variable.
"""

age = 25
price = 19.99
language = "Python"

print(type(age))        # int
print(type(price))      # float
print(type(language))   # str


# ------------------------------------------------------
# 7. Updating Variables
# ------------------------------------------------------

"""
Variables can be updated or reassigned anytime.
"""

score = 50
print(score)

score = 90
print(score)


# ------------------------------------------------------
# 8. Deleting Variables
# ------------------------------------------------------

"""
Python allows deleting variables using the 'del' keyword.
"""

temp_value=100
print(temp_value)

del  temp_value
# print(temp_value)  # This would cause an error

# ------------------------------------------------------
# 8. Type Casting a Variable
# ------------------------------------------------------

"""Type casting is the process of converting a variable from one data type to another.
"""
s = "10"  
n = int(s)

cnt = 5
f = float(cnt) 

age = 25
s2 = str(age)  

print(n)  
print(f)  
print(s2)


