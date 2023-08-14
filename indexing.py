# Indexing is the positional arrangement of elements in a collection
# Indexing in python is of two types: positive and negative indexing (lists and tuples)
# Positive indexing: start from 0 and from the right (the first element)
# Negative indexing: starts from -1 and from the left (the last element)
# Syntax of indexing: variable_name_of_collection[index_number]
# With indexing, we can output only one item from within a collection 

# Creating a list of students
students = ['broderick', 'evander', 'kerry', 'christopher', 'bonnie', 'precious']

# indexing out the first element using positive indexing
print(students[0])

# Last element
print(students[5])

# More reliable method for indexing the last element is negative indexing
print(students[-1])

# Indexing in a dictionary 
# This is done using the keyname (remember key:value pairs)
# The same syntax of indexing that is done in list and tuples is applied here

cars_price = {"Benz": 90000, "Audi": 65000, "Chevrolet": 74000, "BMW": 54000, "Volvo": 36000}

# Getting the value of the key chevrolet (Method 1)
print(cars_price["Chevrolet"])

# Method 2 for obtaining the value of a key
print(cars_price.get("BMW"))

# The main difference between the get and square bracket method of indexing in dictionaries is
# The get method does not return an error if the key does not exist unlike the square bracket method

print(cars_price.get('bmw')) # This does not return an error because it is using the get method

# This will return an error because there is no key called "bmw"
print(cars_price['bmw'])


# Slicing - Does not work in dictionaries
# It helps to output several elements at a time from within a collection
# Syntax - variable_name[start_index* : stop_index - 1* : step*] * represents optional
# Stop index usually does not show 

# Start and stop index
print(students[1: 3]) # Only want to see index number 1 and 2

# No start index - the slicing should start at the beginning of the collection
print(students[: 4]) # start from beginning and end at index 3

# No stop index
print(students[4: ]) # start from the start_index till the end of the collection

# Start or stop index
print(students[:]) # It outputs the tneire list

# Step - the number of elements to skip
print(students[: :2]) # This takes every 2 elements
