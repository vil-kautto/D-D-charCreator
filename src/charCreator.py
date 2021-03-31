from character import Character

# The program generates new characters until the user stops the program
repeat = True
while repeat:
    if repeat:
        char = Character()
        print("\n\nRoll a new character? (Y/n)")
        user_input = input()
        if 'n' in user_input.lower():
            repeat = False
            print("Shutting down")
        elif 'y' in user_input.lower() or "" == user_input:
            print("rolling a new character")
        else:
            print("Invalid input.")
    else:
        repeat = False
        print("Goodbye")
