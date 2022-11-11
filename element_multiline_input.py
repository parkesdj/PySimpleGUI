"""
    The Official Python GUI Programming with PySimpleGUI Course

    Multiline Element
        Scrolled text input/output

    Multiline Input

    Docs: http://www.PySimpleGUI.org
    Built-in help: sg.sdk_help()

    Copyright 2021 PySimpleGUI
"""

import PySimpleGUI as sg

sg.set_options(font='Default 18')

sg.Print('Multiline Input', c='white on red', font='Default 14', keep_on_top=True, size=(60,10), location=(1400, 130))

example_number = 3





#==========================  TEXT, INPUT, MULTILINE EXAMPLE  ==========================
def main_text_input_multiline():

    #------------------------- Layout & Window
    layout = [
        [sg.Text('This is multiple lines\nof text, but no\nscrollbar')],
        [sg.Input(size=(30,1), key='-IN-')],
        [sg.Multiline(size=(30,10), k='-MLINE IN-')],
        [sg.Button('Go'), sg.Button('Exit')],
    ]

    window = sg.Window('Basic Multiline Comparison', layout, keep_on_top=True)

    #------------------------- Event Loop

    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end='')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

    window.close()









#==========================  NOTEPAD EXAMPLE  ==========================
def main_notepad():

    #------------------------- Layout & Window
    layout = [
                [sg.Multiline(size=(80,25), k='-MLINE IN-')],
                [sg.Button('Open'), sg.Button('Save'), sg.Button('Exit')],
             ]

    window = sg.Window('Mini-Notepad', layout, keep_on_top=True, finalize=True, location=(260,120))

    #------------------------- Event Loop

    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end='')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        if event == 'Open':
            with open(__file__, 'r') as f:
                window['-MLINE IN-'].update(value=f.read())

    window.close()










#==========================  CHAT EXAMPLE  ==========================
def main_chat():

    # turning on enable events and enter submits.  Disable rstrip
    #------------------------- Layout & Window
    layout = [[sg.Output(size=(40,10))],
              [sg.Multiline(size=(40,4), k='-MLINE IN-', justification='r', focus=True, enter_submits=True, enable_events=True, rstrip=False),
               sg.B('Send', bind_return_key=True), sg.Exit()]]

    window = sg.Window('Chat', layout, keep_on_top=True)

    #------------------------- Event Loop

    while True:
        event, values = window.read()

        sg.Print(event, end=' ')
        sg.Print(values, c='white on green', end='')
        sg.Print()

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # do manual removal of extra \n
        # perform an extra update so that the text is right justified
        if event == '-MLINE IN-':                           # if multiline event, remove the extra \n if present
            values[event] = window[event].get()             # get the latest value so no characters are accidently lost
            if values[event].endswith('\n'):                # if ends with \n then remove the last char
                values[event] = values[event][:-1]
            window['-MLINE IN-'].update(values[event])      # update with value so that the text is right justified. Typing left justifies the text

        if event == 'Send':
            print(f'You entered: {values["-MLINE IN-"]}')   # print so that it's shown in the output element
            window['-MLINE IN-'].update('')                 # clear the multiline

    window.close()







if __name__ == '__main__':
    examples = [main_text_input_multiline, main_notepad, main_chat]
    examples[example_number-1]()