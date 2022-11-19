"""
Slider Element

Exercise 1
Make an equalizer GUI with Bass, Mid and Treble settings

Instructions:
Make a window that implements a basic equalizer
Use 3 sliders that have a range of 0 to 100
Add a label under each slider
You don't have to be precise, a single Text element with spaces between each label is fine
Include 1 buttons
Ok - Shows a popup of the values dictionary returned from window.read()
Reset - Sets the values to 0 for all sliders
Slider in the Call Reference Documentation
"""
import PySimpleGUI as sg

layout = [[sg.Text('Equalizer', font='Default 15')],
          [sg.Slider((0, 100), orientation='v', size=(10, 20), enable_events=True, k=f'-BASS-'),
          sg.Slider((0, 100), orientation='v', size=(10, 20), enable_events=True, k=f'-MIDD-'),
          sg.Slider((0, 100), orientation='v', size=(10, 20), enable_events=True, k=f'-TREB-')],
          [sg.Text('     Bass      Middle    Treble')],
          [sg.Button('Ok'), sg.Button('Reset')]]

window = sg.Window('Equalizer', layout)

while True:
    event, values = window.read()
    print(values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Ok':
        sg.popup(('Bass', values['-BASS-']), ('Mid', values['-MIDD-']), ('Treble', values['-TREB-']), title='Values')
    if event == 'Reset':
        window['-BASS-'].update(0)
        window['-MIDD-'].update(0)
        window['-TREB-'].update(0)


window.close()

