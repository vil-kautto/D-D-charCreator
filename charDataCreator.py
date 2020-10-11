import json


def addWizardData(classData):
    print("Adding class data: wizard")
    
    cantrips = [
        "Acid Splash",
        "Chill Touch",
        "Dancing Lights",
        "Fire Bolt",
        "Light",
        "Mage Hand",
        "Mending",
        "Message",
        "Minor Illusion",
        "Poison Spray",
        "Prestidigitation",
        "Ray of Frost",
        "Shoking Grasp",
        "True Strike",
        ]
    print("{} {}".format(len(cantrips), "cantrips added"))
    classData["cantrips"] = cantrips
    
    spells = [
        "Alarm",
        "Burning Hands",
        "Charm Person",
        "Color Spary",
        "Comprehend Languages",
        "Detect Magic",
        "Disguise Self",
        "Expeditious Retreat",
        "False Life",
        "Feather Fall",
        "Find Familiar",
        "Fog Cloud",
        "Grease",
        "Identify",
        "Illusory Script",
        "Jump",
        "Longstrider",
        "Mage armor",
        "Magic Missile",
        "Protection from Evil and Good",
        "Shield",
        "Silent Image",
        "Sleep",
        "Thunderwave",
        "Unseen Servant",
    ]
    print("{} {}".format(len(spells), "spells added"))
    classData["spells"] = spells
    
    proficiencies = {
        "Armor": "None",
        "Weapons": [
            "Daggers",
            "Darts",
            "Slings",
            "Quarterstaffs",
            "Light Crossbows"
        ],
        "Skills": "Int/Wis Subskills"
    }
    print("{} {}".format(len(proficiencies), "proficiencies added"))
    classData["proficiencies"] = proficiencies
    
    health =  {
        "hit_die": "1d6",
        "hp": "1d6 + Constitution modifier",
        "hp_scale": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Int/Wis"
        }
    
    print("{} {}".format(len(health), "health items added"))
    classData["health"] = health 
    
    return classData


def addWarlockData(classData):
    print("Adding class data: warlock")
    
    cantrips = [
        "Blade Ward",
        "Booming Blade",
        "Chill Touch",
        "Create Bonfire",
        "Eldrich Blast",
        "Friends",
        "Frostbite",
        "Green-Flame Blade",
        "Infestation",
        "Lightning Lure",
        "Mage Hand",
        "Magic Stone",
        "Mind Sliver",
        "Minor Illusion",
        "Poison Spray",
        "Prestidigitation",
        "Sword Burst",
        "Thunderclap",
        "Toll the Dead",
        "True Strike",
        ]
    print("{} {}".format(len(cantrips), "cantrips added"))
    classData["cantrips"] = cantrips
    
    spells = [
        "Armor of Agathys",
        "Arms of Hadar",
        "Charm Person",
        "Cause Fear",
        "Color Spary",
        "Comprehend Languages",
        "Distort Value",
        "Expeditious Retreat",
        "Hellish Rebuke",
        "Hex",
        "Illusory Script",
        "Protection from Evil and Good",
        "Unseen Servant",
        "Witch Bolt",
    ]
    print("{} {}".format(len(spells), "spells added"))
    classData["spells"] = spells
    
    return classData


data = {}
data["wizard"] = {}
#data["warlock"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}
#data["wizard"] = {}

data["wizard"] = addWizardData(data["wizard"])
#data["warlock"] = addWarlockData(data["warlock"])
print(data)

with open('classData.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)