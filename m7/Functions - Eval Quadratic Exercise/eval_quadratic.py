'''# Exercise: eval quadratic

# Write a Python function, evalQuadratic(a, b, c, x),
that returns the value of the quadratic a . x 2 + b . x + c

# This function takes in four numbers and returns a single number.
'''

def eval_quadratic(aa_, bb_, cc_, xx_):
    '''returns f(a,b,c,x) '''
    return (aa_*(xx_**2)) + (bb_*xx_) + cc_

def main():
    ''' pylint kosam '''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    # print(data)
    for xx_, item_ in enumerate(data):
        temp = str(item_).split('.')
        if temp[1] == '0':
            data[xx_] = int(float(str(data[xx_])))
        else:
            data[xx_] = data[xx_]
    print(eval_quadratic(data[0], data[1], data[2], data[3]))

if __name__ == "__main__":
    main()
