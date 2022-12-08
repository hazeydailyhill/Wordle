import os
from random import randrange
from random import choice as random_choice
import sys

#Haley Hill
#May 3, 2022

# Path to the directory where your Python module and words.txt files
# are located. This makes loading the words.txt file work
os.chdir(os.getcwd())

#Define name of file containing the dictionary of words
WORDLIST_FILENAME = "5letterwords.txt"
secret_word = ''
MAX_GUESSES = 6


#load_words: void -> list
#expects nothing and returns a list of words read from WORDLIST_FILENAME
def load_words():
    # inFile is a file handle, like you see in C++
    with open(WORDLIST_FILENAME, 'rt') as reader:
        wordList = [i for i in reader]
    return wordList

list_of_words = load_words()

#get_word: void -> str
#expects nothing and returns a randomly selected word from list_of()_words
def get_word():
    chosen_word = random_choice(list_of_words)
    return chosen_word

secret_word = get_word()

#-------------------------------------------------------------------------------
# _ _ _ _ _
# 0 1 2 3 4

#word_to_dict: string -> void
# expects a 5-letter string and adds them to index_letter_dict
# dictionary as {index:letter} pairs
#   -ex: 'beach' -> { 0: 'b', 1:'e', 2: 'a', 3: 'c', 4: 'h'}
#returns THE NEW DICTIONARY
def word_to_dict(word):
    enumerated = enumerate(word)
    index_letter_list = list(enumerated)
    wordDict = dict(index_letter_list)
    index_letter_dict = {}
    for key, value in wordDict.items():
        if value not in index_letter_dict:
            index_letter_dict[key] = str(value)
        else:
            index_letter_dict[key].append(str(value))
    return index_letter_dict

#word_guessed: string -> bool
#if the letter values in the guessed word and secret word
#dictionaries match then it returns True, else False
def word_guessed(guess, secret_word):
    g_dict = word_to_dict(guess)
    sw_dict = word_to_dict(secret_word)
    count = 0
    for i in range(0,5):
        if g_dict[i] == sw_dict[i]:
            count +=1
    if count == 5:
        return True
    else:
        return False

#assign_color: string -> dict
#EXPECTS a five-letter word and assigns colors to each index in the word
#based off of the letter.
#RETURNS dictionary {0: 'green', 1: 'yellow', 2: '', 3: 'green', 4: ''}

#slight problem: if a letter has already been entered as green but
#comes up again, it comes back as yellow.
    #ex: sw = 'beach', guess = 'beeps'
    #the first e is green, second one yellow because it is in the word!
def assign_color(guess, secret_word):
    index = 0
    index_color_dict = {}
    g_dict = word_to_dict(guess)        #{0: ['h'], 1: ['e'], 2: ['l'], 3: ['l'], 4: ['o']}
    sw_dict = word_to_dict(secret_word) #{0: ['b'], 1: ['e'], 2: ['a'], 3: ['c'], 4: ['h']}
    color = ''
    for i in range(0,5):
        inword = guess[i] in secret_word #True or False
        if inword: 
            color = 'gold'
        else:
            color = 'light goldenrod yellow'
        if sw_dict[i] == g_dict[i]: 
            color = 'DarkOliveGreen'
        index_color_dict.update({index:color})
        index += 1
    return index_color_dict

