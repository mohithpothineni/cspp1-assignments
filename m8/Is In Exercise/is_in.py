'''chcecks for a char in a string'''
# Exercise: Is In
# Write a Python function, isIn(char, aStr),
#that takes in two arguments a character and String and
#returns the isIn(char, aStr) which retuns a boolean value.
# This function takes in two arguments character and String and returns one boolean value.

def is_in(char_c, a_str):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if a_str == '':
        return False
    if len(a_str) == 1:
        return a_str == char_c
    if a_str[len(a_str) // 2] == char_c:
        return True
    if a_str[len(a_str) // 2] > char_c:
        return is_in(char_c, a_str[0:len(a_str)//2])
    return is_in(char_c, a_str[len(a_str)//2:])

def main():
    '''gets input from user and calls isin func'''
    inp_data = input()
    inp_data = inp_data.split()
    print(is_in((inp_data[0][0]), inp_data[1]))


if __name__ == "__main__":
    main()
