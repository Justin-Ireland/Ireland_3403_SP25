# region imports

from Die import rollFairDie

from Die import rollUnFairDie

# endregion

# region functions
def rollDice(N=3):

    """
    This function simulates rolling N dice simultaneously by using a loop that rolls
    a single die N times and totaling the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    total=0
    for i in range(N):
        i = rollFairDie()
        total += i
    return total



    pass

def rollUnFairDice(N=5, total=0):
    """
    This function simulates rolling N, UnFair dice simultaneously by using a loop that rolls
    a single die N times and totals the score.
    :param N: the number of dice to be rolled
    :return: the total score from rolling N dice
    """
    for i in range(N):
        i = rollUnFairDie()
        total += i

    return total

    pass

if __name__ == "__main__":
    print("Total score of 3 rolls",rollDice(3))
    print("")
    print("Total Score of 5 rolls",rollUnFairDice(5))


# endregion