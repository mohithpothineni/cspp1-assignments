def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    m1_r_len = len(m1)
    m1_c_len = len(m1[0])

    m2_r_len = len(m2)
    m2_c_len = len(m2[0])
    
    if m1_c_len != m2_r_len:
        print("cant multiply")
        return
    res = []
    
    for i in range(m1_r_len):
        tmp_ = []
        for j in range(m2_c_len):
            tmp_.append(0)
        res.append(tmp_)
        
    
    for i in range(m1_r_len):
        for j in range(m2_c_len):
            tmp_ = 0
            for k in range(m1_c_len):
                tmp_ += m1[i][k]*m2[k][j]
            res[i][j] = tmp_
    return res
    
    
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    m1_r_len = len(m1)
    m1_c_len = len(m1[0])
    
    m2_r_len = len(m2)
    m2_c_len = len(m2[0])
    
    if m1_r_len != m2_r_len or m1_c_len != m2_c_len:
        print("cant be added ")
        return 
    
    res = []
    for i in range(m1_r_len):
        tmp_ = []
        for j in range(m1_c_len):
            tmp_.append(m1[i][j] + m2[i][j])
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
    
    row_,column_ = dim_.split(",")
    
    matr_ = []
    
    for i in range(int(row_)):
        row_inp = input()
        matr_.append([int(e) for e in row_inp.split(" ")])
    
    return matr_ 
   
    

def main():
    # read matrix 1
    m1 = read_matrix()
    # read matrix 2
    m2 = read_matrix()
    # add matrix 1 and matrix 2
    print(add_matrix(m1, m2))
    # multiply matrix 1 and matrix 2
    print(mult_matrix(m1, m2))
    
    
    

if __name__ == '__main__':
    main()
