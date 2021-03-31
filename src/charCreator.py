from character import Character
import json


path = "../saved_characters.json"
# The program generates new characters until the user stops the program
repeat = True
while repeat:
    if repeat:
        char = Character()
        print("\n\nRoll a new character? (Yes/no/save)")
        user_input = input()
        if 'n' in user_input.lower():
            repeat = False
            print("Shutting down")
        elif 'y' in user_input.lower() or "" == user_input:
            print("Rolling a new character")
        elif 's' in user_input.lower():
            with open(path, 'a') as outfile:
                json.dump(char.get_data(), outfile, indent=4)
            print("Character saved")
        else:
            print("Invalid input.")
    else:
        print("Goodbye")

