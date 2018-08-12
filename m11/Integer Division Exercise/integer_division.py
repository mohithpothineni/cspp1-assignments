#Exercise: Integer Division Exercise
#Modify the code for integer_division so that this error does not occur.

def integer_division(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    if a == 0:
        return "division by Zero error"

    count_ = 0

    while x >= a:
        count_ += 1
        x = x - a
    return count_
    

def main():
    result = ""
    number_of_times =int(input())
    for i in range(number_of_times):
        data = input()
        data = data.split()
        result += str(integer_division(int(data[0]), int(data[1]))) + ("\n" if number_of_times != 1 and i != number_of_times-1 else "")
        i += 1
    print(result,end="")

if __name__== "__main__":
    main()
