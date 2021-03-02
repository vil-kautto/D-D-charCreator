import json

# Simply defines class features based on available data and translates it into json format

# Barbarian class Data
def add_barbarian_data(class_data):
    class_data["type"] = "warrior"
    print("Adding class data: Barbarian")
    
    # Class proficiencies
    proficiencies = {
        "Armor": "Light armour, medium armour, shields",
        "Weapons": "Simple weapons, Martial weapons",
        "Tools": "None",
        "Skills (2)": "Animal Handling, Athletics, Intimidation, Nature, Perception, Survival"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies
    
    # class start equipment
    equipment =  {
        "Primary": ["Greataxe", "Any martial weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": [],
        "Bags": ["Explorer's bag & 4 javelins"]
        
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Rage",
        "Unarmored defence"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features
    
	# class health data
    health =  {
        "Hit Die": "1d12",
        "Hit Points": "1d12 + Constitution modifier",
        "Hit Point Scaling": "1d12 (or 7) + Constitution modifier",
        "Saving Throws": "Str/Const"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


# Bard class data
def add_bard_data(class_data):
    print("Adding class data: Bard")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [2, 4, 2]

    # Class cantrips
    cantrips = [
        "Blade Ward",
        "Dancing Lights",
        "Friends",
        "Light",
        "Mage Hand",
        "Mending",
        "Message",
        "Minor Illusion",
        "Prestidigitation",
        "Thunderclap",
        "True Strike",
        "Vicious Mockery"
    ]
    print("{} {}".format(len(cantrips), "cantrip entries added"))
    class_data["cantrips"] = cantrips

    # Class spells
    spells = [
        "Animal Friendship",
        "Bane",
        "Charm Person",
        "Comprehend Languages",
        "Cure Wounds",
        "Detect Magic",
        "Disguise Self",
        "Dissonant Whispers",
        "Distort Value",
        "Earth Tremor",
        "Faerie Fire",
        "Feather Fall",
        "Healing word",
        "Heroism",
        "Hideous Laughter",
        "Identify",
        "Illusory Script",
        "Longstrider",
        "Silent Image",
        "Sleep",
        "Speak with Animals",
        "Tasha's hideous Laughter",
        "Thunderwave",
        "Unseen Servant",
    ]
    print("{} {}".format(len(spells), "spell entries added"))
    class_data["spells"] = spells

    # class proficiencies
    proficiencies = {
        "Armor": "Light Armour",
        "Weapons": "Simple weapons, hand crossbows, longswords, rapiers, shortswords",
        "Tools": "3 Musical instruments of your choice",
        "Skills": "Pick 3"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # class start equipment
    equipment = {
        "Primary": ["Rapier", "longsword", "Simple weapon"],
        "Secondary": ["Leather armor & dagger"],
        "Tertiary": ["Lute", "Other instrument"],
        "Bags": ["Diplomat's pack", "Entertainer's pack"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Spellcasting",
        "Bardic Inspiration"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Dex/Cha"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Cleric class Data
def add_cleric_data(class_data):
    print("Adding class data: cleric")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [3, 0, 2]

    # Class start equipment
    cantrips = [
        "Guidance",
        "Light",
        "Mending",
        "Sacred Flame",
        "Spare the Dying",
        "Thaumaturgy",
        "Frostbite",
        "Toll the Dead",
        "Word of Radiance",
    ]
    print("{} {}".format(len(cantrips), "cantrips added"))
    class_data["cantrips"] = cantrips

    spells = [
        "Bane",
        "Bless",
        "Ceremony",
        "Command",
        "Create/Destroy Water",
        "Cure Wounds",
        "Detect Evil & Good",
        "Detect Magic",
        "Detect Poison & Disease",
        "Guiding Bold",
        "Healing Word",
        "Inflict Wounds",
        "Protection from Evil and Good",
        "Purify Food & Drink",
        "Sanctuary",
        "Shield of Faith",
    ]
    print("{} {}".format(len(spells), "spells added"))
    class_data["spells"] = spells

    # Class start equipment
    proficiencies = {
        "Armor": "Light armor, medium armor, shields",
        "Weapons": "Simple weapons",
        "Tools": "None",
        "Skills (2)": "History, Insight, Medicine, Persuasion, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Mace", "Warhammer"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Shield & holy symbol"],
        "Bags": ["Priest's bag", "Explorer's bag"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Spellcasting",
        "Divine Domain"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Druid class Data
def add_druid_data(class_data):
    print("Adding class data: Druid")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [2, 0, 2]

    cantrips = [
        "Control Flames",
        "Create Bonfire",
        "Druidcraft",
        "Frostbite",
        "Guidance",
        "Infestation",
        "Gust",
        "Lightning Lure",
        "Magic Stone",
        "Mending",
        "Mold Earth",
        "Poison Spray",
        "Primal Savagery",
        "Produce Flame",
        "Resistance",
        "Shape Water",
        "Shillelagh",
        "Thorn Whip",
        "Thunderclap",
        "Toll the Dead",
        "True Strike",
    ]
    print("{} {}".format(len(cantrips), "cantrips added"))
    class_data["cantrips"] = cantrips

    spells = [
        "Absorb Elements",
        "Animal Friendship",
        "Beast Bond",
        "Charm Person",
        "Create/Destroy Water",
        "Cure Wounds",
        "Detect Magic",
        "Detect Poison & Disease",
        "Earth Tremor",
        "Entangle",
        "Faerie Fire",
        "Fog Cloud",
        "Goodberry",
        "Healing Word",
        "Ice Knife",
        "Jump",
        "Purify Food & Drink",
        "Snare",
        "Speak with Animals",
        "Thunderwave"
    ]
    print("{} {}".format(len(spells), "spells added"))
    class_data["spells"] = spells

    proficiencies = {
        "Armor": "Light Armour, Medium Armour, Shields (Cannot wear metal)",
        "Weapons": "Clubs, Daggers, Darts, Javelins, Maces, Quarterstaves, Scimitars, Sickles, Slings, Spears",
        "Tools": "Herbalism kit",
        "Skills (2)": "Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # class start equipment
    equipment = {
        "Primary": ["Wooden Shield", "Any simple weapon"],
        "Secondary": ["Scimitar", "Simple melee weapon"],
        "Tertiary": ["Leather Armour & Druidic Focus"],
        "Bags": ["Explorer's pack"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Druidic",
        "Spellcasting"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Wizard class data
def add_wizard_data(class_data):
    print("Adding class data: Wizard")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [3, 6, 2]
    
    # Class cantrips
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
    class_data["cantrips"] = cantrips
    
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
    class_data["spells"] = spells
    
    # class proficiencies
    proficiencies = {
        "Armor": "None",
        "Weapons": "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows",
        "Tools": "None",
        "Skills (2)": "Arcane, History, Investigation, Medicine, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies
    
    # class start equipment
    equipment =  {
        "Primary": ["Quarterstaff", "Dagger"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Spellbook"],
        "Bags": ["Scholar's bag", "Explorer's bag"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Spellcasting",
        "Arcane Recovery"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health =  {
        "Hit Die": "1d6",
        "Hit Points": "1d6 + Constitution modifier",
        "Hit Point Scaling": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


# Warlock class Data
def add_warlock_data(class_data):
    print("Adding class data: Warlock")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [2, 2, 1]
    
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
    class_data["cantrips"] = cantrips
    
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
    class_data["spells"] = spells
    
    proficiencies = {
        "Armor": "Light armor",
        "Weapons": "Simple weapons and light crossbows",
        "Tools": "None",
        "Skills (2)": "Archana, Deception, History, Intimidation, Investigation, Nature, Religion"
    }
    print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # class start equipment
    equipment = {
        "Primary": ["light crossbow & 20 bolts", "a Simple weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Leather armor", "Simple weapon", "2 Daggers"],
        "Bags": ["Scholar's bag", "Dungeoneer's bag"]
    }
    print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Otherworldly Patron",
        "Pact magic"
    ]
    print("{} {}".format(len(features), "features added"))
    class_data["features"] = features
    
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


# TODO: details to cantrips, skills and spells
data = {}
data["barbarian"] = {}
data["bard"] = {}
data["cleric"] = {}
data["druid"] = {}
#data["fighter"] = {}
#data["monk"] = {}
#data["paladin"] = {}
#data["ranger"] = {}
#data["rogue"] = {}
#data["sorcerer"] = {}
data["wizard"] = {}
data["warlock"] = {}

data["barbarian"] = add_barbarian_data(data["barbarian"])
data["bard"] = add_bard_data(data["bard"])
data["cleric"] = add_cleric_data(data["cleric"])
data["druid"] = add_druid_data(data["druid"])
#data["fighter"] = add_fighter_data(data["fighter"])
#data["monk"] = add_monk_data(data["monk"])
#data["paladin"] = add_paladin_data(data["paladin"])
#data["ranger"] = add_ranger_data(data["ranger"])
#data["rogue"] = add_rogue_data(data["rogue"])
#data["sorcerer"] = add_sorcerer_data(data["sorcerer"])
data["wizard"] = add_wizard_data(data["wizard"])
data["warlock"] = add_warlock_data(data["warlock"])
print(data)

with open('class_data.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)