import os
import logging
# when using python for system admin tasks, the libraries used are either os or subprocess


# A function that will ask the user whether they want to install or remove a package
# After the user has confirmed what they want to do 
# It now prompts the user to enter the various packages they want to either install or remove
# When the various packages have been obtained, the packages are either installed or removed


def package_manager():
    # Handles whether the user want to add or remove packages
    reply = input("Would you like to install or remove packages? I: Install R: Remove ").upper()

    # input validation - ensuring the users enter the correct value we want
    while reply != "I" and reply != 'R':
        reply = input("Would you like to install or remove packages? I: Install R: Remove ").upper()

    # Create a variable called IorR based on the above reply
    if reply == 'R': # compares the value of reply with R
        IorR = 'remove' # Assigning the value remove to the variable
    else:
        IorR = 'install'

    # Ask the user to list the various packages they want to either install or remove
    list_of_packages = []
    done = False

    while done is False:
        packages = input("Write the package you want to {} ".format(IorR))
        list_of_packages.append(packages.strip()) # Adds the values to the list

        # Asking the user to add more packages
        more = input("Do you want to add more packages? Y: Yes N: No ").upper()

        # This ensure the loop stops
        if more == 'N':
            done = True
    
    packages = " ".join(list_of_packages)

    if IorR == 'install':
        # os.system('sudo apt-get install {} -y'.format(packages))
        print("Installed the packages {}".format(packages))
    else:
        # os.system('sudo apt-get remove {} -y'.format(packages))
        print("Removed the packages {}".format(packages))


def clean_environment():
    os.system('sudo apt-get autoremove') # remove dependencies for removed apps
    os.system('sudo apt-get autoclean') # clean up obsolete packages

# This will update the existing enviroment
def update_environment():
    os.system('sudo apt-get update')
    os.system('sudo apt-get upgrade')
    os.system('sudo apt-get dist-upgrade')

# Configuring the logging library
logging.basicConfig(format='%(asctime)s - %(message)s', filename='admin.log', level=logging.INFO)

# package_manager()
try:
    clean_environment(90)
except:
    logging.info("clean_environment function failed to execute!")
# update_environment()
 

logging.info('File was run')