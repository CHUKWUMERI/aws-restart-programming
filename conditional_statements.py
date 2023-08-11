# This script holds the first conditional statements we will interact with in python
# IF, ELIF and ELSE statement
# If statement checks if a condition is true and runs an accompanying block of code

# Syntax 
# if condition:
#   # code to be run
# elif condition:
    # code to be run 
# ... multiple elif statements
# else:
    # code to be run 

# Example Store that closes by say 10pm and opens 7am
time = 23 # Using a 24 hour timing
if time < 7 or time > 22:
    print("Store is closed!")
elif time >= 7 and time <= 22: # and operator
    print("Store is open!")


if time >= 7 and time <= 22: # and operator
    print("Store is open!")
else:
    print("Store is closed!")


# If gas tank is below a 40% of the full gas level turn on fuel warning
full_gas_level = 100
current_gas_level = 60

if current_gas_level < (0.4 * full_gas_level): # 0.4 was used to multiply to get 40% of the gas level
    print("Fuel Warning Lights on!")

# Evander's Code
age = 18

if age >= 18:
    print("You are an adult!")
elif age < 18 and age > 13:
    print("You are a teen!")
else:
    print("You are a child!")

# # Jin
# age = 13 # Test different values
# if age >= 18:
#     print("Adult")
# elif age >= 13 and age < 18:
#     print("Teen")
# else:
#     print("Child")

# Andre
age = 25
if age > 18:
    print ("Adult")
elif age >= 13 and age <=18:
    print ("Teenager")
else:
    print ("Child")

# Broderick
# age = int(input("What is your age? "))
# if age >= 18:
#     print("You are an adult!")
# elif age < 18 and age > 12:
#     print("You are a teen!")
# else:
#     print("You are a child!")

# JIN
num_banana = 0
if num_banana >= 5:
    print("I have a bunch of bananas")
elif num_banana > 0 and num_banana < 5:
    print("I have a small bunch of bananas")
else:
    print("I have no bananas")

# Number of Banana with Exception handling from Broderick
try:
    num_bananas = int(input("Enter the number of bananas: "))
    if num_bananas >= 5:
        print("I have a bunch of bananas")
    elif num_bananas > 0:
        print("I have a small bunch of bananas")
    else:
        print("I have no bananas")
except ValueError:
    print("Invalid input. Please enter a valid number.")