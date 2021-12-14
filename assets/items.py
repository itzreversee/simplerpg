class manaBag():
    type = 0
    inGameName = 'Mana Bag'
    hardid = 'manaBag'
    description = "Leather Mana Bag! ( don't ask how it got in here ) "
    cost = 50
    
    value1 = 25 # + max mana 
    value2 = 5 # + mana regen

    rarity = 'common'
    level = 1
class healthNecklace():
    type = 1
    inGameName = 'Health Necklace'
    hardid = 'healthNecklace'
    description = "Heart-Shaped Necklace that gives you health!"
    cost = 150
    
    value1 = 25 # + max hp  | * level 
    value2 = 1 # + hp regen | * level

    rarity = 'rare'
    level = 2

def getItemInfo(item):
    if item.type == 0 or item.type == 1:
        return [item.type, item.description, item.rarity, item.level, item.value1, item.value2,]