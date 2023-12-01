# Objectives
# Get the calibration value from teh text file. 
# that is the first number and the last number of each line then sum them up
# tough part is that the numbers are in words
# example: two1nine will be 219 and therefor the calibration value for that line is 29


# Tasks
# 1. read the file
# 2. loop through the lines
# 3. filter the lines that are empty
# 4. loop though the line and get only the numbers
# 5. if the char is not a number then check if it is a word that means a number
# 5. sum the numbers

import os
import glob

dirname = os.path.dirname(__file__)
print (os.getcwd())
print (dirname)
print (os.path.join(os.getcwd(), 'test'))
print (__file__)
fileName = "2.txt"
# fileName = "2_test.txt"




def init():
    printables("Init", 1)

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
            for i, char in enumerate(line):
                if char.isdigit():
                    numbers += char
                else:
                    # check if the word is in the line by looping through the words and check if the line starts with the word
                    for word in word_to_num:
                        if line[i:].startswith(word):
                            numbers += word_to_num[word]
            adding += int(numbers[0] + numbers[-1])
            print(i)


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