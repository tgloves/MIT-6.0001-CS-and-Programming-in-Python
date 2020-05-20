# Problem Set 2, Hangman Standard.py
# Name: tgloves
# Collaborators: Just me


# Hangman Game
# -----------------------------------
# This is a version of the classic game, Hangman. For more info check out the rules and
# background here: http://en.wikipedia.org/wiki/Hangman_(game)
# First import the words.txt file that in the ps2 folder.
# Run the program with shift + enter
# Try to guess the word before you run out of guesses!


#import words.txt

import random
import string

WORDLIST_FILENAME = "words.txt"



def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    
    return random.choice(wordlist)

# end of helper code

#-----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for n in secret_word:
        if n not in letters_guessed:
            return False
            break
    else:
        return True




def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    x = []
    for n in secret_word:
        if n not in letters_guessed:
            x.append("_")
        else:
            x.append(n)
    return ''.join(x)
# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed) )


import string
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
   
    x = string.ascii_lowercase
    for n in letters_guessed:
        if n in x:
            x = x.replace(n, '')
        else:
            x
    return str(x)

# letters_guessed = []
# print (get_available_letters(letters_guessed))



def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
        
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("----------------")
    print("You may only enter upper or lowercase letters. You have 3 warnings before you are kicked out of the game.")
  
    letters_guessed = []
    guesses = 6 #counter for guesses
    warning = 3 #counter for the # of non-numeric warnings
    import string
    
    
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed)== False:
        #letters_guessed = list()
        
        print("You have", guesses, "guesses left.")    
        print("Available letters:",get_available_letters(letters_guessed))
        guess = input("Please make your guess:")
        
        if str.isalpha(guess) == False:
            if warning > 0:
                warning = warning - 1
                print("Your guesss is not a letter. You've been warned! You have", warning, "warnings left")
            else:
                guesses = guesses - 1
                print("Your guesss is not a letter. You have no warnings left so you're losing guess.")
        else:
            guess = str.lower(guess)
            if guess in letters_guessed:
                
                if warning > 0:
                    warning = warning - 1
                    print("Oops! You've already guessed that letter. You now have", warning,"warnings left.")
                else:
                    guesses = guesses - 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you're losing a guess.")
        
            elif guess not in secret_word:
                if guess in ["a","e","i","o","u"]:
                    print("Oops! That letter is not in my word. Because you've guessed a vowel you lose 2 guesses")
                    guesses = guesses - 2
                else:
                    print("Oops! That letter is not in my word. Because you've guessed a consonant you lose 1 guess")
                    guesses = guesses - 1
                letters_guessed.append(guess)
            else:
                letters_guessed.append(guess)
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))              
                
             
    if guesses == 0:
        print("You're out of guesses! GAME OVER")
    else:
        print('-----------')
        print('Congratulations! You won!')
        print('Your total score for this game is:', guesses*len(secret_word))



if __name__ == "__main__":
        
    secret_word = choose_word(wordlist)
    hangman(secret_word)
    
