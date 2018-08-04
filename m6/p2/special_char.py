'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_input = input()
    for i in str_input:
        if ord(i) >= 97 and ord(i) <= 122:
            print(i, end="")
        elif ord(i) >= 65 and ord(i) <= 90:
            print(i, end="")
        elif ord(i) >= 48 and ord(i) <= 57:
            print(i, end="")
        else:
            print("", end=" ")

if __name__ == "__main__":
    main()
