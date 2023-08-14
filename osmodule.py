import os 

# print(os.listdir()) # listdir enables you to list any directory of your choice

def show_specific_files(directory, extension):
    "This shows specific file types within any directory of choice"
    list_of_files = os.listdir(directory) # Save the list of files to a variable

    for file in list_of_files:
        split_file_name = file.split('.') # Splits by fullstop
        ext = split_file_name[-1] # Saving the file extension to a variable

        # Only display the files that are the same file extension
        if ext == extension:
            print(file)


# show_specific_files('/home/meri', "ipynb") # Gets all jupyter notebook files in the folder
print(os.getlogin())
print(os.uname())
