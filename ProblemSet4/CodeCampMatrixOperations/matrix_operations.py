''' matrix operations'''
def mult_matrix(m1_, m2_):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if m1_ is None or m2_ is None:
        return None
    m1__r_len = len(m1_)
    m1__c_len = len(m1_[0])

    m2__r_len = len(m2_)
    m2__c_len = len(m2_[0])

    if m1__c_len != m2__r_len:
        print("Error: Matrix shapes invalid for multNone")
        return None
    res = []

    for i in range(m1__r_len):
        tmp_ = []
        for j in range(m2__c_len):
            tmp_.append(0)
        res.append(tmp_)


    for i in range(m1__r_len):
        for j in range(m2__c_len):
            tmp_ = 0
            for k in range(m1__c_len):
                tmp_ += m1_[i][k]*m2_[k][j]
            res[i][j] = tmp_
    return res


def add_matrix(m1_, m2_):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if m1_ is None or m2_ is None:
        return None
    m1__r_len = len(m1_)
    m1__c_len = len(m1_[0])

    m2__r_len = len(m2_)
    m2__c_len = len(m2_[0])

    if m1__r_len != m2__r_len or m1__c_len != m2__c_len:
        print("Error: Matrix shapes invalid for additionNone")
        return None

    res = []
    for i in range(m1__r_len):
        tmp_ = []
        for j in range(m1__c_len):
            tmp_.append(m1_[i][j] + m2_[i][j])
        res.append(tmp_)
    return res





def read_matrix():
    '''
        read the matrix dimensions from input
x`        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    dim_ = input()

    row_, column_ = dim_.split(",")

    matr_ = []

    for i in range(int(row_)):
        row_inp = input()
        k = [int(e) for e in row_inp.split(" ")]
        if len(k) != int(column_):
            print("Error: Invalid input for the matrix")
            return None
        matr_.append(k)
        i += 1
    return matr_



def main():
    '''takes user input and calls the appropriate funcs '''
    # read matrix 1
    m1_ = read_matrix()
    # read matrix 2
    m2_ = read_matrix()
    # add matrix 1 and matrix 2
    k = add_matrix(m1_, m2_)
    if k is not None:
        print(k)
    # multiply matrix 1 and matrix 2
    k = mult_matrix(m1_, m2_)
    if k is not None:
        print(k)




if __name__ == '__main__':
    main()
