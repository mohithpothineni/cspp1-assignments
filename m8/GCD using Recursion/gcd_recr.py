'''gcd using recurion '''
# Exercise: GCDRecr
# Write a Python function, gcdRecur(a, b),
#that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcd_recur(inp_a, inp_b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if inp_a == 0 or inp_b == 0:
        return 0
    if inp_a == 1 or inp_b == 1:
        return 1
    if inp_a == inp_b:
        return inp_a
    if inp_a > inp_b:
        return gcd_recur(inp_b, inp_a - inp_b)
    return gcd_recur(inp_a, inp_b - inp_a)


def main():
    '''gets input from user and calls the gcd func '''
    data = input()
    data = data.split()
    print(gcd_recur(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
