import pandas
import re
import requests
from bs4 import BeautifulSoup
from data import Data


class Weapons(Data):
    def __init__(self, page_url):
        self.page_url = page_url

    def get_weapons(self):
        page = requests.get(self.page_url)
        soup = BeautifulSoup(page.content, 'html.parser')

        guide = soup.find(id="wiki-content-block")
        weapon_data = guide.find_all('p')

        weapon_names = []
        weapon_locations = []

        for i in range(3, len(weapon_data)):
            if i % 2 is 0:
                weapon_locations.append(weapon_data[i].get_text())
            elif weapon_data[i].a is not None:
                weapon_names.append(self.get_item_name(weapon_data[i]))

        print(len(weapon_names))
        print(len(weapon_locations))

        for item in weapon_locations:
            print(item)

        #weapons = pandas.DataFrame({
        #    "name":weapon_names,
        #    "location":weapon_locations
        #})

        #return weapons

    def get_item_name(self, item):
        return item.find('a').get_text()

    def get_item_location(self, item):
        pass
