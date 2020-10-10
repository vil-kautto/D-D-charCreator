import random
import json
from collections import defaultdict

'''
Generates stats based on following model: 4d6 - smallestRoll
Generated stats are between 3-18, minor bias on median
'''
def generateStat():
    randomNums = [0, 0, 0, 0]
    for i in range(0, 4):
        randomNums[i] = random.randint(1,6)
    
    # Remove the smallest 
    randomNums.sort();
    #print(randomNums)
    randomNums.pop(0)
    #print(randomNums)
    
    # Getting the sum of a array
    sum = 0
    for i in range(0, 3):
        sum += randomNums[i]
    #print(sum)
    return sum
    

def getWizardSpells(wizard):
    cantrips = wizard["cantrips"] 
    print("\nCantrips:")
    for i in range(0, 3):
        randomNum = random.randint(0, len(cantrips)-1)
        print("{}: {}".format(i+1, cantrips[randomNum]))
        cantrips.pop(randomNum)
    
    spells = wizard["spells"]
    print("\nSpells:")
    for i in range(0, 6):
        randomNum = random.randint(0, len(spells)-1)
        print("{}: {}".format(i+1, spells[randomNum]))
        spells.pop(randomNum)
    
    

def getRandomAttr(attr):
    print("\nAttributes:")
    for key, value in attr.items():
        value = generateStat()
        print( '{}: {}'.format( key, value ) )
    return attr
    
    
# chardata = {'stats':[], 'class':"" ,'skills':[],'items':[]}
charData = {}
charData['attributes'] = {
    'Strength': 0,
    'Dexterity': 0, 
    'Constitution': 0,
    'Intelligence': 0,
    'Wisdom': 0,
    'Charisma': 0
    }

# Generating, modifying and printing random attributes
#attr = charData['attributes']
#charData['attributes'] = getRandomAttr(attr)

classData = {}
with open('./classData.json') as file:
  classData = json.load(file)
classData["wizard"] = getWizardSpells(classData["wizard"])



