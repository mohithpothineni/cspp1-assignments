'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dictionary):
    ''' print the dictionary in the specified format'''
    dict_keys = list(dictionary.keys())
    for key in sorted(dict_keys):
        print("{} - {}".format(key, dictionary[key]))

def main():
    '''gets input form the user '''
    dictionary = eval(input())
    print_dictionary(dictionary)

if __name__ == '__main__':
    main()
