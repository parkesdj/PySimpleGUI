import PySimpleGUI as sg

graph = sg.Graph((600, 600), (0, 0), (10, 75), key='-GRAPH-',  background_color='lightblue',)
#                window size  bottom  units x, y

data_points = [35, 37, 64, 68]

layout = [[graph], [sg.Exit(), sg.Button('Draw')]]

window = sg.Window('My Bar Graph', layout)

while True :
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit') :
        break
    if event == 'Draw':
        for i, data in enumerate(data_points):
            graph.draw_rectangle((i*2+1, data), (i*2+2, 0), fill_color='orange', line_width=0)
            graph.draw_text(f'        {data}', (i*2+1, data+2), font='_ 18')

window.close()