"""
edice.py -- Simple Python script to simulate electronic gaming dice.

Last updated: 9/7/21 (gchadder3)
"""

import random

class Dice(object):
    def __init__(self, numDice=1, diceSides=6):
        self.numDice = numDice
        self.diceSides = diceSides
        self.theDice = [None for ii in range(self.numDice)]  # unrolled dice
        
    def show(self):
        print('%dd%d -- ' % (self.numDice, self.diceSides), end='')
        if self.theDice[0] is None:
            print('unrolled')
        else:
            for ii in range(self.numDice):
                print(self.theDice[ii], end='')
                if ii < (self.numDice - 1):
                    print(' + ', end='')
            if self.numDice == 1:
                print('')
            else:
                print(' == %d' % sum(self.theDice))
        
    def roll(self):
        theRoll = 0
        for ii in range(self.numDice):
            self.theDice[ii] = random.randint(1, self.diceSides)
            theRoll += self.theDice[ii]
        return theRoll
        
if __name__ == '__main__':
    print('E-Dice:')
    print('Starting with a normal die...')
    
    # Create a normal 1d6 die.
    theDice = Dice(1, 6)

    # Loop until we break out of the loop...
    while (True):
        # Roll the dice and show them.
        theDice.roll()
        theDice.show()
        
        # Query for a command.  By default you can just hit Enter to role the same dice
        # again.
        inStr = input('Enter a command (q=quit, n=new dice, all other=roll again): ')
        if inStr == 'q':  # quit
            break
        elif inStr == 'n':  # query for new dice settings so user can switch
            numDice = int(input('How many dice to throw?: '))
            numSides = int(input('How many sides on each die?: '))
            theDice = Dice(numDice, numSides)
    