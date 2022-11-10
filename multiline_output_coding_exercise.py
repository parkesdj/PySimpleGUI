"""
Print numbers 0 to 999 in an Output Element

Instructions:
While not recommended as the preferred way to re-route stdout, the Output element is still fine to use.

Make your Output element have a size of 40 chars wide by 20 rows high
Print the numbers 0 to 999 when a "Count" button is clicked
"""

import PySimpleGUI as sg

layout = [[sg.Text('Counting 1 to 1000:')],
          [sg.Multiline(size=(48,20),key='-MLINE-',autoscroll=True, disabled=True, reroute_stdout=True)],
          [sg.Button('Count'), sg.Button('Clear')]
          ]

window = sg.Window('Output Element', layout)
mline = window['-MLINE-']  # type: sg.Multiline
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Count':
        for i in range(1,1000):
            print(i)
    if event == 'Clear':
        mline.update('')
        # mline.update('')

window.close()