
import sys

class FireSpell(): 
    hardid = "FireSpell"
    id = 2

    name = "Fire Spell"
    cost = 20

    type = "damage"
    value = 8
    duration = 1 # rounds, 1 = only this

class IceSpell(): 
    hardid = "IceSpell"
    id = 3

    name = "Ice Spell"
    cost = 20

    type = "damage"
    value = 8
    duration = 1

class AirSpell(): 
    hardid = "AirSpell"
    id = 4

    name = "Air Spell"
    cost = 15

    type = "damage"
    value = 6
    duration = 1

class HealSpell(): 
    hardid = "HealSpell"
    id = 5

    name = "Heal Spell"
    cost = 25

    type = "heal"
    value = 10
    duration = 1

class CurseSpell(): 
    hardid = "CurseSpell"
    id = 6

    name = "Curse Spell"
    cost = 75

    type = "curse"
    value = 8
    duration = 3 # rounds, 2 = this and next
