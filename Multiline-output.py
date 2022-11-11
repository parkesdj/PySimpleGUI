"""
Use an output element to print the numbers 2 to 500
Print the prime numbers as white on red background
Print all the other numbers normally with no color change than the default

Instructions
Use a Multiline element as an output element
In your layout, set parameter so that no values are returned for the element when window is read
Make the size of your Multiline be 10 chars wide by 25 rows high
Use the Multiline Element's print method for the output
If you can't figure out how to determine a prime number, check the hints
Use a Button (e.g. named "Start") to start the printing
At the top of the window show the text "Prime numbers 2 to 500". Use the same text for the Window's title
Remember to always check to see if the window has been closed after you read it.


"""
import PySimpleGUI as sg

layout = [[sg.Text('MultiLine Output')], [sg.Multiline( size=(10, 25), disabled=True,
                                                        autoscroll=True, reroute_stdout=True)],
          [sg.Button('Go'), sg.Button('Erase'), sg.Button('Exit')]]

window = sg.Window('', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Go':
        for num in range(2, 30):
            for q in range(2, num):
                if (num % q) == 0:
                    break
                print(num)


window.close()
