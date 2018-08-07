'''factorial using recursion '''
# Exercise: Assignment-1
# Write a Python function, factorial(n),
#that takes in one number and returns the factorial of given number.
# This function takes in one number and returns one number.


def factorial(inp_n):
    '''
    n is positive Integer

    returns: a positive integer, the factorial of n.
    '''
    # Your code here
    if inp_n in (0, 1):
        return 1
    return inp_n * factorial(inp_n-1)


def main():
    '''gets user input and calls the factorial func '''
    inp_a = input()
    print(factorial(int(inp_a)))

if __name__ == "__main__":
    main()
