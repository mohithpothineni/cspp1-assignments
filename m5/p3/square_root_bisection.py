''' square root by bisection method '''
# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
    ''' returns square root of a number by bisection method '''
    num_ = int(input())
    # epsilon and step are initialized
    # don't change these values
    epsilon_ = 0.01
    low_ = 0
    high_ = num_
    ans_ = (high_ + low_) / 2.0

    while abs(ans_ ** 2 - num_) >= epsilon_:
        if ans_ ** 2 < num_:
            low_ = ans_
        else:
            high_ = ans_
        ans_ = (high_ + low_) / 2.0
    print(ans_)

if __name__ == "__main__":
    main()
