import PySimpleGUI as sg
import os
from pathlib import Path
from statistics import mean

#Haley Hill
#May 3, 2022

#RUN THIS FILE :-) wordleFunctions.py and 5letterwords.txt should be in same folder!
#-------------------------------------------------------------------------------
from wordleFunctions import * #<-- file with wordle logic!
#'DarkOliveGreen', 'gold', 'light goldenrod yellow'<-this one's the default color

import string
alphabet = string.ascii_uppercase
def subtract_strings(a, b):
    return ''.join(a.rsplit(b))

#-------------------------------------------------------------------------------
sg.theme('darkgreen')

#----USED IN THE LAYOUT----
sgLetterList = [sg.Text(size=(2, 1), key='-OUTPUT1-',
    background_color = 'light goldenrod yellow', visible = True),
                sg.Text(size=(2, 1), key='-OUTPUT2-',
    background_color = 'light goldenrod yellow', visible = True),
                sg.Text(size=(2, 1), key='-OUTPUT3-',
    background_color = 'light goldenrod yellow', visible = True),
                sg.Text(size=(2, 1), key='-OUTPUT4-',
    background_color = 'light goldenrod yellow', visible = True),
                sg.Text(size=(2, 1), key='-OUTPUT5-',
    background_color = 'light goldenrod yellow', visible = True)]

sgFillIn = [sg.Text(size=(2, 1), key='0',   #key is the same as str(key) in Guess.items()
    background_color = 'gold', visible = True),
                sg.Text(size=(2, 1), key='1',
    background_color = 'orange1', visible = True),
                sg.Text(size=(2, 1), key='2',
    background_color = 'coral', visible = True),
                sg.Text(size=(2, 1), key='3',
    background_color = 'coral2', visible = True),
                sg.Text(size=(2, 1), key='4',
    background_color = 'tomato2', visible = True)]

Instructions = 'enter your guess below!'

#----LAYOUT----
layout = [
    
    sgLetterList,
    
    [sg.Text('enter your guess below!', key = '-INSTRUCTIONS-'), sg.Push(), sg.Text('0/6', key = '-NUMTRIES-')],
    
    [sg.Input(key='-IN-', visible = True)],
    
    [(sg.Button('ok'), sg.Button('exit'), sg.Text(size=(35, 2), key = '-WORDBANK-',
    background_color = 'light goldenrod yellow', visible = False))],

    [sg.Text(size=(40, 2), key = '-GUESSBANK-', visible = False)],

    sgFillIn,

    [sg.Text(size=(45, 1), key = '-LETGUESSED-', background_color = 'light goldenrod yellow', visible = False)]

    ]

#----MAKING THE WINDOW----
window = sg.Window("WORDLE", layout, font=('comicsans',14))

#---
letters_guessed = []
words_guessed = []
index_color = {0: '', 1: '', 2: '', 3: '', 4: ''} #used in sgfillin
#---

#-----EVENT LOOP----
#event = what a user does (enter a word)
#value = letters given, etc ('hello')
win = False
count = 0
MAXGUESSES = 6
while True:
    event, values = window.read()
    # - NOPE BUTTON -
    if event == sg.WIN_CLOSED or event == 'exit':
        break
    #- OK BUTTON -
    if event == 'ok':
        text = values['-IN-']
        if len(text) == 5:
            count += 1
            window['-INSTRUCTIONS-'].update('enter your guess below!') 
            window['-IN-'].update("")
            window['-NUMTRIES-'].update(str(count) +'/6')

            #SQUARES VISIBLE
            window['-OUTPUT1-'].update(visible = True)
            window['-OUTPUT2-'].update(visible = True)
            window['-OUTPUT3-'].update(visible = True)
            window['-OUTPUT4-'].update(visible = True)
            window['-OUTPUT5-'].update(visible = True)
            #CHANGING SQUARE COLOR GREEN/YELLOW/DEFAULT
            Guess = assign_color(str(values['-IN-']), secret_word) #index:color dictionary
            window['-OUTPUT1-'].update(background_color=Guess[0])
            window['-OUTPUT2-'].update(background_color=Guess[1])
            window['-OUTPUT3-'].update(background_color=Guess[2])
            window['-OUTPUT4-'].update(background_color=Guess[3])
            window['-OUTPUT5-'].update(background_color=Guess[4])
            #PUTTING LETTERS IN EACH SQUARE
            window['-OUTPUT1-'].update(" " + values['-IN-'][0].upper())
            window['-OUTPUT2-'].update(" " + values['-IN-'][1].upper())
            window['-OUTPUT3-'].update(" " + values['-IN-'][2].upper())
            window['-OUTPUT4-'].update(" " + values['-IN-'][3].upper())
            window['-OUTPUT5-'].update(" " + values['-IN-'][4].upper())
        
            #----
            #WORDBANK: LETTERS LEFT
            [letters_guessed.append(i) for i in values['-IN-'].upper()]
            letters_guessed.sort()
            guessSet = set(letters_guessed) #using this in [-LETGUESSED-]
            alphaSet = set(alphabet)
            lettersLeft = list(alphaSet - guessSet)
            lettersLeft.sort()
            window['-WORDBANK-'].update(visible = True)
            window['-WORDBANK-'].update("LETTERS LEFT:  " + '  '.join(lettersLeft))
        
            #---
            #GUESSBANK: WORDS GUESSED
            [words_guessed.append(i) for i in values['-IN-'].upper()]
            words_guessed.append('       ')
            window['-GUESSBANK-'].update(visible = True)
            window['-GUESSBANK-'].update(' '.join(words_guessed))

            #SGFILLIN
            for key, value in Guess.items():
                if value == 'DarkOliveGreen':
                    index_color.update({key:'DarkOliveGreen'})
                    window[str(key)].update(" " + values['-IN-'][key].upper())
            #---
            #LETGUESSED
            swSet = set(secret_word.upper())
            correctLetters = [] 
            for i in guessSet:
                if i in swSet:
                    correctLetters.append(i)

            if len(correctLetters) != 0:
                window['-LETGUESSED-'].update(visible = True)
                window['-LETGUESSED-'].update('          THE ~SECRET WORD~ CONTAINS:  ' + '  '.join(correctLetters))

            #---
            #WIN
            win = word_guessed(str(values['-IN-']), secret_word) #win = true if guessed correctly
            if win: # - figure out how to center things in a not gross way ?
                window['-WORDBANK-'].update('                                YOU WIN\n                      !!!  !!!  !!!  !!!  !!!  !!!  !!!')
                window['-INSTRUCTIONS-'].update("don't enter a guess :)")
            #LOSE
            if count == MAXGUESSES:
                window['-WORDBANK-'].update('                   THE SECRET WORD WAS...\n                                  ' + secret_word.upper())
                window['-INSTRUCTIONS-'].update("no tries left!")
        #---
        #IF 'OK' BUT LEN(TEXT) != 5
        else:
            window['-INSTRUCTIONS-'].update('FIVE-LETTER WORD! FIVE-LETTER WORD! AAAHH!')

window.close()
