
import json
# Welcome message and initial instructions
print("Welcome to Monster Data Cleaner!")
print("This program will clean the JSON file with monster data.")
print("Please upload your file to")
print(r"C:\Users\dawn\Class Coding Projects\Python Project 2")

# Get file name from user
while True:
    monsterFile = input("Enter your file name: ")
    print("Loading file...")
    # Open, load, and Close JSON file
    try:
        monsterData = open(monsterFile, 'r')
        monsterList = json.load(monsterData)
        monsterData.close()
    except FileNotFoundError:
        print("Error loading file")
        continue

    if len(monsterList) > 0:
        print("Monster file loaded successfully.")
        break
    else:
        print("This file does not contain data")

# Data Mapping
# 0 = Name
# 1 = Size
# 2 = HP
# 3 = Location
# 4 = Magic User

# Monster data cleaning functions 
cleaned_monsters = []

# Cleaning Creature Name
def clean_creature_name(creature_name):
    creature_name = creature_name.strip()
    creature_name = creature_name.title()
    if creature_name == "":
        creature_name = "Name not given"
    return creature_name

# Cleaning Creature Size
def clean_creature_size(creature_size):
    creature_size = creature_size.strip()
    creature_size = creature_size.title()
    if creature_size == "":
        creature_size = "Unknown"
    return creature_size

#Cleaning Creature HP
def clean_creature_HP(creature_HP):
    creature_HP = creature_HP.strip()
    creature_HP = int(creature_HP)
    if creature_HP == "":
        creature_HP = 0
    return creature_HP

#Cleaning Creature Location
def clean_creature_location(creature_location):
    creature_location = creature_location.strip()
    creature_location = creature_location.title()
    if creature_location == "":
        creature_location = "Unknown"
    return creature_location

# Cleaning Creature Magic Status
def clean_creature_magic_status(creature_magic_status):
    creature_magic_status = creature_magic_status.strip()
    creature_magic_status = creature_magic_status.lower()
    if creature_magic_status == "y" or creature_magic_status == "yes":
        creature_magic_status = True
    elif creature_magic_status == "n" or creature_magic_status == "no":
        creature_magic_status = False
    else:
        creature_magic_status = "Unknown"
    return creature_magic_status

# Call Cleaning Functions
def clean_all_creatures():
    for creature in monsterList:
        cleaned_name = clean_creature_name(creature[0])
        cleaned_size = clean_creature_size(creature[1])
        cleaned_HP = clean_creature_HP(creature[2])
        cleaned_location = clean_creature_location(creature[3])
        cleaned_magic_status = clean_creature_magic_status(creature[4])
        cleaned_creature = [cleaned_name, 
                            cleaned_size, 
                            cleaned_HP, 
                            cleaned_location, 
                            cleaned_magic_status]
        cleaned_monsters.append(cleaned_creature)
    return cleaned_monsters

cleaned_monsters = clean_all_creatures()

# Create Cleaned Monsters File
cleaned_monsters_file = open("cleaned_monster_file.json", 'w')
json.dump(cleaned_monsters, cleaned_monsters_file)
cleaned_monsters_file.close()

print("Cleaned monster data saved successfully.")
print("cleaned_monsters.json")
print("*** Cleaned Monster Records***")
print("Name              Size              HP         Location          Magic User")
print("===========================================================================")
for creature in cleaned_monsters:
    print(f"{creature[0]:<15} | {creature[1]:<15} | {creature[2]:>8} | {creature[3]:<15} | {creature[4]:<15}")
