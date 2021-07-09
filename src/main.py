import PySimpleGUI as sg
from character import Character
import json

path = "../saved_characters.json"

char = Character()

# Update function
def update():
    char = Character()
    char_data = char.get_data()

    # Class and race details
    window['-class-'].update("Class: {}".format(char_data['class'].capitalize()))
    window['-race-'].update("Race: {}".format(char_data['race'].capitalize()))
    window['-size-'].update('  Size: {}'.format(char_data['size']))
    window['-speed-'].update('  Speed: {}ft'.format(char_data['speed']))

    attr = char_data['attributes']

    # Attribute details
    window['-str-'].update('  Strength: {}, mod: {:+}'.format(attr['Strength'][0], attr['Strength'][1]))
    window['-dex-'].update('  Dexterity: {}, mod: {:+}'.format(attr['Dexterity'][0], attr['Dexterity'][1]))
    window['-con-'].update('  Constitution: {}, mod: {:+}'.format(attr['Constitution'][0], attr['Constitution'][1]))
    window['-int-'].update('  Intelligence: {}, mod: {:+}'.format(attr['Intelligence'][0], attr['Intelligence'][1]))
    window['-wis-'].update('  Wisdom: {}, mod: {:+}'.format(attr['Wisdom'][0], attr['Wisdom'][1]))
    window['-cha-'].update('  Charisma: {}, mod: {:+}'.format(attr['Charisma'][0], attr['Charisma'][1]))


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
        with open(path, 'a') as outfile:
            json.dump(char.get_data(), outfile, indent=4)
        break
window.close()
