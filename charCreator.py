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
    
def defineModifier(value):
    return int(value/2-5) 
    
    
def getRandomAttr(attr):
    print("\nAttributes:")
    for key, value in attr.items():
        value = generateStat()
        modifier = defineModifier(value)
        print(' {}: {}, Modifier: {:+d}'.format( key, value , modifier))
    return attr    


'''
Picks spells, cantrips, proficiencies and health stats for wizard class from external data files
'''
def getWizard(wizard):
    cantrips = wizard["cantrips"] 
    print("\nCantrips:")
    for i in range(0, 3):
        randomNum = random.randint(0, len(cantrips)-1)
        print(" {}: {}".format(i+1, cantrips[randomNum]))
        cantrips.pop(randomNum)
    
    spells = wizard["spells"]
    print("\nSpells:")
    for i in range(0, 6):
        randomNum = random.randint(0, len(spells)-1)
        print(" {}: {}".format(i+1, spells[randomNum]))
        spells.pop(randomNum)
        
    proficiencies = wizard["proficiencies"]
    print("\nProficiencies:")
    for key, value in proficiencies.items():
        print(" {}: {}".format(key, value))
        
    health = wizard["health"]
    print("\nHealth:")
    for key, value in health.items():
        print(" {}: {}".format(key, value))
    
    
# chardata = {'stats':[], 'class':"" ,'skills':[],'items':[]}
charData = {}
charData["attributes"] = {
    "Strength": 0,
    "Dexterity": 0, 
    "Constitution": 0,
    "Intelligence": 0,
    "Wisdom": 0,
    "Charisma": 0
    }

# Generating, modifying and printing random attributes
charData['attributes'] = getRandomAttr(charData['attributes'])

classData = {}
with open('./classData.json') as file:
  classData = json.load(file)
  
classData["wizard"] = getWizard(classData["wizard"])



