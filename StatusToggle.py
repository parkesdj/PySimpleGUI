import PySimpleGUI as sg

graph = sg.Graph((40, 40), (0, 0), (40, 40))

status = ['green', 'red']

def led(colour) :
    if colour == 'green':
        return circle('red')
    else:
        return circle('green')

def circle(colour):
    graph.draw_circle((20, 20), radius=18, fill_color=colour, line_width=2)
    return
count = 0
layout = [[graph], [sg.Button('Toggle')]]

window = sg.Window('Network Status', layout, element_justification='c', finalize=True)
led('green')

while True:
    event, values = window.read()
    print(event)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Toggle':
        count = count + 1
        if count == 2:
            count = 0
        led(status[count])
        print(count)

window.close()