''' square root by approximation method '''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    '''returns square root by approximation method '''
    num_ = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_ = 0.01
    step_ = 0.1
    ans_ = 0.0
    # your code starts here
    while abs(ans_ ** 2 - num_) >= epsilon_:
        ans_ += step_
    if abs(ans_ ** 2 - num_) >= epsilon_:
        pass
    else:
        print(ans_)

if __name__ == "__main__":
    main()
