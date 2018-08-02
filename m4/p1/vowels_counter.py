''' vowels_counter '''
#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
#Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
#For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
    ''' gives the count of vowels '''
    str_ = input()
	# the input string is in s
    count_ = 0
    for i in str_:
        if i in ('a', 'e', 'i', 'o', 'u'):
            count_ += 1
    return count_

if __name__ == "__main__":
    main()
