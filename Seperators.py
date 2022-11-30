"""
Separator Element

Exercise 1
Use vertical and horizontal Separator Elements to divide up a window's layout

Instructions:
In this exercise, you're simply trying to break up the visual parts of the interface so they're more easily visible
You are to make a layout with 3 rows. Between the elements, add Separators.
The rows are as follows:
Listbox (size of 20 x 10), Multiline (size 30 x 10)
Multiline (size 60 x 10)
Exit Button
"""
import PySimpleGUI as sg

color_names = ('red', 'green', 'blue', 'yellow', 'blue', 'blue green', 'sky blue', 'navy blue')

layout = [[sg.Listbox(color_names, size=(20, 10), key='-LB1-', no_scrollbar=True),sg.VerticalSeparator('yellow'), sg.Multiline(size=(30, 10),
                                                                             key='-ML1-', no_scrollbar=True)],
          [sg.HorizontalSeparator('yellow')],
          [sg.Multiline(size=(60, 10), key='-ML2-', no_scrollbar=True)],
          [sg.Exit()]]

window = sg.Window('Seperator Exercise', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break