# region imports
import random
import random as rnd

# endregion

# region functions
def between(gen, low, high, inclusivelow=True, inclusivehigh=True):
    """
    I wrote this function to return a boolean to indicate if num is in a range
    :param num: the number to check
    :param low: the low end of the range
    :param high: the high end of the range
    :param inclusivelow: bool to include the low end
    :param inclusivehigh: bool to include the high end
    :return: bool indicating if between low and high limits
    """
    if inclusivelow:
        return low<= gen <high
    elif inclusivehigh:
        return low< gen <=high
    elif inclusivelow + inclusivehigh:
        return low<= gen  <=high
    else:
        return low< gen <high

"""using bool to set limiting ranges for results"""

pass


def main():
    """
    This function produces an array of numbers from a normally distributed population

    To check if the numbers generated are normally distributed, I can count
    the percentage within 1,2 and 3 standard deviations of the mean and see
    if they match the theoretical values.  I'll create 3 bins into which the
    numbers in my array will fit.  Note:  a number in bin 1 will also be in bins
    2 & 3.  A number in bin3 will not necessarily be in 1 or 2.
    :return: nothing
    """
    N = 1000 # size of array I want
    arr = []  # array for storing the numbers
    mean = 50  # the mean I want
    stdev = 10  # the standard deviation

    bin1=0  # normal dist should contain 68% within +/-1stdev
    bin2=0  # normal dist should contain 95.5% within +/-2stdev
    bin3=0  # normal dist should contain 99.7% within +/-3stdev

    # find edges of the limits for the various bins
    bin1low = mean - stdev
    bin1high = mean + stdev
    """bin1 calls for +/-1stdev"""

    bin2low = mean - (stdev * 2)
    bin2high = mean + (stdev * 2)
    """bin2 calls for +/-2stdev"""

    bin3low = mean - (stdev * 3)
    bin3high = mean + (stdev * 3)
    """bin3 calls for +/-3stdev"""

    for i in range(N):
        gen= rnd.normalvariate(mean, stdev) # this loop generates the numbers
        """rnd used as random imported as rnd"""
        arr.append(gen)
        """generated numbers stored in array"""
        if between(gen, bin1low, bin1high):
         bin1 +=1
        if between(gen, bin2low, bin2high):
         bin2 +=1
        if between(gen, bin3low, bin3high):
         bin3 +=1
    """use boolean with between function to check which bin numbers are in"""

    #print(arr)  # If I want to see the actual array, uncomment this.
    print("{:.1f}% of data within +/-1 StDev of mean.".format(100*bin1 /N))
    print("{:.1f}% of data within +/-2 StDev of mean.".format(100*bin2 /N))
    print("{:.1f}% of data within +/-3 StDev of mean.".format(100*bin3 /N))
# endregion

if __name__ == "__main__":
    main()  # calls the function main
