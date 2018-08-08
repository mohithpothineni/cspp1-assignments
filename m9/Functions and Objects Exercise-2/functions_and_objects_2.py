'''func and objects 2'''
#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(num_i):
    '''takes and input n and increment it by 1'''
    return num_i + 1

def apply_to_each(list_, func_):
    '''applies func to entire list and returns new list'''
    return list(map(func_, list_))

def main():
    ''' takes input from user and calls apply to each func'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
