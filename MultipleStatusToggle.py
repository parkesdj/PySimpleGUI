import PySimpleGUI as sg

graph = sg.Graph((140, 140), (0, 0), (140, 140), background_color='blue')

status = ['green', 'red']

def update_led(i, colour):
    graph.draw_circle((i, 70), radius=18, fill_color=colour, line_width=2)
    return

count = 0
scount = 0
rcount = 0

layout = [[graph], [sg.Button('Main'), sg.Button('Stdb'), sg.Button('Resv')]]

window = sg.Window('Network Status', layout, element_justification='c', background_color='blue', finalize=True)

for i in range(20, 170, 50):
    graph.draw_circle((i, 70), radius=18, fill_color='green', line_width=2)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Main':
        count = count + 1
        if count == 2:
            count = 0
        update_led(20, status[count])

    if event == 'Stdb':
        scount = scount + 1
        if scount == 2:
            scount = 0
        update_led(70, status[scount])

    if event == 'Resv':
        rcount = rcount + 1
        if rcount == 2 :
            rcount = 0
        update_led(120, status[rcount])


window.close()