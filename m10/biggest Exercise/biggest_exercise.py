'''
#Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the key corresponding to the entry with
#the largest number of values associated with it.
If there is more than one such entry, return any one of the matching keys.
'''

def biggest(inp_dict):
    '''
    inp_dict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest_ = 0
    for i in inp_dict.values():
        if len(i) > biggest_:
            biggest_ = len(i)
    result_ = ""
    for i in inp_dict:
        if len(inp_dict[i]) == biggest_:
            if result_ != "":
                result_ += ","+i
            else:
                result_ += i
    return result_

def main():
    '''gets input from user and calls biggest func '''
    inp_ = input()
    inp_dict = {}
    for i in range(int(inp_)):
        inp_s = input()
        inp_l = inp_s.split()
        if inp_l[0][0] not in inp_dict:
            inp_dict[inp_l[0][0]] = [inp_l[1]]
        else:
            inp_dict[inp_l[0][0]].append(inp_l[1])
        i += 1
    print(biggest(inp_dict))


if __name__ == "__main__":
    main()
