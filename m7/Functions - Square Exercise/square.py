'''# Exercise: square
# Write a Python function, square, that takes in one number and returns the square of that number.

# This function takes in one number and returns one number.
'''

def square(xx_):
    '''
    x: int or float.
    '''
    # Your code here
    return xx_*xx_

def main():
    '''runs square with user input '''
    data = input()
    data = float(data)
    temp = str(data).split('.')
    if temp[1] == '0':
        print(square(int(float(str(data)))))
    else:
        print(square(data))

if __name__ == "__main__":
    main()
