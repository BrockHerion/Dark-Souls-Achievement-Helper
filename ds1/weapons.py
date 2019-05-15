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
        weapon_location = []

        for i in range(3, len(weapon_data) ):
            if i % 2 is 0:
                pass
            else:
                print(weapon_data[i].find('a').get_text())

        return weapon_data

    def get_item_name(self, item):
        pass

    def get_item_location(self, item):
        pass