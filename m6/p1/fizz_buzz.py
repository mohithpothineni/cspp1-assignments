'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num_ = int(input())
    for i in range(1, num_ + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz\nBuzz", end="\n")
        elif i % 3 == 0:
            print("Fizz", end="\n")
        elif i % 5 == 0:
            print("Buzz", end="\n")
        else:
            print(i, end="\n")

if __name__ == "__main__":
    main()
