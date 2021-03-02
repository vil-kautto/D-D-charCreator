import random
import json

'''
Generates stats based on following model: 4d6 - smallestRoll
Generated stats are between 3-18, minor bias on median
'''


def generate_stat():
    random_nums = [0, 0, 0, 0]
    for i in range(0, 4):
        random_nums[i] = random.randint(1, 6)
    
    # Remove the smallest 
    random_nums.sort();
    # print(random_nums)
    random_nums.pop(0)
    # print(random_nums)
    
    # Getting the sum of a array
    sum = 0
    for i in range(0, 3):
        sum += random_nums[i]
    # print(sum)
    return sum


def define_modifier(value):
    return int(value/2-5) 


def get_random_attr(attr):
    print("\nAttributes:")
    for key, value in attr.items():
        value = generate_stat()
        modifier = define_modifier(value)
        print(' {}: {}, Modifier: {:+d}'.format( key, value , modifier))
    return attr    


def get_class_name(i):
    print(i)
    classes = {
        1:  "barbarian",
        2:  "bard",
        3:  "cleric",
        4:  "wizard",
        5:  "wizard",
        6:  "wizard",
        7:  "wizard",
        8:  "wizard",
        9:  "wizard",
        10: "wizard",
        11: "warlock",
        12: "wizard",
    }
    return classes[i]


'''
Picks spells, cantrips, proficiencies and health stats for wizard class from external data files
'''


def get_character(character):
    if character["type"] == "spellcaster" :
        cantrips = character["cantrips"] 
        print("\nCantrips:")
        for i in range(0, 3):
            random_num = random.randint(0, len(cantrips)-1)
            print(" {}: {}".format(i+1, cantrips[random_num]))
            cantrips.pop(random_num)
        
        spells = character["spells"]
        print("\nSpells:")
        for i in range(0, 6):
            random_num = random.randint(0, len(spells)-1)
            print(" {}: {}".format(i+1, spells[random_num]))
            spells.pop(random_num)
        
    proficiencies = character["proficiencies"]
    print("\nProficiencies:")
    for key, value in proficiencies.items():
        print(" {}: {}".format(key, value))
        
    health = character["health"]
    print("\nHealth:")
    for key, value in health.items():
        print(" {}: {}".format(key, value))


repeat = True
while repeat:
    # char_data contains all character related data
    char_data = {}
    char_data["attributes"] = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    # Fetching class data from external file generated by CharDataCreator.py
    class_data = {}
    with open('./class_data.json') as file:
        class_data = json.load(file)
    if repeat:
        className = get_class_name(random.randint(1, 12))
        print('Class: {}'.format(className))

        # Generating, modifying and printing random attributes
        char_data['attributes'] = get_random_attr(char_data['attributes'])

        # class_data[className] =
        get_character(class_data[className])
        print("\n\nRoll a new character? (Y/n)")
        user_input = input()
        if 'n' in user_input.lower():
            repeat = False
            print("Shutting down")
    else:
        repeat = False
        print("Goodbye")
