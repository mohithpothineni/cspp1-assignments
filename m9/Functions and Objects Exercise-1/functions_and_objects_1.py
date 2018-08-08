'''func and object 1'''
#Exercise : Function and Objects Exercise-1
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 4, 8, 9]

def apply_to_each(list_inp, func_inp):
    ''' applies func to each element in list and returns new list'''
    return list(map(func_inp, list_inp))

def main():
    ''' gets input from user and calls the func apply func to all'''
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
