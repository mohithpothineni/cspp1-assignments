''' checks whether a given number is perfect cube or not'''
# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def main():
    ''' checks a no is perf cube or not by guess and check '''
    # input is captured in s
    num_ = int(input())
    # watch out for the data type of value stored in s
    # your code starts here
    ans_ = 0
    while ans_ ** 3 < num_:
        ans_ += 1
    if ans_ ** 3 == num_:
        print(num_, "is a perfect cube", sep=" ")
    else:
        print(num_, "is not a perfect cube", sep=" ")

if __name__ == "__main__":
    main()
