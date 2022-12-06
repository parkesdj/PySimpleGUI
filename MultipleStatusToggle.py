import PySimpleGUI as sg

graph = sg.Graph((140, 140), (0, 0), (140, 140))

status = ['green', 'red']

def led(colour) :
    if colour == 'green':
        return ('red')
    else:
        return circle('green')

for i in range(20, 170, 50):
    graph.draw_circle((i, 70), radius=18, fill_color=colour, line_width=2)
    return= 0
layout = [[graph], [sg.Button('Main'), sg.Button('Stdb'), sg.Button('Resv')]]

window = sg.Window('Network Status', layout, element_justification='c', background_color='yellow', finalize=True)
led('green')

while True:
    event, values = window.read()
    print(event)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Main':
        count = count + 1
        if count == 2:
            count = 0
        update_led(20, status[count])
        print(count)

    if event == 'Stdb':
        count = count + 1
        if count == 2:
            count = 0
        update_led(70, status[count])
        print(count)

    if event == 'Resv' :
        count = count + 1
        if count == 2 :
            count = 0
        update_led(120, status[count])
        print(count)


window.close()