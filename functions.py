# Functions are a named sequence of statments that perform a computation!
# Creating a computation to check a person's eligibility to vote
age = 15

if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")


age = 20
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

age = 40
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")

# Without functions, the computation that checks a person's eligibility will be repeated several times
# Thus going agains the Dont Repeat Yourself (DRY) principle
# The essence of functions is repeatability 
# Syntax for creating a function is
# def function_name(arguments[optional]):
#   computation to be performed - This is the most important part
#   return [optional] - Specifies the value that a function should return

def voter_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote!")

# Makes the code very repeatable
voter_eligibility(60)
voter_eligibility(12)
voter_eligibility(6)

# Calling a function (making a function that have been created to work)
# function_name(argument[optional]) 

# Create a function that checks the level a person is in, based on the years of experience
# Less than 2 - Entry level, 2 - 5 : midlevel, 5 - 8: senior level & Above 8  management level

def experience_cadre(years_of_experience):
    if years_of_experience < 2:
        verdict = "You are still entry level"
    elif years_of_experience >= 2 and years_of_experience < 5:
        verdict = "Mid Level Executive"
    elif years_of_experience >= 5 and years_of_experience <= 8:
        verdict = "Senior Level Executive"
    else:
        verdict = "Management Level"
    # Whatever of the value of verdict is, it will be returned
    return verdict

ten = experience_cadre(10)
three = experience_cadre(3)
one = experience_cadre(1)

print(ten, three, one)
