"""
ProgressBar Element

Exercise 1
Make a vertical Progress Bar that shows progress increasing using a button

Instructions:
Your program will display the value of a counter as it counts up to 20
Create a layout that has 3 elements
A vertical Progress Bar that is 20 chars (rows) by 30 pixels. The Maximum value for your Progress Bar should be 20
A Text Element for showing your counter's value
A Button with the text "Increment"
When the Increment button is clicked:
Increment your counter
Display the current counter value in your Text Element
Update the Progress Bar using the counter's value
"""
import PySimpleGUI as sg

# Create the layout as described in the exercise
layout = [[sg.Text('A typical custom progress meter')],
              [sg.ProgressBar(100, orientation='v', size_px=(100, 10), key='-PROGRESS-', )],
          [sg.Text('Reading  ', key='-OUTPUT-')],
              [sg.Button('Increment', key='-INC-')]]

window = sg.Window("Progress Bars", layout)

counter = 0
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-INC-' :
        counter += 1
        window['-PROGRESS-'].update(counter * 5)
        window['-OUTPUT-'].update(f'Counter = {counter}')

    # add your event processing here

window.close()