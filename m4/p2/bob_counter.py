''' bob_counter '''
#Assume s is a string of lower case characters.
#Write a program that prints the number of times the string 'bob' occurs in s.
#For example, if s = 'azcbobobegghakl', then your program should print
#Number of times bob occurs is: 2

def main():
    ''' gives the counter of bob '''
    str_ = input()
    # the input string is in s
    count_ = 0
    for i in range(len(str_) - len('bob') + 1):
        if str_[i:i+3] == 'bob':
            count_ += 1
    print(count_)

if __name__ == "__main__":
    main()
