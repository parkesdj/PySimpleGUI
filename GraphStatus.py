"""
You are going to make a new element using a technique called "User Defined Element".
A User Defined Element is simply a function that returns a PySimpleGUI element or a list of PySimpleGUI element. In this case, your Status element will return a Graph element.

Your Status element will display the status as a circle, much like an LED light.
It will display a colored circle to indicate "status"
Write a function called Status
It should return a Graph element that is 40 pixels by 40 pixels
Write a function called change_status that creates a circle with the specified color
It should take these parameters status_change(window, key, color)
window - your GUI's window
key - the key you used to create your Graph element
color - the color you want the circle to be
When drawing the circle should:
Be roughly centered in the Graph
Have a radius of 18 pixels
Have no line around it
Your layout should have:
3 rows for the Status
On each row have a Text element that says what the status represents and your Status element.
The text for the rows should be - 'Main server:', 'Secondary server:', 'Network Link:'
Include a Button called "Status" as a way to generate an event
In your event loop, change the color of your Status elements to a random color from the list
 of the colors in the variable colors that is pre-defined for you.
When you create your window:
Use a font that's "Default" and has a size of 15
Right justify the elements in the Window
font='Default 15'
element_justification='r'
"""

import PySimpleGUI as sg
import random  # You will use a function from the random standard library to choose a random color

def Status(key):
    return sg.Graph(canvas_size=(40,40), graph_bottom_left=(0,0), graph_top_right=(40,40), key=key)

def status_change(window, key, color):
    window[key].erase()
    window[key].draw_circle((20,20), radius=18, fill_color=color, line_width=0)

colors = ('red', 'green', 'yellow')
alert = ('up', 'down', 'error')

layout = [  [sg.Text('Main server:'), Status('-STATUS MAIN-')],
            [sg.Text('Secondary server:'), Status('-STATUS SECONDARY-')],
            [sg.Text('Network Link:'), Status('-STATUS NETWORK-')],
            [sg.Button('Main'), sg.Button('Stdb'), sg.Button('Nwk')]]

window = sg.Window('Status Elements', layout, element_justification='r', font='Default 15')

while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Main':
        status_change(window, '-STATUS MAIN-', colors[2])
    else:
        status_change(window, '-STATUS MAIN-', colors[1])

    # status_change(window, '-STATUS MAIN-', random.choice(colors))
    status_change(window, '-STATUS SECONDARY-', random.choice(colors))
    status_change(window, '-STATUS NETWORK-', random.choice(colors))


window.close()
