import json
import os
# Simply defines class features based on available data and translates it into json format


# Barbarian class Data
def add_barbarian_data(class_data):
    class_data["type"] = "warrior"
    if debug:
        print("Adding class data: Barbarian")
    
    # Class proficiencies
    proficiencies = {
        "Armor": "Light armour, medium armour, shields",
        "Weapons": "Simple weapons, Martial weapons",
        "Tools": "None",
        "Skills (2)": "Animal Handling, Athletics, Intimidation, Nature, Perception, Survival"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies
    
    # Class start equipment
    equipment = {
        "Primary": ["Greataxe", "Any martial weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["None"],
        "Bags": ["Explorer's bag & 4 javelins"]
        
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Rage",
        "Unarmored defence"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features
    
    # Class health data
    health = {
        "Hit Die": "1d12",
        "Hit Points": "1d12 + Constitution modifier",
        "Hit Point Scaling": "1d12 (or 7) + Constitution modifier",
        "Saving Throws": "Str/Const"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


# Bard class data
def add_bard_data(class_data):
    if debug:
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
    if debug:
        print("{} {}".format(len(cantrips), "cantrip entries added"))
    class_data["cantrips"] = cantrips

    # Class 1st level spells
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
        "Thunderwave",
        "Unseen Servant",
    ]
    if debug:
        print("{} {}".format(len(spells), "spell entries added"))
    class_data["spells"] = spells

    # class proficiencies
    proficiencies = {
        "Armor": "Light Armour",
        "Weapons": "Simple weapons, hand crossbows, longswords, rapiers, shortswords",
        "Tools": "3 Musical instruments of your choice",
        "Skills": "Select 3 minor skills"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # class start equipment
    equipment = {
        "Primary": ["Rapier", "longsword", "Simple weapon"],
        "Secondary": ["Leather armor & dagger"],
        "Tertiary": ["Lute", "Other instrument"],
        "Bags": ["Diplomat's pack", "Entertainer's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Spellcasting",
        "Bardic Inspiration"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Dex/Cha"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Cleric class Data
def add_cleric_data(class_data):
    if debug:
        print("Adding class data: cleric")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [3, 0, 2]

    # Class cantrips
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
    if debug:
        print("{} {}".format(len(cantrips), "cantrips added"))
    class_data["cantrips"] = cantrips

    # Class 1st level spells
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
    if debug:
        print("{} {}".format(len(spells), "spells added"))
    class_data["spells"] = spells

    # Class start equipment
    proficiencies = {
        "Armor": "Light armour, medium armour, shields",
        "Weapons": "Simple weapons",
        "Tools": "None",
        "Skills (2)": "History, Insight, Medicine, Persuasion, Religion"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Mace", "Warhammer"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Shield & holy symbol"],
        "Bags": ["Priest's bag", "Explorer's bag"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Spellcasting",
        "Divine Domain"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Druid class Data
def add_druid_data(class_data):
    if debug:
        print("Adding class data: Druid")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [2, 0, 2]

    # Class cantrips
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
    if debug:
        print("{} {}".format(len(cantrips), "cantrips added"))
    class_data["cantrips"] = cantrips

    # Class 1st level spells
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
    if debug:
        print("{} {}".format(len(spells), "spells added"))
    class_data["spells"] = spells

    # Class proficiencies
    proficiencies = {
        "Armor": "Light Armour, Medium Armour, Shields (Cannot wear metal)",
        "Weapons": "Clubs, Daggers, Darts, Javelins, Maces, Quarterstaves, Scimitars, Sickles, Slings, Spears",
        "Tools": "Herbalism kit",
        "Skills (2)": "Arcana, Animal Handling, Insight, Medicine, Nature, Perception, Religion, Survival"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Wooden Shield", "Any simple weapon"],
        "Secondary": ["Scimitar", "Simple melee weapon"],
        "Tertiary": ["Leather Armour & Druidic Focus"],
        "Bags": ["Explorer's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Druidic",
        "Spellcasting"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Fighter class Data
def add_fighter_data(class_data):
    class_data["type"] = "warrior"
    if debug:
        print("Adding class data: Fighter")

    # Class proficiencies
    proficiencies = {
        "Armour": "All armour, shields",
        "Weapons": "Simple weapons, Martial weapons",
        "Tools": "None",
        "Skills (2)": "Acrobatics, Animal Handling, Athletics, History, Insight, Intimidation, Perception, Survival"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Chain mail", "Any martial weapon"],
        "Secondary": ["Martial Weapon & shield", "2 Martial Weapons"],
        "Tertiary": ["Light crossbow & 20 bolts", "2 Handaxes"],
        "Bags": ["Explorer's pack", "Dungeoneer's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Fighting Style",
        "Second Wind"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d10",
        "Hit Points": "1d10 + Constitution modifier",
        "Hit Point Scaling": "1d10 (or 6) + Constitution modifier",
        "Saving Throws": "Str/Const"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Monk class Data
def add_monk_data(class_data):
    class_data["type"] = "warrior"
    if debug:
        print("Adding class data: Monk")

    # Class proficiencies
    proficiencies = {
        "Armour": "None",
        "Weapons": "Simple weapons, Shortswords",
        "Tools": "Choose one type of artisan's tools or one musical instrument",
        "Skills (2)": "Acrobatics, Athletics, History, Insight, Religion, Stealth"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Shortsword", "Any Simple Weapon"],
        "Secondary": ["10 Darts"],
        "Tertiary": ["None"],
        "Bags": ["Explorer's pack", "Dungeoneer's pack"]

    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Unarmoured Defense",
        "Martial Arts"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Str/Dex"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Cleric class Data
def add_paladin_data(class_data):
    if debug:
        print("Adding class data: Paladin")
    class_data["type"] = "warrior"

    # Class start equipment
    proficiencies = {
        "Armor": "All armour, Shields",
        "Weapons": "Simple weapons, Martial Weapons",
        "Tools": "None",
        "Skills (2)": "Athletics, Insight, Intimidation, Medicine, Persuasion, Religion"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Martial Weapon & Shield", "Two Martial Weapons"],
        "Secondary": ["5 javelins", "Simple Melee Weapon"],
        "Tertiary": ["Chain Mail & holy symbol"],
        "Bags": ["Priest's pack", "Explorer's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Divine Sense",
        "Lay on Hands"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d10",
        "Hit Points": "1d10 + Constitution modifier",
        "Hit Point Scaling": "1d10 (or 6) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Ranger class Data
def add_ranger_data(class_data):
    class_data["type"] = "warrior"
    if debug:
        print("Adding class data: Ranger")

    # Class proficiencies
    proficiencies = {
        "Armour": "Light Armour, Medium Armour, Shields",
        "Weapons": "Simple weapons, Martial Weapons",
        "Tools": "None",
        "Skills (3)": "Animal Handling, Athletics, Insight, Investigation, Nature, Perception, Stealth, Survival"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Scale mail", "Leather Armour"],
        "Secondary": ["Two Shortswords", "Two Simple Melee Weapons"],
        "Tertiary": ["Longbow & quiver with 20 arrows"],
        "Bags": ["Explorer's pack", "Dungeoneer's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Favored Enemy",
        "Natural Explorer"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d10",
        "Hit Points": "1d10 + Constitution modifier",
        "Hit Point Scaling": "1d10 (or 6) + Constitution modifier",
        "Saving Throws": "Str/Dex"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Rogue class Data
def add_rogue_data(class_data):
    class_data["type"] = "warrior"
    if debug:
        print("Adding class data: Ranger")

    # Class proficiencies
    proficiencies = {
        "Armour": "Light Armour",
        "Weapons": "Simple weapons, Hand crossbows, Longswords, Rapiers, Shortswords",
        "Tools": "Thieve's tools",
        "Skills (4)": "Acrobatics, Athletics, Deception, Insight, Intimidation, Investigation,\n"
                      " Perception, Performance, Persuasion, Sleight of Hand, and Stealth"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Rapier", "Shortsword"],
        "Secondary": ["Shortbow & quiver with 20 arrows", "Shortsword"],
        "Tertiary": ["Leather Armour, Two Daggers & thieves' tools"],
        "Bags": ["Explorer's pack", "Dungeoneer's pack", "Burglar's pack"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Expertize",
        "Sneak Attack",
        "Thieves' Cant"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d10 (or 5) + Constitution modifier",
        "Saving Throws": "Dex/Int"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Sorcerer class data
def add_sorcerer_data(class_data):
    if debug:
        print("Adding class data: Wizard")
    class_data["type"] = "spellcaster"
    class_data["spell_details"] = [4, 2, 2]

    # Class cantrips
    cantrips = [
        "Acid Splash",
        "Blade Ward",
        "Booming Blade",
        "Chill Touch",
        "Control Flames",
        "Create Bonfire",
        "Dancing Lights",
        "Fire Bolt",
        "Friends",
        "Frostbite",
        "Green-flame Blade",
        "Gust",
        "Infestation",
        "Light",
        "Lightning Lure",
        "Mage Hand",
        "Mending",
        "Message",
        "Mind Sliver",
        "Minor Illusion",
        "Mold Earth",
        "Poison Spray",
        "Prestidigitation",
        "Ray of Frost",
        "Shape Water",
        "Shoking Grasp",
        "Sword Burst",
        "Thunderclap",
        "True Strike",
    ]
    if debug:
        print("{} {}".format(len(cantrips), "cantrip entries added"))
    class_data["cantrips"] = cantrips

    # Class 1st level spells
    spells = [
        "Absorb Elements",
        "Burning Hands",
        "Charm Person",
        "Catapult",
        "Chaos Bolt",
        "Charm Person",
        "Chromatic Orb"
        "Color Spray",
        "Comprehend Languages",
        "Detect Magic",
        "Disguise Self",
        "Distort Value",
        "Earth Tremor",
        "Expeditious Retreat",
        "False Life",
        "Feather Fall",
        "Fog Cloud",
        "Ice Knife",
        "Jump",
        "Mage Armour",
        "Magic Missile",
        "Ray of Sickness",
        "Shield",
        "Silent Image",
        "Sleep",
        "Thunderwave",
        "Witch Bolt",
    ]
    if debug:
        print("{} {}".format(len(spells), "spell entries added"))
    class_data["spells"] = spells

    # Class proficiencies
    proficiencies = {
        "Armour": "None",
        "Weapons": "Daggers, Darts, Slings, Quarterstaves, Light Crossbows",
        "Tools": "None",
        "Skills (2)": "Arcane, Deception, Insight, Intimidation, Persuasion, Religion"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # Class start equipment
    equipment = {
        "Primary": ["Light Crossbow & 20 bolts", "Simple Weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Two Daggers"],
        "Bags": ["Dungeoneer's bag", "Explorer's bag"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Spellcasting",
        "Sorcerous Origin"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d6",
        "Hit Points": "1d6 + Constitution modifier",
        "Hit Point Scaling": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Const/Cha"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health

    return class_data


# Wizard class data
def add_wizard_data(class_data):
    if debug:
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
    if debug:
        print("{} {}".format(len(cantrips), "cantrip entries added"))
    class_data["cantrips"] = cantrips
    
    # Class 1st level spells
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
        "Mage armour",
        "Magic Missile",
        "Protection from Evil and Good",
        "Shield",
        "Silent Image",
        "Sleep",
        "Thunderwave",
        "Unseen Servant",
    ]
    if debug:
        print("{} {}".format(len(spells), "spell entries added"))
    class_data["spells"] = spells
    
    # Class proficiencies
    proficiencies = {
        "Armour": "None",
        "Weapons": "Daggers, Darts, Slings, Quarterstaffs, Light Crossbows",
        "Tools": "None",
        "Skills (2)": "Arcane, History, Investigation, Medicine, Religion"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies
    
    # Class start equipment
    equipment = {
        "Primary": ["Quarterstaff", "Dagger"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Spellbook"],
        "Bags": ["Scholar's bag", "Explorer's bag"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class Features
    features = [
        "Spellcasting",
        "Arcane Recovery"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features

    # Class health data
    health = {
        "Hit Die": "1d6",
        "Hit Points": "1d6 + Constitution modifier",
        "Hit Point Scaling": "1d6 (or 4) + Constitution modifier",
        "Saving Throws": "Int/Wis"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


# Warlock class Data
def add_warlock_data(class_data):
    if debug:
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
    if debug:
        print("{} {}".format(len(cantrips), "cantrips added"))
    class_data["cantrips"] = cantrips
    
    spells = [
        "Armor of Agathys",
        "Arms of Hadar",
        "Charm Person",
        "Cause Fear",
        "Color Spray",
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
    if debug:
        print("{} {}".format(len(spells), "spells added"))
    class_data["spells"] = spells
    
    proficiencies = {
        "Armour": "Light armour",
        "Weapons": "Simple weapons and light crossbows",
        "Tools": "None",
        "Skills (2)": "Arcana, Deception, History, Intimidation, Investigation, Nature, Religion"
    }
    if debug:
        print("{} {}".format(len(proficiencies), "proficiency entries added"))
    class_data["proficiencies"] = proficiencies

    # class start equipment
    equipment = {
        "Primary": ["light crossbow & 20 bolts", "a Simple weapon"],
        "Secondary": ["Component Pouch", "Arcane Focus"],
        "Tertiary": ["Leather armor", "Simple weapon", "2 Daggers"],
        "Bags": ["Scholar's bag", "Dungeoneer's bag"]
    }
    if debug:
        print("{} {}".format(len(equipment), "equipment entries added"))
    class_data["equipment"] = equipment

    # Class features
    features = [
        "Otherworldly Patron",
        "Pact magic"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    class_data["features"] = features
    
    health = {
        "Hit Die": "1d8",
        "Hit Points": "1d8 + Constitution modifier",
        "Hit Point Scaling": "1d8 (or 5) + Constitution modifier",
        "Saving Throws": "Wis/Cha"
    }
    if debug:
        print("{} {}".format(len(health), "health entries added"))
    class_data["health"] = health
    
    return class_data


debug = False
data = {
        "barbarian": {},
        "bard": {},
        "cleric": {},
        "druid": {},
        "fighter": {},
        "monk": {},
        "paladin": {},
        "ranger": {},
        "rogue": {},
        "sorcerer": {},
        "wizard": {},
        "warlock": {}
        }
data["barbarian"] = add_barbarian_data(data["barbarian"])
data["bard"] = add_bard_data(data["bard"])
data["cleric"] = add_cleric_data(data["cleric"])
data["druid"] = add_druid_data(data["druid"])
data["fighter"] = add_fighter_data(data["fighter"])
data["monk"] = add_monk_data(data["monk"])
data["paladin"] = add_paladin_data(data["paladin"])
data["ranger"] = add_ranger_data(data["ranger"])
data["rogue"] = add_rogue_data(data["rogue"])
data["sorcerer"] = add_sorcerer_data(data["sorcerer"])
data["wizard"] = add_wizard_data(data["wizard"])
data["warlock"] = add_warlock_data(data["warlock"])
print("Class data generated.")
if debug:
    print(data)

path = "../data/class_data.json"
try:
    os.mkdir('../data/')
except FileExistsError:
    print("")
finally:
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
