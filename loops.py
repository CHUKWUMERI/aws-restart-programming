# Loops are a way to tell python interpreter to run a block of code repeatedly
# Python has for and while loops

# While loop is a conditional loop. It runs a code as long as a condition is True
# while condition:
#   computation 
# [loop control statements]

# Throwing a birthday party for a person till they are 18
age = 0 # This is when the person was born

while age <= 18:
    print("Happy Birthday!, you are", age, "years old")
    age += 1 # Add a value to age for every cycle of the loop 
    # age = age + 1 is the same as the code above 
    # age =+ 1


# Countdown timer
counter = 10

while counter >= 0:
    # We want to print take off when the value is 0
    if counter == 0:
        print("Take off!")
    else:
        print(counter)
    counter = counter - 1 # Subtracting one everytime from the counter variable


# For Loops
# This kind of loop iterates through a collection and stops as soon as the collection is finished
# The syntax
# for iterable_variable in collection:
# computation to be performed on each item

# Salaries - task is to calculate the bonus for each of the salaires (15%)
salaries = [100000, 40000, 36000, 48000, 55000, 67000, 62000]

for salary in salaries:
    print("Your bonus for your salary of", salary, "is",  0.15 * salary)


# Getting the number of years employees have until they retire - 65 (age of retirement)
employee_age = [25, 18, 40, 35, 60, 55, 27]

for emp in employee_age:
    print(65 - emp, 'years until retirement')
