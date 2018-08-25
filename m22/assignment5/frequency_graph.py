'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
    ''' print the dictionary in the specified format'''
    dict_keys = list(dictionary.keys())
    for key in sorted(dict_keys):
        print("{} - {}".format(key, '#'*dictionary[key]))

def main():
    '''gets input from user and calls graph func '''
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
