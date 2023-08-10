# String concatenation - merge two strings to become one using the + operator
first = "I am a programming language"
second = "Me too, I just became one!"

print(first + " " + second)

# Operators
# Mathematical : +,-,/,*,**,//,%
x = 10 + 10 # Addition
y = 200 - 50 # Subtraction
z = 200 / 5 # Division
w = 20 * 5 # Multiplication
s = 7 // 3 # Floor division - division that gets only the whole number
t = 7 % 3 # Modulus/Modulo - remainder after a division
r = 6 ** 2 # Raised to power (exponential) == 36

print("This is the Addition (+) operator", x)
print("This is the Subtraction (-) operator", y)
print("This is the Division (/) operator", z)
print("This is the Multiplication (*) operator", w)
print("This is the Floor division (//) operator", s)
print("This is the Modulo (%) operator", t)
print("This is the Raised to Power (**) operator", t)

# Comparison : !=, ==, <, >, <=, >=. This always returns a boolean
a = 2 != 20 # Not equal to
b = 3 == 3 # Equal to 
c = 4 < 6 # Less than
d = 7 > 2 # Greater than
e = 8 <= 8 # Less than or equal to
f = 9 >= 4 # Greater than or equal to 

# Assignment : =, +=, *=, -=, /=. Used for assigning a value to a variable
g = 90 # Assignment
print("The current value of variable g is", g)
g += 3 # It will add 3 to every value of g and save it back to g
print("The current value of variable g is", g)
g *= 3 # It will multiply the value of g by 3 and save it back to g
print("The current value of variable g is", g)
g -= 30 # Subtract 3 from the value of g and save it back
print("The current value of variable g is", g)
g /= 9 # Divide the value of g by 9 and save it back
print("The current value of variable g is", g)

# Membership : in, not in - Whether a value belongs in a collection, Always return boolean
who = "i" in "whoami" # checks if i is in the string
two = 2 in [0, '2', 4, 8, 90] # checks if 2 is present in the list
who_2 = "i" not in "whoami" # Checks if the value does not exist there

# Identity: is, is not
"Fair" is not True
"Dark" is False


# Logical : and, not, or. Logical operators tries to resolve what is true or not
True and False and True # False
False or False or False or False or True # Only one needs to be true for tit to be true