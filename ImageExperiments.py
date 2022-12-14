import PySimpleGUI as sg

# r'C:\PySimpleGUI\Demos\images\emojis\blank_stare_112.png'
image_folder = 'C:\PySimpleGUI\Demos\images\emojis\\'
blank = 'blank_stare_112.png'
happy = 'clap_112.png'
sad = 'depressed_112.png'
layout = [[sg.Text('Make Me ...')], [sg.Image(image_folder + blank, key='-EMOJI-')],
          [sg.Button('Sad', key='-SAD-'), sg.Button('Happy', key='-HAPPY-'), sg.Button('Blank', key='-BLANK-')]]

window = sg.Window('Make Me ...', layout, )

while True :

    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit' :
        break
    if event == '-HAPPY-' :
        window['-EMOJI-'].update(image_folder + happy)

    if event == '-SAD-' :
        window['-EMOJI-'].update(image_folder + sad)

    if event == '-BLANK-' :
        window['-EMOJI-'].update(image_folder + blank)
