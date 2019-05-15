from ds1.sorceries import Sorceries
from ds1.weapons import Weapons

def main():
    #spells = Sorceries("https://darksouls.wiki.fextralife.com/Wisdom+of+a+Sage+Achievement+Guide")
    #print(spells.get_sorceries())
    weapons = Weapons("https://darksouls.wiki.fextralife.com/Knight%27s+Honor+Achievement+Guide")
    weapons.get_weapons()
    #print(weapons.get_weapons())

if __name__ == "__main__":
    main()
