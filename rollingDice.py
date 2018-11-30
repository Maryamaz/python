#This project involves writing a program that simulates rolling dice.
# When the program runs, it will randomly choose a number between 1 and 6. 
#(Or whatever other integer you prefer - the number of sides on the die 
#is up to you.) The program will print what that number is. 
#It should then ask you if you'd like to roll again.
from random import randint
import sys
#min = 1
#max = 6
#print 'Number of arguments:', len(sys.argv), 'arguments.'
#print 'Argument List:', str(sys.argv)
#print str(sys.argv
if len(sys.argv)==3: 
    min = int(str(sys.argv[1]))
    max = int(str(sys.argv[2]))
    #print min, max

    if max < min:
        print ("Your second number should be larger than your first number, please try again")
        min = int(str(sys.argv[1]))
        max = int(str(sys.argv[2]))
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
else:

    min = int(raw_input("Please enter a minimum number: "))
    max = int(raw_input("Please enter a maximum number: "))
    while max < min:
        print ("Your max number should be larger than your min number, please try again")
        min = int(raw_input("Please enter a minimum number: "))
        max = int(raw_input("Please enter a maximum number: "))
    #min, max = map(int, userIn1().split())
    #print min, max
    randNum = randint(min, max)
    print randNum
    userIn = raw_input("Would you like to roll again? y/n: ")
    while userIn == 'y':
        randNum = randint(min, max)
        print randNum
        userIn = raw_input("Would you like to roll again? y/n: ")