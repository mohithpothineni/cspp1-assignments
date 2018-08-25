'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

#declaring a dicct globally
DICT_TOK = {}

def tokenize(string):

    ''' returns the tokenized string'''
    clned_string = "".join(i for i in string if i not in ('"', ',', ';', '.'))

    for i in clned_string.split(" "):
        if i not in DICT_TOK:
            DICT_TOK[i] = 1
        else:
            DICT_TOK[i] += 1

def main():
    '''takes input form the user and calls tokenize func '''
    #global DICT_TOK
    inp_n = int(input())
    i_c = 0
    while i_c < inp_n:
        tokenize(input())
        i_c += 1
    print(DICT_TOK)


if __name__ == '__main__':
    main()
