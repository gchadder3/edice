"""
edice.py -- Simple Python script to simulate electronic gaming dice.
"""

import random

class Dice(object):
    def __init__(self, numDice=1, diceSides=6):
        self.numDice = numDice
        self.diceSides = diceSides
        
    def show(self):
        print('%dd%d' % (self.numDice, self.diceSides), end='')
        
    def roll(self):
        theRoll = 0
        for ii in range(self.numDice):
            theRoll += random.randint(1, self.diceSides)
        return theRoll
        
if __name__ == '__main__':
    print('E-Dice:')
    print('Starting with a normal die...')
    theDice = Dice(1, 6)
    while (True):
        theDice.show()
        print(' -- ', end='')
        print(theDice.roll())
        inStr = input('Enter a command (q=quit, n=new dice, all other=roll again): ')
        if inStr == 'q':
            break
        elif inStr == 'n':
            numDice = int(input('How many dice to throw?: '))
            numSides = int(input('How many sides on each die?: '))
            theDice = Dice(numDice, numSides)
    