''' tic tac toe validation'''



def is_valid_gameplay(pattern):
    ''' checks whetther the gameplay is valid or not'''
    x_count = 0
    o_count = 0
    for i in pattern:
        for j in i:
            if j == 'x':
                x_count += 1
            elif j == 'o':
                o_count += 1
    if abs(x_count - o_count) == 1 or x_count == o_count:
        return True
    return False

def is_winner(pattern, symbol):
    ''' returns true if the symbol is winner'''
    for i in pattern:
        if "".join(i) == symbol * 3:
            return True
    for i in range(3):
        tmp_ = ''
        for j in range(3):
            tmp_ += pattern[j][i]
        if tmp_ == symbol*3:
            return True
    if "".join([pattern[0][0], pattern[1][1], pattern[2][2]]) == symbol*3:
        return True
    if "".join([pattern[2][0], pattern[1][1], pattern[0][2]]) == symbol*3:
        return True
    return False




def validate_game(pattern):
    ''' prints the game result'''
    if not is_valid_gameplay(pattern):
        return "invalid game"
    if is_winner(pattern, 'x') and is_winner(pattern, 'o'):
        return "invalid game"
    if is_winner(pattern, 'x'):
        return 'x'
    if is_winner(pattern, 'o'):
        return 'o'
    return "draw"



def main():
    '''takes user from input and calls the validaate game func'''
    pattern_ = [input().split(" ") for i in range(3)]
    if all([True if j in ('x', 'o', '.') else False for i in pattern_ for j in i]):
        print(validate_game(pattern_))
    else:
        print("invalid input")

if __name__ == "__main__":
    main()
