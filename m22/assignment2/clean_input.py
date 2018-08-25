'''
Write a function to clean up a given string by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    """returns the clean string """
    return "".join([i for i in string if ord(i) in range(97, 123) \
                    or ord(i) in range(65, 91) or ord(i) in range(48, 58)])

def main():
    ''' takes input form the user and calls clean func'''
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
