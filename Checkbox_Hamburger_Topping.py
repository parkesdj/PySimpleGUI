"""
As part of an order entry GUI, make the Hamburger Toppings Section

Include a "Place Order" button
When clicked it will show a popup with containing the values dictionary returned from `window.read()
Include a "Clear" button that will clear all checkboxes
Make each checkbox on a separate row in the window. Multiple ways of solving this including:
Manually making your layout with a checkbox per row
Using a list comprehension inside your layout
Building the layout in code, using a for loop for the toppings portion
Checkbox in the Call Reference Documentation
https://pysimplegui.readthedocs.io/en/latest/call%20reference/#checkbox-element

"""
import PySimpleGUI as sg

toppings = ['Cheese', 'Lettuce', 'Tomato', 'Pickles', 'Onions', 'Ketchup', 'Mayonnaise', 'Mustard']

layout = [  [sg.Text('Hamburger Toppings', font='Default 15')],
            [[sg.Checkbox(topping, key=topping)] for topping in toppings],
            [sg.Button('Place Order'), sg.Button('Clear')]]


window = sg.Window('Food Order GUI', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Place Order':
        order = []
        for i in values:
            if values[i] == True:
                order.append(i)
        sg.popup(order, title='Values', location=(1000, 400))
    elif event == 'Clear':
        for topping in toppings:
            window[topping].update(False)
window.close()
