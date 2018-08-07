''' gcd using iterative technique'''
# Exercise: GCDIter
# Write a Python function, gcdIter(a, b),
#that takes in two numbers and returns the GCD(a,b) of given a and b.
# This function takes in two numbers and returns one number.

def gcd_iter(inp_a, inp_b):
    '''
    a, b: positive integers
    returns: a positive integer,the greatest common divisor of a & b.
    '''
    # Your code here
    if inp_a == 0 or inp_b == 0:
        return 0
    if inp_a == 1 or inp_b == 1:
        return 1
    c_low = inp_a if inp_a > inp_b else inp_b

    i = 1
    res_gcd = 0
    while i <= c_low:
        if inp_a % i == 0 and inp_b % i == 0:
            res_gcd = i
        i += 1
    return res_gcd



def main():
    ''' gets user input and calls gcd func '''
    data = input()
    data = data.split()
    print(gcd_iter(int(data[0]), int(data[1])))

if __name__ == "__main__":
    main()
