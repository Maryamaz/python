#This project involves writing a program that simulates rolling dice. 
#If we run the program with 2 arguments, it will take the first one as min
#and the second one as max, and will create random numbers between te min and max.
# If we run the program without entering arguments, the program will ask us for
#a min and a max number - The program will print what the random number is. 
#It should then ask you if you would like to roll again.
from random import randint
import sys

def randNumCreator(min, max):
    while max < min:
        print ("Your max number should be larger than your min number, please try again")
        min = int(raw_input("Please enter a minimum number: "))       
        max = int(raw_input("Please enter a maximum number: "))
    randNum = randint(min, max)
    print randNum
    userIn = raw_input("Would you like to roll again? y/n: ")
    while userIn == 'y':
        randNum = randint(min, max)
        print randNum
        userIn = raw_input("Would you like to roll again? y/n: ")

if len(sys.argv)==3: #we have file name and 2 parameters
    min = int(str(sys.argv[1])) #2nd prameter
    max = int(str(sys.argv[2])) #3rd paameter
    if max < min:
        print ("Your second number should be larger than your first number, please try again")
        min = int(str(sys.argv[1]))  #2nd prameter
        max = int(str(sys.argv[2]))  #3rd paameter
    else:
        randNum = randint(min, max)
        print randNum
        userIn = raw_input("Would you like to roll again? y/n: ")
        while userIn == 'y':
            randNum = randint(min, max)
            print randNum
            userIn = raw_input("Would you like to roll again? y/n: ")
elif len(sys.argv)==2:
    min = int(str(sys.argv[1]))
    max = int(raw_input("Eenter a max number: "))
    randNumCreator(min, max)

else:
    min = int(raw_input("Please enter a minimum number: "))
    max = int(raw_input("Please enter a maximum number: "))
    randNumCreator(min, max)
    #min, max = map(int, userIn1().split())
    #print min, max