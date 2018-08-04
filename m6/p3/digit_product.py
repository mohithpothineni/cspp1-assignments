'''
Given a  number int_input, find the product of all the digits
example:
	input: 123
	output: 6
'''
def main():
    '''
    Read any number from the input, store it in variable int_input.
    '''
    int_input = int(input())
    prod_ = 1
    num_ = abs(int_input)

    while  num_ > 0:
        prod_ *= num_ % 10
        num_ //= 10
    if int_input < 0:
        print(-1 * prod_)
    elif int_input == 0:
        print(int_input)
    else:
        print(prod_)


if __name__ == "__main__":
    main()
