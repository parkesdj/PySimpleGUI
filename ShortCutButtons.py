"""
Lesson 34
Button Element - Shortcuts

Exercise 1
Replace conventional Buttons with shortcut equivalents

Instructions:
Replace the Button Elements in the layout with their shortcut alias
Print the event each time through your event loop to see what is generated when you click the Button
Break from your event loop if the window is closed or one of the 3 Buttons in the example that would
logically close a window is clicked.
"""

import PySimpleGUI as sg

sg.theme('DarkAmber')

# Replace these Buttons with their "Shorttcut" version
layout = [  [sg.Text('Button Shortcuts')],
            [sg.Ok(), sg.Cancel(), sg.Yes(), sg.No()],
            [sg.Open(), sg.Save(), sg.Quit(), sg.Exit()],
            [sg.Submit(), sg.Help()],]

window = sg.Window('Button Shortcuts', layout)

# In the event loop, check for window closed and other buttons that maybe should close a window
# Also print the event each time through the loop
while True:
    event, values = window.read()
    print(event)
    if event in (sg.WIN_CLOSED, 'Exit', 'Quit', 'Cancel'):
        break


window.close()