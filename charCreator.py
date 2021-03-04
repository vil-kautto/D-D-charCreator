
from character import Character


# The program generates new characters until the user stops the program
# TODO: create characters via objects
repeat = True
while repeat:
    if repeat:
        char = Character()
        print("\n\nRoll a new character? (Y/n)")
        user_input = input()
        if 'n' in user_input.lower():
            repeat = False
            print("Shutting down")
    else:
        repeat = False
        print("Goodbye")
