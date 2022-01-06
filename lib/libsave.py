from lib.libentity import player, baseEntity
import pickle, random

class smanager():
    def save(savefile, p):
        with open(savefile, 'wb') as s:
            pickle.dump(baseEntity(p.name, p.location, p.hp, p.maxhp, p.basemaxhp, p.basehpregen, p.hpregen, p.mana, p.maxmana, p.manaregen, p.basemana, p.basemanaregen, p.maxitems, p.inventory, p.items, p.gold, p.exp, p.level, p.nextlevel, p.isEnemy, p.curseLeft, p.curseId), s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.location, s, pickle.HIGHEST_PROTOCOL) 
            pickle.dump(p.hp, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.maxhp, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.basemaxhp, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.basehpregen, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.hpregen, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.mana, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.maxmana, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.manaregen, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.basemana, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.basemanaregen, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.maxitems, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.inventory, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.items, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.gold, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.exp, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.level, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.nextlevel, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.isEnemy, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.curseLeft, s, pickle.HIGHEST_PROTOCOL)
            pickle.dump(p.curseId, s, pickle.HIGHEST_PROTOCOL)
    class world():
        seed = 0
        shopstock = []
        def save(seed, shopstock):
            seedfile = open("s0_seed.pkl", "wb")
            sstock = open("s0_sstock.pkl", "wb")
            pickle.dump(seed, seedfile, pickle.HIGHEST_PROTOCOL)
            pickle.dump(shopstock, sstock, pickle.HIGHEST_PROTOCOL)
        def newSave():
            smanager.world.save(random.randint(111111,99999999), [])


    def load(savefile):
        with open(savefile, 'rb') as s:
            #print(pickle.load(s))
            return(pickle.load(s))

