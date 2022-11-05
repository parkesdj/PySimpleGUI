'''
Multiline Input

Exercise 1
Write a program that multiplies 2 numbers

Instructions
Make a window that has 2 rows
3 Input Elements and 2 Text Elements
A "Calculate" Button
The first row will resemble this format: 2 x 6 = 12
The location of the 2 and 6 are Input elements
The location of the 12 is also an Input element
the "x" and "=" are Text Elements
Your Input elements should have a size of (8,1) each
When the Calculate button is pressed
Get the values of the first 2 input elements
Convert the 2 values into integers
Multiply the integers
Display the result in the 3rd input element by calling its update method
'''


import PySimpleGUI as sg

s=(8,1)
layout = [[sg.Input(size=s, key='-INT1-'),sg.Text('X'),sg.Input(size=s, key='-INT2-'),sg.Text('='), sg.Input(size=s, key='-ANSWER-')],
          [sg.Button('Calculate', key='-CALC-')]]

window = sg.Window('Multiply', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-CALC-':
        window['-ANSWER-'].update(int(values['-INT1-']) * int(values['-INT2-']))

window.close()