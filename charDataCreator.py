import json


def addWizardData(classData):
    print("Adding class data: Wizard")
    
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
    print("{} {}".format(len(cantrips), "cantrip entries added"))
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
    print("{} {}".format(len(spells), "spell entries added"))
    classData["spells"] = spells
    
    proficiencies = {
        "Armor": "None",
        "Weapons": "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows",
        "Tools": "None",
        "Skills (2)": "Arcane, History, Investigation, Medicine, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    classData["proficiencies"] = proficiencies
    
    equipment =  {
        "Weapons": ["Quarterstaff", "Dagger"],
        "Pouches": ["Component Pouch", "Arcane Focus"],
        "Bags": ["Scholar's bag", "Explorer's bag"],
        "Spellbook": "Spellbook"
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    classData["equipment"] = equipment
    
    health =  {
        "Hit Die": "1d6",
        "Hit Points": "1d6 + Constitution modifier",
        "Hit Point Scaling": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    print("{} {}".format(len(health), "health entries added"))
    classData["health"] = health 
    
    
    
    return classData


def addWarlockData(classData):
    print("Adding class data: Warlock")
    
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
    
    proficiencies = {
        "Armor": "Light armor",
        "Weapons": "Simple weapons and light crossbows",
        "Tools": "None",
        "Skills (2)": "Archana, Deception, History, Intimidation, Investigation, Nature, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    classData["proficiencies"] = proficiencies
    
    health =  {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    print("{} {}".format(len(health), "health entries added"))
    classData["health"] = health 
    
    return classData


data = {}
data["Wizard"] = {}
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

data["Wizard"] = addWizardData(data["Wizard"])
#data["Warlock"] = addWarlockData(data["Warlock"])
print(data)

with open('classData.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)