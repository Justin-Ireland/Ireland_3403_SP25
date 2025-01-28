

from itertools import count


from Die import rollFairDie as rfd, rollUnFairDie as rufd


# endregion

# region function declarations
def main():
    """
    This function rolls a fair die 1000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: probability of side of fair die rolled
    """
    scores = [0, 0, 0, 0, 0, 0,]  # create a list with 6 elements/items initialized to 0's
    n = 1000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[score -1] += 1  # increment score-1 item b/c 0 indexing start
        """[score -1] indexed back to zero"""
    print ("Probabilities (fair) for 1000 rolls:")

    for i,count in enumerate(scores):
        """Using enumerate builtin b/c I can display the counts as individual indexes"""
        RollChance= count / n
        percent = (RollChance * 100)
        print(f" Side {i+1}: {RollChance:.3f}")
        print (f" percentage of side {i+1}: {percent:.2f}%")
    """Prints both the decimal amount and percentage of the amount
    the sides were rolled"""
    pass



def main2():
    """
    This function rolls a fair die 10000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    """function uses two for loops to call rfd 10,000 times and counting the scores input into the scores list. Then 
    calculates the probability of each side being rolled in decimal and percentage"""
    scores = [0, 0, 0, 0, 0, 0, ]  # create a list with 6 elements/items initialized to 0's
    """6 zeros in list"""
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rfd()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start
        """[score -1] indexed back to zero"""
    # print the result
    print("")
    print("Probabilities (fair) for 10000 rolls:")

    for i, count in enumerate(scores):
        RollChance = count / n
        percent = (RollChance * 100)
        print(f" Side {i + 1}: {RollChance:.3f}")
        print(f" percentage of side {i + 1}: {percent:.2f}%")

    pass


def main3():
    """
    This function rolls an unfair die 10000 times and tallies the number of 1's, 2's etc.  Finally,
    it calculates and outputs the probability of each possible score.
    :return: nothing
    """
    scores = [0, 0, 0, 0, 0, 0, ]  # create a list with 6 elements/items initialized to 0's
    n = 10000  # how many times to roll the die
    for i in range(n):  # each time through the loop, roll die and increment a score
        score = rufd()  # score = 1 to 6
        scores[score - 1] += 1  # increment score-1 item b/c 0 indexing start

    print("Probabilities (unfair) for 10000 rolls:")

    for i, count in enumerate(scores):

        RollChance = count / n
        percent = (RollChance * 100)
        print(f" Side {i + 1}: {RollChance:.3f}")
        print(f" percentage of side {i + 1}: {percent:.2f}%")
    pass


# endregion

# this if statement prevents these calls if this file is imported as a module.
if __name__ == "__main__":
    main()
    print("")
    main2()
    print("")
    main3()