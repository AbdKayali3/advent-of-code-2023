# Objectives
# Get the calibration value from teh text file. 
# that is the first number and the last number of each line then sum them up
# example: 1abc2 and pqr3stu8vwx are lines.. we get from them 12 and 38 then sum them up to get 50

# Tasks
# 1. read the file
# 2. loop through the lines
# 3. filter the lines that are empty
# 4. filter each line to get only the numbers
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

        # remove the new line character
        line = line.rstrip()

        # to check if the line is empty
        if line.strip() == "":
            print("empty line")
        else:
            # get the calibration value from the line
            value = getCalibrationValue(line)
            adding = adding + value

    print("sum: " + str(adding))
    
    f.close()

    printables("End", 1)


def getCalibrationValue(line):
    # filter the line to get only the numbers
    line = line.translate(str.maketrans('', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))

    # count the characters in the line
    print(line)

    # get the first and last number add them beside each other
    calibration = line[0] + line[-1]

    print(calibration + "\n")

    # convert the string to int
    calibration = int(calibration)
    return calibration


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