''' square root by newton rapson method '''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''using newton rapson method the square root is produced '''
    num_ = int(input())
    guess_ = num_ / 2.0
	# epsilon and step are initialized
	# don't change these values
    epsilon_ = 0.01
	# your code starts here
    while abs(guess_ * guess_ -num_) >= epsilon_:
        guess_ = guess_ - (((guess_ ** 2) - num_) / (2 * guess_))
    print(guess_)


if __name__ == "__main__":
    main()
