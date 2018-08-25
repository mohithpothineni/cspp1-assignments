'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def main():
    '''takes input from the user '''
    inp_n = int(input())
    i_c = 0
    while i_c < inp_n:
        print(input())
        i_c += 1

if __name__ == '__main__':
    main()
