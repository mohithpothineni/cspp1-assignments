""" guess the number """

GAME_OVER_FLAG = 0

print("Please think of a number between 0 and 100!")

HIGH_ = 100
LOW_ = 0
NUM_ = 0

while GAME_OVER_FLAG != 1:

    NUM_ = (LOW_ + HIGH_) // 2



    INPUT_FLAG = 0
    while INPUT_FLAG != 1:
        print("Is your secret number", NUM_, "?", sep=" ")
        INP_ = input("Enter 'h' to indicate the guess is too high.\n\
Enter 'l' to indicate the guess is too low.\n\
Enter 'c' to indicate I guessed correctly.\n ")

        if INP_ == 'h':
            HIGH_ = NUM_
            INPUT_FLAG = 1
        elif INP_ == 'l':
            LOW_ = NUM_
            INPUT_FLAG = 1
        elif INP_ == 'c':
            INPUT_FLAG = 1
            GAME_OVER_FLAG = 1
        else:
            print("sorry, I did not understand your input.")


print("Game over. Your secret number was: ", NUM_)
