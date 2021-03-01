import json

# Simply defines class features based on available data and translates it into json format

# Barbarian class Data
def addBarbarianData(classData):
    classData["type"] = "warrior"
    print("Adding class data: Barbarian")
    
	# Class proficiencies
    proficiencies = {
        "Armor": "Light armour, medium armour, shields",
        "Weapons": "Simple weapons, Martial weapons",
        "Tools": "None",
        "Skills (2)": "Animal Handling, Athletics, Intimidation, Nature, Perception, Survival"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    classData["proficiencies"] = proficiencies
	
    classData["cantrips"] = ["none"]
    classData["spells"] = ["none"]
    
	# class start equipment
    equipment =  {
        "Primary": ["Greataxe", "Any martial weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
		"Tertiary": [],
        "Bags": ["Explorer's bag & 4 javelins"]
        
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    classData["equipment"] = equipment
	
	#Class Features
    features = [
        "Rage",
        "Unarmored defence"
    ]
    print("{} {}".format(len(features), "features added"))
    classData["features"] = features
    
	# class health data
    health =  {
        "Hit Die": "1d12",
        "Hit Points": "1d12 + Constitution modifier",
        "Hit Point Scaling": "1d12 (or 7) + Constitution modifier",
        "Saving Throws": "Str/Const"
    }
    print("{} {}".format(len(health), "health entries added"))
    classData["health"] = health 
    
    return classData


# Wisard class data
def addWizardData(classData):
    print("Adding class data: Wizard")
    classData["type"] = "spellcaster"
    
	#Class cantrips
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
    
	# Class spells
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
    
	# class proficiencies
    proficiencies = {
        "Armor": "None",
        "Weapons": "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows",
        "Tools": "None",
        "Skills (2)": "Arcane, History, Investigation, Medicine, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    classData["proficiencies"] = proficiencies
    
	# class start equipment
    equipment =  {
        "Primary": ["Quarterstaff", "Dagger"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
		"Tertiary": ["Spellbook"],
        "Bags": ["Scholar's bag", "Explorer's bag"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    classData["equipment"] = equipment

	#Class Features
    features = [
        "Spellcasting",
        "Arcane Recovery"
    ]
    print("{} {}".format(len(features), "features added"))
    classData["features"] = features
    
    
	# class health data
    health =  {
        "Hit Die": "1d6",
        "Hit Points": "1d6 + Constitution modifier",
        "Hit Point Scaling": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    print("{} {}".format(len(health), "health entries added"))
    classData["health"] = health 
    
    return classData

# Warlock class Data
def addWarlockData(classData):
    print("Adding class data: Warlock")
    classData["type"] = "spellcaster"
    
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
	
	# class start equipment
    equipment =  {
        "Primary": ["light crossbow & 20 bolts", "a Simple weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
		"Tertiary": ["Leather armor", "Simple weapon", "2 Daggers"],
        "Bags": ["Scholar's bag", "Dungeoneer's bag"]
    }

    # Class features
    features = [
        "Otherworldly Patron",
        "Pact magic"
    ]
    print("{} {}".format(len(features), "features added"))
    classData["features"] = features
    
    health =  {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    print("{} {}".format(len(health), "health entries added"))
    classData["health"] = health 
    
    return classData


#TODO: details to cantrips, skills and spells
	
data = {}
data["barbarian"] = {}
#data["bard"] = {}
#data["cleric"] = {}
#data["druid"] = {}
#data["fighter"] = {}
#data["monk"] = {}
#data["paladin"] = {}
#data["ranger"] = {}
#data["rogue"] = {}
#data["sorcerer"] = {}
data["wizard"] = {}
data["warlock"] = {}

data["barbarian"] = addBarbarianData(data["barbarian"])
#data["bard"] = addWizardData(data["bard"])
#data["cleric"] = addWizardData(data["barbarian"])
#data["druid"] = addWizardData(data["barbarian"])
#data["fighter"] = addWizardData(data["barbarian"])
#data["monk"] = addWizardData(data["barbarian"])
#data["paladin"] = addWizardData(data["barbarian"])
#data["ranger"] = addWizardData(data["barbarian"])
#data["rogue"] = addWizardData(data["barbarian"])
#data["sorcerer"] = addWizardData(data["barbarian"])
data["wizard"] = addWizardData(data["wizard"])
data["warlock"] = addWarlockData(data["warlock"])
print(data)

with open('class_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)