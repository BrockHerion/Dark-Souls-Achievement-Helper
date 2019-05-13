import requests
import re
import pandas
from bs4 import BeautifulSoup

def main():
    page = requests.get("https://darksouls.wiki.fextralife.com/Wisdom+of+a+Sage+Achievement+Guide")
    soup = BeautifulSoup(page.content, 'html.parser')

    guide = soup.find(id="wiki-content-block")
    spell_data = guide.find_all('li')

    spell_names = []
    spell_locations = []

    for item in spell_data:
        spell_names.append(get_item_name(item))
        spell_locations.append(get_item_location(item))

    spells = pandas.DataFrame({
        "name":spell_names,
        "location":spell_locations
    })

    print(spells.sort_values(by=['name']))

def get_item_name(item):
    return item.find(class_="wiki_link").get_text()

def get_item_location(item):
    for child in item.find_all('a'):
        child.decompose()

    item_location = item.get_text()
    item_location = re.sub(r'\s-\s', '', item_location)
    return item_location


if __name__ == "__main__":
    main()
