from ds1.sorceries import Sorceries

def main():
    spells = Sorceries("https://darksouls.wiki.fextralife.com/Wisdom+of+a+Sage+Achievement+Guide")
    print(spells.get_sorceries())

if __name__ == "__main__":
    main()
