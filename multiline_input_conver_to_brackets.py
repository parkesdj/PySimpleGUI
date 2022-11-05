"""
Multiline Input

Exercise 1
Instructions:
Read multiple lines of text using a Multiline Element, add parenthesis around each line, and write
results back into the Multiline Element

Create a window with a Multiline Element with a size of (30,10) and a Button with the text "Convert"
When "Convert" button is pressed, each line entered is converted to have "( )" around the line
For example this text:

1
2
3

Should be converted to:

(1)
(2)
(3)

Write the changes lines back to the Multiline Element by using its update method
"""
import PySimpleGUI as sg

layout = [ [sg.Multiline(size=(30,10), key='-MLIN-')], # Your multline element goes here
            [sg.Button('Convert')]]

window = sg.Window('Multiline Convert', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event,values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Convert':
        lines = values['-MLIN-'].split('\n')
        newlines = []
        print(lines)
        for i in range(len(lines)):
            newlines.append('('+lines[i]+')')
        print(newlines)
        window['-MLIN-'].update('\n'.join(newlines))

    # HERE add your code to look for the Convert event
    #   when Convert found, process the Multiline input as per the instructions
window.close()
