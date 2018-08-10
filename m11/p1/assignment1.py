'''
Exercise: Assignment-1
'''
from PSET4 import ps4a

def get_word_score(word, inp_n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LE  TTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    score_ = 0
    for i in word:
        score_ += ps4a.SCRABBLE_LETTER_VALUES[i]
    score_ *= len(word)
    if inp_n == len(word):
        score_ += 50
    return score_



def main():
    '''
    Main function for the given problem
    '''
    data = input()
    data = data.split()
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
