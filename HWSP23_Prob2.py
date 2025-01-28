#region imports
import Dice



#endregion

#region functions
def main1():  # main function to roll nDice fair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: Chance of rolling each possible score of 3 dice rolled simultaneously
    """
    nDice = 3  # number of dice
    nMinScore = 3  # total score if each die scores 1
    nMaxScore = 18  # total score if each die scores 6
    nNumScores = 16  # number of possible scores
    """used (nMaxScore-nMinScore+1) to get (18 -3 +1 =16)"""
    nTally = [0, 0, 0, 0 ,0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000 # how many times to roll the dice

    for i in range(nRolls):  # each loop rolls dice and increments a score
        rollScore = Dice.rollDice(nDice) # call with N=nDice
        nTally [rollScore - nMinScore] +=1
        # increment score-nMinScore item b/c 0 indexing start
    print("After {} rolls of {} dice...".format(nRolls, nDice))
    for i in range(nNumScores):# print the fraction of rolls for each score
        NumScore = (i + nMinScore)
        Chance = nTally[i] / nRolls
        print("Score {}: Chance {}" .format(NumScore, Chance ))

def main2():  # main function to roll nDice unfair dice nRolls times and output probabilities
    """
    This function rolls nDice nRolls times and calculates the probabilities for
    each possible score based on P(7)=nTally/nRolls, where nTally is number times I roll a 7, for example.
    :return: Chance of each score of rolling 5 unfair dice 1000 times
    """
    nDice = 5   # number of dice
    nMinScore = 5   # total score if each die scores 1
    nMaxScore = 30  # total score if each die scores 6
    nNumScores = 26  # number of possible scores
    nTally = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  # create a list with (nMaxScore-nMinScore+1) elements/items
    nRolls = 1000  # how many times to roll the dice
    for i in range(nRolls):  # each loop rolls dice and increments a score
        roll_score = Dice.rollUnFairDice(nDice)  # call with N=nDice
        nTally[roll_score - nMinScore] +=1
        # increment score-nMinScore item b/c 0 indexing start
    print("After {} rolls of {} dice...".format(nRolls, nDice))
    for i in range(nNumScores):  # print the fraction of rolls for each score
        NumScore = (i + nMinScore)
        Chance = nTally[i] / nRolls
        print("Score {}: Chance {}".format(NumScore, Chance))
#endregion

#this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main1()
    print("")
    main2()