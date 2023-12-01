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
import re

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)
fileName = "2.txt"
# fileName = "2_test.txt"



# The main function that we will perfomr the tasks in
def init():
    printables("Init", 1)

    adding = 0

    f = open(os.path.join(dirname,fileName), "r")

    lines = f.readlines()

    # looping through all lines
    for line in lines:

        # remove the new line character
        line = line.rstrip()

        # replace the words with numbers
        line = wordsToNumbers(line)

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

# this function will get the calibration value from the line
# @param line: the line that will be filtered
# @return: the calibration value
def getCalibrationValue(line):
    # filter the line to get only the numbers
    line = line.translate(str.maketrans('', '', 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'))

    # count the characters in the line
    print(line)
    writeToFile(line)

    # get the first and last number add them beside each other
    calibration = line[0] + line[-1]

    print(calibration + "\n")
    writeToFile(calibration)
    writeToFile("\n")

    # convert the string to int
    calibration = int(calibration)
    return calibration


# this function will print the string with a line above and below it
# @param str: the string that will be printed
# @param type: the type of the line that will be printed
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



# this function will replace the words with numbers
# @param str: the string that will be filtered
# @return: the string with numbers instead of words
def wordsToNumbers(str): 

    # dictionary of words and numbers
    word_to_num = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        # "zero": "0"
        }

    # loop through the dictionary and replace the words with numbers
    my_string = str
    
    print (my_string)
    writeToFile(my_string)

    # Create a regular expression pattern that matches any of the words
    pattern = re.compile('|'.join(word_to_num.keys()))

    # Use the sub() function to replace each match with the corresponding number
    result = pattern.sub(lambda m: word_to_num[m.group()], my_string)

    print (result)
    writeToFile(result)

    return result


# write a line in a file
def writeToFile(str):
    logFileName = "2_log.txt"

    # create the file if it doesn't exist
    # add the str as a new line in the file

    s = open(os.path.join(dirname,logFileName), "a")
    s.write(str + "\n")
    s.close()

    
init()