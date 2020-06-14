# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : tgloves
# Collaborators : Just me
# Time spent    : 18 hours over 2 weeks
"""
Wecome to the Word Game. The program is built out below. Ensure the that the word.txt file
is in your current directory. If not, then update your current directory to the location of
the word.txt file. After that, just run the program in an Python IDE and play!

"""

import math
import random
import string
import copy

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
WILDCARD = '*'
HAND_SIZE = 7
letters = VOWELS + CONSONANTS + WILDCARD


#Modified to include a astrisk as a wildcard score == 1
SCRABBLE_LETTER_VALUES = {
    '*': 0,'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        
        freq[x] = freq.get(x,0) + 1

    return freq
	
#print(get_frequency_dict("hello"))
# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    
    #Creates the first score variable
    first_score = 0   
    #Sets all letters in word to lowercase
    word = word.lower()
    #Create new variable as word length
    word_length = len(word)
    #Create second score variable
    second_score = n * word_length - 3*(n-word_length)
    
    #Checks that all characters in the word entered are a lowercase letter, raises TypeError otherwise.
    for x in word:
        if x not in letters:
            raise TypeError ("Sorry, that's not a word. Only enter letters.")
    
    #If no type errors, iterate through the dictionary to calculate the first score based on the score per letter
        else:
            if x in SCRABBLE_LETTER_VALUES:
                first_score += SCRABBLE_LETTER_VALUES[x]
    
    #Evaluate the secord_score. If < 1, set second_score to 1
    if second_score < 1:
        second_score = 1
    
    #Calcuate the word_score as a sum of first_score+second_score     
    word_score = first_score * second_score
    
    #return the calculated score
    return word_score

#print(get_word_score('FORK', 4))

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    print("Current Hand:")
    for letter in hand.keys():
        for j in range(hand[letter]):
             
             
             print(letter, end=' ')      # print all on the same line
      
#print(display_hand(get_frequency_dict("axxllledl")))

def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))
    
    #Adds a wildcard key to hand. This replaces 1 vowel allocation in next statement
    hand["*"] = 1
    
    #interates from 0 to num_vowels - 1, adding vowels to the dict. 
    for i in range(num_vowels-1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    
    #iterates from the num_vowels to the total n, adding consonants to the dict
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    
    return hand

#print(deal_hand(7))

# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
        
    #create a deep copy of the hand called new_hand to mutate in the func
    new_hand = copy.deepcopy(hand)
    
    #Converts all letters in word to lower case letters
    word = word.lower()
        
    #Checks that all characters in the word entered are a lowercase letter, raises TypeError otherwise.
    for x in word:
        if x not in letters:
            raise TypeError ("Sorry, that's not a word. Only enter letters.")
    
    #Subtracts value of 1 for each key in the dictionary for a given letter in the word. Removes keys in the dictionary that are <= 1
    for x in word:   
        new_hand[x] = new_hand.get(x, 0) - 1
        if new_hand[x] <= 0:
            new_hand.pop(x)
    return new_hand
      
#print(update_hand({'a': 1, 'i': 1, 'e': 1, 'b': 1, 'p': 1, 'j': 2}, "pebble"))

# Problem #3: Test word validity
#
def is_valid_word(word, hand, wordlist):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #create a deep copy of the hand called new_hand to mutate in the func
    new_hand = copy.deepcopy(hand)
    
    #Converts all letters in word to lower case letters
    word = word.lower()
        
    #Checks that all characters in the word entered are a lowercase letter, raises TypeError otherwise.
    for x in word:
        if x not in letters:
            raise TypeError ("Sorry, that's not a word. Only enter letters.")
    
    #Create check_counter the adds 1 if the word is in the list
    check_counter = 0
    
    for i in wordlist:
        
        #If word is in the dictionary, set check_counter to 1, break the loop. 1st Criteria for setting
        #function to True has been met.
        if i == word:
            check_counter = 1
            
            #print for debugging
            #print("A",i, word, check_counter)
            break
        elif "*" in word:
            #find the location of the astrisk
            wildcard_words = list()
            #word = "d*ddger"
            for n in VOWELS:
                new_word = word.replace("*", n)
                wildcard_words.append(new_word)
            #print("A.1", wildcard_words)
            for words in wildcard_words:
                for i in wordlist:
                    if words == i:
                        check_counter = 1
                        #print("A.2",check_counter)
            break
           
    if check_counter == 1:

        #print for debugging
        #print("B",check_counter)
        
        for x in word:   
            new_hand[x] = new_hand.get(x, 0) - 1
            #print for debugging
            #print("C",new_hand[x])
        for x in new_hand:
            if new_hand[x] < 0:
                
                check_counter = 2
                #print for debugging
                #print("D",new_hand[x], check_counter)
        if check_counter == 2:
            
            #print for debugging
            print("Sorry, your hand doesn't have the letters to spell the word.")
            return False
        
        #Returns True since word in dictionary and player has requsite letters in hand
        else:
            return True
    
    #Returns false for word not in the dictionary
    else:
        
        return False
  
#print(is_valid_word("lo*k",{'*': 1, 'o': 1, 'e': 1, 'l': 1, 'k': 2, 'j': 2}, word_list))

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    calc_hand = 0
    for x in hand:
        calc_hand += hand[x]      
    return calc_hand

#calculate_handlen({'*': 1, 'a': 1, 'e': 1, 'l': 1, 'p': 2, 'j': 2})

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    total_word_score = 0
    word = ''
    
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
       
        # Display the hand
        display_hand(hand)
         
        # Ask user for word input
        word = input("Enter word, or !! to indicate that you are finished:")
        
         # If the input is two exclamation points:
        if word == '!!':
            
            #End the game (break out of the loop)
            break
            
        #Otherwise (the input is not two exclamation points):
        else:    
            
            #If the word is valid:
            #print("A",word)
            #print("A", hand)
                        
            if is_valid_word(word, hand, word_list) == True:
                
                #Calculate the word score
                get_word_score(word, calculate_handlen(hand))
                
                # and the updated total score
                total_word_score += get_word_score(word, calculate_handlen(hand))
                
                # Tell the user how many points the word earned
                print('"'+ word + '"', "earned", get_word_score(word, calculate_handlen(hand)), "points. Total:", total_word_score)
                print()
                update_hand(hand, word)
                
            # Otherwise (the word is not valid):
            else:
                
                #Reject invalid word
                print("Sorry, the word isn't in the dictionary.")
        #Update the user's hand by removing the letters of their inputted word
        hand = update_hand(hand, word)      

    #Calculates total word score            
    if calculate_handlen(hand) == 0:
        print("Ran out of letters. Total score:", total_word_score, "points")
        return total_word_score  
    else:
        print("Total score:", total_word_score, "points")
        return total_word_score  

#play_hand(deal_hand(7), word_list)

#
# Problem #6: Playing a game
# 

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
        
    #Check if letter is in the hand
    if letter in hand:
    
        #Create a copy of the hand
        new_hand = copy.deepcopy(hand)
                
        #Create a new string of letters but remove those in the hand
        new_letters = ''.join(i for i in letters if not i in hand)
        
        #Select 1 letter at random from new_letters
        x = random.choice(new_letters)
       
        #Add that letter to the hand
        new_hand[x] = hand.get(x, 0) + 1
                
        #Remove letter value from the dictionary
        new_hand[letter] = new_hand.get(letter, 0) - 1
        if new_hand[letter] <= 0:
            new_hand.pop(letter)
        
        #Return new hand    
        return(new_hand)
        
    else:
        return hand
   
#substitute_hand({'*': 1, 'a': 1, 'e': 1, 'l': 1, 'p': 2, 'j': 2}, 'e')    

def ask_total_hands(total_hands):
    """
    Parameters
    ----------
    total_hands : int
        Asks user to enter the total number of hands. Function repeats until an int is given.

    Returns 
    -------
    int
        Provides the number of hand the user will play in the game.
    """
    try:
        #Asks user if he/she wants to substitute a letter yes or no. Lowers case, strips whitespace.
        total_hands = int(input("Enter total number of hands:"))
        return total_hands
    
    
    #Repeats the function if the user enters an interger
    except ValueError:
        print("Sorry, that's not a whole number. Only enter whole numbers.") 
        return ask_total_hands(total_hands)

def ask_for_yes_no(substitute):
    """
    Parameters
    ----------
    substitute : string
        This prompt the users to enter yes or no. If the user doesn't enter yes
        or no, then user is prompted again until the string yes or no is provided

    Returns Boolean True if user enters "yes", False if user enters "no"
    -------
    """   
    try:
        #Asks user if he/she wants to substitute a letter yes or no. Lowers case, strips whitespace.
        substitute = str(input("Would you like to substitute a letter? (yes/no): "))
        substitute = substitute.lower()
        substitute = substitute.strip() 
        
        #Returns True if yes
        if substitute == 'yes':
            return True
        
        #Returns False if yes
        elif substitute == 'no':
            return False
        
        #Repeats the function if string but not yes or no
        else:
            print("Sorry, please only enter 'yes' or 'no'.") 
            return ask_for_yes_no(substitute)
    
    #Repeats the function if the user enters non-string value
    except ValueError:
        print("Sorry, please only enter 'yes' or 'no'.") 
        return ask_for_yes_no(substitute)

def ask_for_replay(replay):
    """    
    Parameters
    ----------
    substitute : string
        This prompt the users to enter yes or no. If the user doesn't enter yes
        or no, then user is prompted again until the string yes or no is provided

    Returns 
    -------
    Boolean True if user enters "yes", False if user enters "no"    
    """    
    try:
        #Asks user if he/she wants to substitute a letter yes or no. Lowers case, strips whitespace.
        replay = str(input("Would you like to replay the hand? (yes/no): "))
        replay = replay.lower()
        replay = replay.strip() 
        
        #Returns True if yes
        if replay == 'yes':
            return True
        
        #Returns False if yes
        elif replay == 'no':
            return False
        
        #Repeats the function if string but not yes or no
        else:
            print("Sorry, please only enter 'yes' or 'no'.") 
            return ask_for_replay(replay)
    
    #Repeats the function if the user enters non-string value
    except ValueError:
        print("Sorry, please only enter 'yes' or 'no'.") 
        return ask_for_replay(replay)

def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    
    print(
    """    
      Welcome to the Word Game!
      In this game you will get dealt a number of letters
      that you will use to spell words. Each letter has
      a different score based on its frequency of use in English.
      You will gain points for the letters you use and letters
      in your hand. You will get a wildcard letter as a * that
      can be substituted for a vowel. You may replay a hand only
      once during the game. If you elect to replay the hand,
      you won't get a new set of letters. Try to use all your
      letters to spell words in each hand. If you choose a word
      and you don't have the letters in your hand, you will
      lose those letters.
      
      Good luck!
    """  
      )
    
    #Asks the user to input a total number of hands
    total_hands = 0   
    total_hands = ask_total_hands(total_hands)    
    final_total_score = 0
    replay_counter = 0
    
    #Continue game through the total number of hands indicated by user
    while total_hands > 0:
        
        #Deal new hand for each new hand
        hand = deal_hand(HAND_SIZE)

        #Display hand
        display_hand(hand)

        #Ask the user if they want to substitute one letter for another. Only allow once at start of hand
        substitute = ""
        if ask_for_yes_no(substitute) == True:
            letter = input("Which letter would you like to replace: ")
            hand = substitute_hand(hand, letter)
        
        first_hand_score = 0
        second_hand_score = 0
        
        #Play hand. Continue hand until user enters !!, or user runs out of letters. Store first_hand_score
        first_hand_score = play_hand(hand, word_list)
        print("FIRST", first_hand_score)
        replay = ""
        
        #Reset replay counter to ensure only 1 replay per hand
        
        #Ask if user wants to replay, takes the highest score and adds to final_total_score
        if replay_counter == 0:
            
            #If the user wants to replay, deal same hand again
            if ask_for_replay(replay) == True:
                second_hand_score = play_hand(hand, word_list)
                print("SECOND", second_hand_score)
                #Compare first_hand_score to replay_hand_score, keep highest. Only 1 replay per game. Update counter.
                if first_hand_score > second_hand_score:
                    final_total_score += first_hand_score
                    print("Total score for this hand:", first_hand_score)
                    replay_counter += 1
                else:
                    final_total_score += second_hand_score
                    replay_counter += 1
                    total_hands = total_hands - 1    
                    print("Total score for this hand:", second_hand_score)
                    print("-----------")
                    
            #User indicates no replay, add first_hand_score to final_total_score, update hands
            else:
                print("Total score for this hand:", first_hand_score)
                final_total_score += first_hand_score
                total_hands -= 1 
                print("-----------")
                
        #User has no replays left, add first score to total and subtract total hands
        else:
            final_total_score += first_hand_score
            total_hands -= 1
            print("-----------")
    
    #Returns the final total score for the game      
    return print("Total score over all hands:", final_total_score)

# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
