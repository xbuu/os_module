# Variables // Modules ]

import os
import time

# Functions // Def ]

def doesfilexist(filePathAndName):
    return os.path.exists(filePathAndName)

# Create Directory ]

if doesfilexist("brew-config"):
    pass
    rmdir("brew-config")
    print("attempting to remove configuration")
    time.sleep(2.5)
    print("removed, reinstalling.")
    os.mkdir("brew")
    os.chdir("brew")
    os.makedirs('brew-config')
    fh = open("readme.txt", "w")
    fh.write("""
    # This program was made only
    # to try out the os module,
    # nothing else

    # h
    """)
    fh.close()
else:
    os.mkdir("brew")
    os.chdir("brew")
    os.makedirs('brew-config')
    fh = open("readme.txt", "w")
    fh.write("""
    # This program was made only
    # to try out the os module,
    # nothing else

    # h
    """)
    fh.close()

print(os.listdir())

# Destroy Directory ]

print("y/n")
deletebootstrapper = input("Do you want to delete the bootsrapper? \n")
if deletebootstrapper.lower() == "y":
    rmdir("brew_bootstrapper")
else:
    print("ending process.")
