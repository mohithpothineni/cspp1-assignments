''' func and objects 3'''
#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]

def square(num_):
    ''' returns square of a given number'''
    return num_ * num_


def apply_to_each(list_, func_):
    '''applies func to each element in list and returns a new list'''
    return list(map(func_, list_))

def main():
    ''' gets user from the input and calls apply to each func'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
