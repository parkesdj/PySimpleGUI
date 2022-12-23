import PySimpleGUI as sg

value = 0
data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
heads = ['Heading 1', 'Heading 2', 'Heading 3', 'Heading 4']
layout = [[sg.Table(values=data, headings=heads, def_col_width=10,
                    vertical_scroll_only=True,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=5,
                    alternating_row_color=sg.theme_button_color()[1],
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    bind_return_key=True,
                    expand_x=True,
                    expand_y=True,
                    right_click_selects=True,
                    enable_click_events=True
                    )],
          [sg.Text('Value Selected'), sg.Text(value, key='-VAL-')],
          [sg.Exit(), sg.Button('Edit Value', key='-EDIT-'), sg.Input(key='-INP-', enable_events=True)]]

window = sg.Window('Table', layout)

while True :
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit') :
        break
    if '+CLICKED+' in event :
        row = event[2][0]
        column = event[2][1]
        value = data[row][column]
        window['-VAL-'].update(value)
    if event == '-EDIT-':
        print(values.get('-INP-'))
        new_val = values.get('-INP-')
        data[row][column] = new_val
        print(data)
        window['-TABLE-'].update(data)
