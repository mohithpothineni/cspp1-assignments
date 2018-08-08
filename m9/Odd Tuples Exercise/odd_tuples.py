#Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as input and returns a tuple in which contains odd index values in the input tuple  



def odd_tuples(a_tup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    return tuple(a_tup[i]  for i in range(0,len(a_tup),2))
    

def main():
    inp_data = input()
    inp_data = inp_data.split()
    a_tuple=()
    for j in range(len(inp_data)):
        a_tuple += (str(inp_data[j]),)
    print(odd_tuples(a_tuple))

if __name__ == "__main__":
    main()
