import PySimpleGUI as gui
from character import Character
import json

path = "../saved_characters.json"

char = None
recent = []
saved = []
try:
    saved = json.load(open(path, 'r'))
except FileNotFoundError:
    print("saved characters not found")
finally:
    print("")


# Update function
def update():
    char_data = char.get_data()

    # Class and race details
    window['-class-'].update("Class: {}".format(char_data['class'].capitalize()))
    window['-race-'].update("Race: {}".format(char_data['race'].capitalize()))
    window['-size-'].update('  Size: {}'.format(char_data['size']))
    window['-speed-'].update('  Speed: {}ft'.format(char_data['speed']))

    # Attribute details
    attr = []
    for key, value in char_data['attributes'].items():
        attribute = '{}: {}; mod {:+}'.format(key, value[0], value[1])
        attr.append(attribute)

    window['-attr-'].update(attr)

    # class and racial features
    window['-race feat-'].update(char_data['features'][0])
    window['-class feat-'].update(char_data['features'][1])

    # storing character data
    window['-recent-'].update(recent)
    window['-saved-'].update(saved)


def find(list, item):
    char = [item for item in list if item['name'] == item]
    update()


# the character stat layout
stat_layout = [
    [gui.Text('Class: ', key='-class-', size=(20, 1), font='Helvetica 11')],
    [gui.Text('Race: ', key='-race-', size=(20, 1), font='Helvetica 11')],
    [gui.Text('  Size: ', key='-size-', size=(20, 1), font='Helvetica 11')],
    [gui.Text('  Speed: ', key='-speed-', size=(20, 2), font='Helvetica 11')],

    [gui.Text('Attributes: ', size=(20, 1), font='Helvetica 11')],
    [gui.Listbox(values=[], enable_events=True, size=(25, 6), key="-attr-")],
    [gui.Button('Save', enable_events=True, font='Helvetica 11'),
     gui.Button('Roll', enable_events=True, font='Helvetica 11'),
     gui.Button('Exit', enable_events=True, font='Helvetica 11')
     ]
]

# The feature section layout
feature_layout = [
    [gui.Text('Racial Features: ', size=(25, 1), font='Helvetica 11')],
    [gui.Listbox(values=[], enable_events=True, size=(30, 8), key="-race feat-")],
    [gui.Text('Class Features: ', size=(25, 1), font='Helvetica 11')],
    [gui.Listbox(values=[], enable_events=True, size=(30, 8), key="-class feat-")],
]


# The character section layout
character_layout = [
    [gui.Text('Recent characters:', size=(20, 1), font='Helvetica 11')],
    [gui.Listbox(values=[], enable_events=True, size=(25, 7), key="-recent-")],
    [gui.Text('Saved characters:', size=(20, 1), font='Helvetica 11')],
    [gui.Listbox(values=[], enable_events=True, size=(25, 7), key="-saved-")],
]

# The general layout used in the application
layout = [
    [
        gui.Column(character_layout),
        gui.VSeperator(),
        gui.Column(stat_layout),
        gui.VSeperator(),
        gui.Column(feature_layout),
    ]
]


# Create the window
window = gui.Window('CharCreator', layout, size=(700, 400))


# Event loop
while True:
    event, values = window.read()
    if event in (gui.WIN_CLOSED, 'Exit'):
        break
    if event == 'Roll':
        char = Character()
        recent.append(char)
        update()
    #if event == '-recent-':
        #find(recent, "null")
    if event == 'Save':
        with open(path, 'w') as outfile:
            saved.append(char.get_data())
            json.dump(saved, outfile, indent=4)
            update()
window.close()
