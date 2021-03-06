# Name: Yi Jie TAN
# Section: 
# 6.189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *		# import all the functions from string library
from hangman_lib import *

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap' 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    for letter in secret_word:
    	if letter in letters_guessed:
    		return True;
    	else:
    		return False;
    pass # This tells your code to skip this function; delete it when you
         # start working on this function


def print_guessed():
    '''
    Prints out the characters you have guessed in the secret word so far
    '''
    global secret_word
    global letters_guessed
    
    result = ''
    
    if (letters_guessed == []):
    	print "-" * len(secret_word)
    
    for letter in secret_word:
    	if letter in letters_guessed:
    		result += letter;
    	else:
    		result += '-'
    
    return result;
    pass # This tells your code to skip this function; delete it when you
         # start working on this function

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
	
	# print hangman image
	print_hangman_image(mistakes_made);

    while (mistakes_made < MAX_GUESSES):
    	print "%d guess(es) left" %(MAX_GUESSES - mistakes_made)
    	letter = raw_input("Please enter a letter: ").lower()
    	
        if (letter in letters_guessed):
            print "You have chosen this letter already."
            mistakes_made += 1
            print_hangman_image(mistakes_made)

    	else:
    		letters_guessed.append(letter)
    		print print_guessed()

    		if (letter not in secret_word):
    			mistakes_made += 1
                print_hangman_image(mistakes_made)


    	if(mistakes_made == MAX_GUESSES):
    		print "You lose!"
        elif (word_guessed()):
            print 'You won!'
            break
	
	
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()


play_hangman()

    
