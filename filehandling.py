# File handling allows you to interact with files within the operating system
# You can read or write to files
# syntax is open(filepath, mode - read/write)
data = open("GroundRules.txt", 'r') # Reading in the dataset
# print(data.readlines()) # Readlines method outputs the entire file as a list of strings
data.close() # To close the file and ensure that it is not assessible in this code

# Context managers are now used for reading files
# It automatically handles file closing
with open("GroundRules.txt", 'r') as file:
    data = file.readlines()

# With context managers, you no longer need the file.close()

with open("newlycreated.txt", "w+") as file:
    file.write("I am just trying to append to this file again!")
