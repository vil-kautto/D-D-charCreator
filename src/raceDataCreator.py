import json
import os


def add_dragonborn_data(race_data):
    if debug:
        print("Adding class data: Dragonborn")

    # Features determined by racial traits
    features = [
        "Dragonic Ancestry",
        "Breath Weapon",
        "Damage Resistance"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
                "Strength": 2,
                "Dexterity": 0,
                "Constitution": 0,
                "Intelligence": 0,
                "Wisdom": 0,
                "Charisma": 1
            }

    return race_data


def add_dwarf_data(race_data):
    if debug:
        print("Adding class data: Dwarf")

    # Features determined by racial traits
    features = [
        "Darkvision",
        "Dwarven Resilience",
        "Dwarven Combat Training",
        "Stonecunning"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 2,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }

    return race_data


def add_elf_data(race_data):
    if debug:
        print("Adding class data: Elf")

    # Features determined by racial traits
    features = [
        "Darkvision",
        "Keen Senses",
        "Fey Ancestry",
        "Trance"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
            "Strength": 0,
            "Dexterity": 2,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }

    return race_data


def add_gnome_data(race_data):
    if debug:
        print("Adding class data: Gnome")

    # Features determined by racial traits
    features = [
        "DarkVision",
        "Gnome Cunning"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 2,
        "Wisdom": 0,
        "Charisma": 0
    }

    return race_data


def add_half_elf_data(race_data):
    if debug:
        print("Adding class data: Half-elf")

    # Features determined by racial traits
    features = [
        "Darkvision",
        "Fey Ancestry",
        "Skill Versatility",
        "+1 to 2 other attributes"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 2
    }

    return race_data


def add_halfling_data(race_data):
    if debug:
        print("Adding class data: Halfling")

    # Features determined by racial traits
    features = [
        "Lucky",
        "Brave",
        "Halfling Nimbleness"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
        "Strength": 0,
        "Dexterity": 2,
        "Constitution": 0,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    return race_data

def add_half_orc_data(race_data):
    if debug:
        print("Adding class data: Half-orc")

    # Features determined by racial traits
    features = [
        "Darkvision",
        "Menacing",
        "Relentless Endurance",
        "Savage Attacks"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
        "Strength": 2,
        "Dexterity": 0,
        "Constitution": 1,
        "Intelligence": 0,
        "Wisdom": 0,
        "Charisma": 0
    }

    return race_data


def add_human_data(race_data):
    if debug:
        print("Adding class data: Human")

    # Features determined by racial traits
    features = [
        "Extra Language"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
            "Strength": 1,
            "Dexterity": 1,
            "Constitution": 1,
            "Intelligence": 1,
            "Wisdom": 1,
            "Charisma": 1
        }

    return race_data


def add_tiefling_data(race_data):
    if debug:
        print("Adding class data: Tiefling")

    # Features determined by racial traits
    features = [
        "DarkVision",
        "Hellish Resistance",
        "Infernal Legacy"
    ]
    if debug:
        print("{} {}".format(len(features), "features added"))
    race_data["features"] = features

    # Attribute bonuses determined by racial traits
    race_data["attributes"] = {
        "Strength": 0,
        "Dexterity": 0,
        "Constitution": 0,
        "Intelligence": 1,
        "Wisdom": 0,
        "Charisma": 2
    }

    return race_data


debug = False
data = {
        "dragonborn": {},
        "dwarf": {},
        "elf": {},
        "gnome": {},
        "half-elf": {},
        "halfling": {},
        "half-orc": {},
        "human": {},
        "tiefling": {},
        }
data["dragoborn"] = add_dragonborn_data(data["dragonborn"])
data["dwarf"] = add_dwarf_data(data["dwarf"])
data["elf"] = add_elf_data(data["elf"])
data["gnome"] = add_gnome_data(data["gnome"])
data["half-elf"] = add_half_elf_data(data["half-elf"])
data["halfling"] = add_halfling_data(data["halfling"])
data["half-orc"] = add_half_orc_data(data["half-orc"])
data["human"] = add_human_data(data["human"])
data["tiefling"] = add_tiefling_data(data["tiefling"])
print("Race data generated.")
if debug:
    print(data)

path = "../data/race_data.json"
try:
    os.mkdir('../data/')
except FileExistsError:
    print()
finally:
    with open(path, 'w') as outfile:
        json.dump(data, outfile, indent=4)
