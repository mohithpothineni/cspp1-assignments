'''
# Exercise: odd

# Write a Python function, odd, that takes in one number
and returns True when the number is odd and False otherwise.

# You should use the % (mod) operator, not if.

# This function takes in one number and returns a boolean.
'''

def odd(xx_):
    '''
    x: int or float.

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return xx_ % 2 == 1

def main():
    '''takes user input and validates odd or not '''
    data = input()
    print(odd(int(data)))

if __name__ == "__main__":
    main()
