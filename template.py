# This file will have a template code that I might use a lot in the challenges.and
# Like reading the input file and loop through it...etc

import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)


f = open(os.path.join(dirname,"1.txt"), "r")

lines = f.readlines()



for line in lines:

    # remove the new line character
    line = line.rstrip()

    # do something
    print(line)

f.close()



# to check if the line is empty
if line.strip() == "":
    print("empty line")




def printables(str, type = 1):
    if type == 1:
        print("-=-=-=-=--=-=-=-=-")
    elif type == 2:
        print("\n")
    
    print(str)

    if type == 1:
        print("-=-=-=-=--=-=-=-=-")
    elif type == 2:
        print("\n")





