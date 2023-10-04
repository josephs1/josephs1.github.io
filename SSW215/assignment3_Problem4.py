# "I pledge my honor that I have abided by the Stevens Honor System." -Joseph Stefanoni IV
# 10/3/23
# Assignment #3 Problem 4:
import random
pot = int(input("How much cash are you putting into the pot? (Please enter an integer): "))
maxPot = pot
rolls = 0
while pot>0:
    r1 = random.randint(1,6)
    r2 = random.randint(1,6)
    total = r1+r2
    rolls += 1
    if total==7:
        pot+=4
        if pot>maxPot:
            maxPot = pot
    else:
        pot -= 1
print("The number of rolls taken to break the player was: ", rolls, ". The maximum pot amount was: ", maxPot)


