# Objectives
# Get the calibration value from teh text file. 
# that is the first number and the last number of each line then sum them up
# example: 1abc2 and pqr3stu8vwx are lines.. we get from them 12 and 38 then sum them up to get 50

# Tasks
# 1. read the file
# 2. loop through the lines
# 3. filter the lines that are empty
# 4. loop though the line and get only the numbers
# 5. sum the numbers

import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)
fileName = "1.txt"
# fileName = "1_test.txt"




def init():
    printables("Init", 1)

    adding = 0

    f = open(os.path.join(dirname,fileName), "r")

    lines = f.readlines()

    # looping through all lines
    for line in lines:

        numbers = ""

        # remove the new line character
        line = line.rstrip()

        # to check if the line is empty
        if line.strip() == "":
            print("empty line")
        else:
            # get the calibration value from the line by looping through the line and get the numbers
            for char in line:
                if char.isdigit():
                    numbers += char
            adding += int(numbers[0] + numbers[-1])


    print("sum: " + str(adding))
    
    f.close()

    printables("End", 1)


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

init()