import PySimpleGUI as sg

#Haley Hill
#PySimpleGUI demo! :-)

sg.theme('HotDogStand')

#ALL THE STUFF INSIDE THE WINDOW
layout = [
    [sg.Text('enter a word:'), sg.Text(size=(7, 1), key='-OUTPUT-',
    background_color = 'black', visible = False)],
    [sg.Input(key='-IN-')],
    [sg.Button('OK'), sg.Button('EXIT'), sg.Text(size=(32, 2))]
    ]

#MAKING THE WINDOW
window = sg.Window('TITLE!!', layout, font=('comicsans',14))

#EVENT LOOP
# - event = what a user does (entering a word)
# - value = leters given, etc ('hello')
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break
    if event == 'OK':
        window['-OUTPUT-'].update(visible = True)         #the black bar is now visible
        window['-OUTPUT-'].update(values['-IN-'].upper()) #put the word given over the bar
        
window.close()


#ALL THE COLORS!
#https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Color_Names_Smaller_List.py

#ALL THE THEMES!
#https://www.geeksforgeeks.org/themes-in-pysimplegui/

#THE PYSIMPLEGUI COOKBOOK
#https://pysimplegui.readthedocs.io/en/latest/cookbook/#the-demo-programs-are-also-recipes
