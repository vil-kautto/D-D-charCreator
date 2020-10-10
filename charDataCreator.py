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
    
    return classData


data = {}
data["wizard"] = {}
#data["wizard"] = {}
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


with open('classData.json', 'w') as outfile:
    json.dump(data, outfile)