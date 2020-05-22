# Problem Set 2, Hangman With Hints.py
# Name: tgloves
# Collaborators: Just me
# Time taken: 8 hours


# Hangman Game
# -----------------------------------
# This is a version of the classic game, Hangman. For more info check out the rules and
# background here: http://en.wikipedia.org/wiki/Hangman_(game)
# First import the words.txt file.
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

def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = list(my_word.replace('_', '0'))
    other_word = list(other_word)
    if len(my_word) != len(other_word):
        return False
    else:
        for i in range(len(my_word)):
            if my_word[i] == other_word[i] and my_word.count(my_word[i]) != other_word.count(other_word[i]):
                return False
    for i in range(len(my_word)):
        if my_word[i] == '0':
            my_word[i] = ''
            other_word[i] = ''
    if my_word == other_word:
        return True
    else:
        return False


def contain(word, wrong_guess):
    count = []
    for i in range(len(word)):
        if word[i] in wrong_guess:
            count.append(1)
        else:
            count.append(0)
    if sum(count) >= 1:
        return True
    else:
        return False


def show_possible_matches(my_word, wrong_guess):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    suggestion = []
    for word in wordlist:
        if match_with_gaps(my_word, word) and not contain(word, wrong_guess):
            suggestion.append(word)
    if not suggestion:
        print('No matches found')
    else:
        for word in suggestion:
            print(word, end=' ')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game Hangman With Hints!")
    print("If you want to get a list of possible solutions, enter *")
    print("I am thinking of a word that is", len(secret_word), "letters long.")
    print("----------------")
    print("You may only enter upper or lowercase letters. You have 3 warnings before you are kicked out of the game.")
  
    letters_guessed = []
    wrong_guess = []
    guesses = 6 #counter for guesses
    warning = 3 #counter for the # of non-numeric warnings
    import string
    
    
    while guesses > 0 and is_word_guessed(secret_word, letters_guessed)== False:
        
        #Start of the while loop if conditions are met. Provide count of guesses and available letters. Prompts input.
        print("You have", guesses, "guesses left.")    
        print("Available letters:", get_available_letters(letters_guessed))
        guess = input("Please make your guess:")
        
        #Calls all words in the wordlist that are the same length and have the same letters as the input so far.
        if guess == '*':
            print('Possible word matches are:')
            show_possible_matches(get_guessed_word(secret_word, letters_guessed), wrong_guess)
            print('\n-------------')
            print(get_guessed_word(secret_word, letters_guessed))
        
        #Checks if the input is alphabetical. Violations subtract from warnings or guesses.
        elif str.isalpha(guess) == False:
            if warning > 0:
                warning = warning - 1
                print("Your guesss is not a letter. You've been warned! You have", warning, "warnings left:",get_guessed_word(secret_word, letters_guessed))
            else:
                guesses = guesses - 1
                print("Your guesss is not a letter. You have no warnings left so you're losing guesses.", get_guessed_word(secret_word, letters_guessed))
        
        #If guess is alphabetical, check if the guess is in the secret word.
        else:
            guess = str.lower(guess)
            
            #If guess has already been guessed, subtract warnings.
            if guess in letters_guessed:
                if warning > 0:
                    warning = warning - 1
                    print("Oops! You've already guessed that letter. You now have", warning,"warnings left.", get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses = guesses - 1
                    print("Oops! You've already guessed that letter. You have no warnings left so you're losing a guess.", get_guessed_word(secret_word, letters_guessed))
            
            #If guess is not in secret word, subtract guesses from the total. -2 for vowels, -1 for consonants.
            elif guess not in secret_word:
                if guess in ["a","e","i","o","u"]:
                    print("Oops! That letter is not in my word. Because you've guessed a vowel you lose 2 guesses:", get_guessed_word(secret_word, letters_guessed))
                    guesses = guesses - 2
                else:
                    print("Oops! That letter is not in my word. Because you've guessed a consonant you lose 1 guess:", get_guessed_word(secret_word, letters_guessed))
                    guesses = guesses - 1
                letters_guessed.append(guess)
                wrong_guess.append(guess)
            
            #If guess is in the secret word, append letter to letters guessed.
            else:
                letters_guessed.append(guess)
                print("Good guess!", get_guessed_word(secret_word, letters_guessed))              
                
    #Checks if while loop is broken because user is out of guesses. Ends game.         
    if guesses <= 0:
        print("You're out of guesses! GAME OVER")
        print("The word was", secret_word + ".")
    
    #While loop is broken because the user enters correct word. Issues congrats and ends game.
    else:
        print('-----------')
        print('Congratulations! You won!')
        print('Your total score for this game is:', guesses*len(secret_word)) 


###############
##Uncomment below and run code to play Hangman With Hints
###############

if __name__ == "__main__":
        
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
