"""
Lesson 32
Button Element - Buttons with Images

Exercise 1
Make the Play and Stop portion of a Media Player

Instructions:
You have been given artwork assets by the artists in your team. The assets are 2 buttons, a play and a stop button.

Your task is to use these images in a window to implement the play and stop portion of the media player.

Make a window with 2 Button elements
Use the provided Base64 encoded images
The artwork is larger than needed in this portion of the project, use your Button Element to reduce the image size shown
to the user to be 1/3 the original size
The buttons should blend completely into the background (they should appear round only)
When each button is clicked, show a popup indicating what would happen in the program when complete (e.g. "Starting Playback")
"Button Element" in the Call Reference Documentation
"""
import PySimpleGUI as sg


def main():
    layout = [[sg.Text('Media Player')],
              [sg.Button(image_data=play_image, image_subsample=3, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='-PLAY-'),
              sg.Button(image_data=stop_image, image_subsample=3, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, key='-STOP-')]
              # Write your Button Elements
              ]

    window = sg.Window('Media Player', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == '-PLAY-':
            sg.Popup('Starting Playback')
        if event == '-STOP-':
            sg.Popup('Stopping Playback')

    # add your event processing here....

    window.close()


if __name__ == '__main__':
    # these are the Base64 encoded buttons for your use provided by the artists on your team
    play_image = b'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'
    stop_image = b'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'

    main()