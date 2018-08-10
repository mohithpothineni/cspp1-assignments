#Exercise: Assignment-2
'''
Implement the updateHand function. Make sure this function has no side effects:
i.e., it must not mutate the hand passed in.
Before pasting your function definition here,
be sure you've passed the appropriate tests in test_ps4a.py.
'''

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    result_ = {}
    for i in hand:
        if i in word:
            result_[i] = hand[i] - word.count(i)
        else:
            result_[i] = hand[i]
    return result_



def main():
    '''gets input from user and call the func'''
    inp_ = input()
    adict_ = {}
    for i in range(int(inp_)):
        data_ = input()
        ll_ = data_.split()
        adict_[ll_[0]] = int(ll_[1])
        i += 1
    data1_ = input()
    print(updateHand(adict_, data1_))



if __name__ == "__main__":
    main()
