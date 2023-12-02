# Objectives
# Determine the least number of cubes you would need to play the game in.
# find the power of them for that game and sum them up
# example: Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green. would be 4 red, 6 blue, 2 green. that means 4 * 6 * 2 = 48

# Tasks
# 1. read the file
# 2. loop through the lines (games)
# 3. devide the line into turns
# 4. loop though the turns and check for each color if it exceeds the limit
# 5. if it exceeds the limit then break the loop and go to the next game
# 6. if it doesn't exceed the limit then add the game to the list of possible games
# 5. sum the numbers of the possible games

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

    adding = 0
    MaxColorsAdding = 0

    colorLimit = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    f = open(os.path.join(dirname,fileName), "r")

    lines = f.readlines()

    # looping through all lines
    for line in lines:

        numbers = ""

        # remove the new line character
        line = line.rstrip()

        print ("=------------=-")
        print (line)

        # divide the line into 2 strings by locating the :
        turns = line.split(":")
        gameNumber = turns[0].strip()
        #get the number form the game number
        gameNumber = gameNumber.split(" ")
        gameNumber = gameNumber[1].strip()
        turns = turns[1].split(";")

        exceed = False

        MaxColors = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        # loop through the turns
        for turn in turns:
            # remove the spaces from the turn
            turn = turn.strip()

            # divide the turn into strings by locating the,
            colors = turn.split(",")

            # loop through the colors
            for color in colors:
                # remove the spaces from the color
                color = color.strip()

                # divide the color into strings by locating the space
                color = color.split(" ")

                # check if the color is the max color
                if int(color[0].strip()) > MaxColors[color[1].strip()]:
                    MaxColors[color[1].strip()] = int(color[0].strip())


                # check if the color exceeds the limit
                if int(color[0].strip()) > colorLimit[color[1].strip()]:
                    print("Game " + gameNumber + ": " + turn + " exceeds the limit")
                    print(color[1].strip()+": "+color[0].strip()+" > "+str(colorLimit[color[1].strip()]))
                    exceed = True
                    # break
                else:
                    # exceed = False
                    print("Game " + gameNumber + ": " + turn + " is possible")
            # if exceed:
            #     break

            # check if we are in the last turn in the loop
            if turns[-1].strip() == turn and not exceed:
                adding += int(gameNumber)
                print("total " + str(adding))
                    

        # add all the max colors multiplied together

        MaxColorsAdding += MaxColors["red"] * MaxColors["green"] * MaxColors["blue"]
            # print(turn)

        # print('\n')

        # print (line)

        # # to check if the line is empty
        # if line.strip() == "":
        #     print("empty line")
        # else:
        #     # get the calibration value from the line by looping through the line and get the numbers
        #     for char in line:
        #         if char.isdigit():
        #             numbers += char
        #     adding += int(numbers[0] + numbers[-1])


    # print("sum: " + str(adding))
    print("MaxColorsSum: " + str(MaxColorsAdding))
    
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