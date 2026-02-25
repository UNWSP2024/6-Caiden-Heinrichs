#Week 6, Program 1 - Random Dice
#Caiden Heinrichs
#02/27/26

import random

def randDice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def main():
    #Counter for adding rolls
    rollTotal = 0.0

    for i in range(100):
        #Roll dice and display roll
        currentRoll = randDice()
        print(currentRoll)
        #Add result to total counter
        rollTotal += currentRoll

    #Calculate and display average result of rolls
    average = round(rollTotal / 100, 2)
    print(f'Average of rolls: {average}')


if __name__ == '__main__':
    main()
