import PySimpleGUI as sg
from character import Character

path = "../saved_characters.json"


# Update function
def update():
    char = Character()
    char_data = char.get_data()

    # Class and race details
    window['-class-'].update("Class: {}".format(char_data['class'].capitalize()))
    window['-race-'].update("Race: {}".format(char_data['race'].capitalize()))
    window['-size-'].update('  Size: {}'.format(char_data['size']))
    window['-speed-'].update('  Speed: {}ft'.format(char_data['speed']))

    # Attribute details
    window['-str-'].update("  Strength: {}".format(char_data['attributes']['Strength']))
    window['-dex-'].update('  Dexterity: {}'.format(char_data['attributes']['Dexterity']))
    window['-con-'].update('  Constitution: {}'.format(char_data['attributes']['Constitution']))
    window['-int-'].update("  Intelligence: {}".format(char_data['attributes']['Intelligence']))
    window['-wis-'].update('  Wisdom: {}'.format(char_data['attributes']['Wisdom']))
    window['-cha-'].update('  Charisma: {}'.format(char_data['attributes']['Charisma']))


# Define the window's contents i.e. layout
layout = [
        [sg.Text('Class: ', key='-class-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('Race: ', key='-race-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Size: ', key='-size-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Speed: ', key='-speed-', size=(25, 1), font='Helvetica 11')],

        [sg.Text('Attributes: ', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Strength: ', key='-str-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Dexterity: ', key='-dex-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Constitution: ', key='-con-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Intelligence: ', key='-int-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Wisdom: ', key='-wis-', size=(25, 1), font='Helvetica 11')],
        [sg.Text('  Charisma: ', key='-cha-', size=(25, 1), font='Helvetica 11')],
        [[sg.Button('Save', enable_events=True, font='Helvetica 11')],
            [sg.Button('Roll', enable_events=True, font='Helvetica 11')],
            [sg.Button('Exit', enable_events=True, font='Helvetica 11')]]
    ]

# Create the window
window = sg.Window('CharCreator', layout, size=(350, 400))

# Event loop
while True:
    event, values = window.read()
    update()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Roll':
        update()
    if event == 'Save':
        #save()
        break
window.close()
