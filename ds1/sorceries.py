import pandas
import re
import requests
from bs4 import BeautifulSoup
from data import Data

class Sorceries(Data):
    def __init__(self, page_url):
        self.page_url = page_url

    def get_sorceries(self):
        page = requests.get(self.page_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        guide = soup.find(id="wiki-content-block")
        spell_data = guide.find_all('li')

        spell_names = []
        spell_locations = []

        for item in spell_data:
            spell_names.append(self.get_item_name(item))
            spell_locations.append(self.get_item_location(item))

        spells = pandas.DataFrame({
            "name":spell_names,
            "location":spell_locations
        })

        return spells

    def get_item_name(self, item):
        return item.find(class_="wiki_link").get_text()

    def get_item_location(self, item):
        for child in item.find_all('a'):
            child.decompose()

        item_location = item.get_text()
        item_location = re.sub(r'\s-\s', '', item_location)
        return item_location