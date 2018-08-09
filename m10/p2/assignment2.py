'''
Exercise : Assignment-2
implement the function hangman, which takes one parameter - the secretWord 
the user is to guess. This starts up an interactive game of Hangman between 
the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, 
that you've defined in the previous part.
'''

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
from get_available_letters import get_available_letters
from  get_guessed_word import get_guessed_word

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    print("----------------------------------")
    #print("answer is",secretWord)
    guess_count = 12
    user_guess = {}
    while True:
        grammer_ = "gussess" if guess_count>1 else "guess"
        print("you have",guess_count,grammer_,"left")
        print("Available letters:",get_available_letters(user_guess))
        new_guess = input("Please guess a letter: ")
        new_guess = new_guess.lower()[0:1]
        if ord(new_guess) in range(97,123) and new_guess not in user_guess:
            guess_count -= 1
            if new_guess in secretWord:
                user_guess[new_guess]=1
                print("Good guess:",get_guessed_word(secretWord,[i for i in user_guess]))
            else:
                print("Oops! That letter is not in my word:",get_guessed_word(secretWord,[i for i in user_guess]))
        else:
            print("Oops! You've already guessed that letter:",get_guessed_word(secretWord,[i for i in user_guess]))
        print("--------------------------------------")
        if get_guessed_word(secretWord,[i for i in user_guess]) == secretWord:
            print("Congratulations, you won!")
            break
        if guess_count == 0:
            print("Sorry, you ran out of guesses. The word was",secretWord)
            break






def main():
    '''
    Main function for the given program
    
    When you've completed your hangman function, uncomment these two lines
    and run this file to test! (hint: you might want to pick your own
    secretWord while you're testing)
    '''
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)


if __name__ == "__main__":
    main()
