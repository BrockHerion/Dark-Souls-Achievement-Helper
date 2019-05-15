from abc import ABC, abstractmethod

class Data(ABC):
    # Data object is initialized with a url
    def __init__(self, page_url):
        self.page_url = page_url

    @abstractmethod
    def get_item_name(self, item):
        pass

    @abstractmethod
    def get_item_location(self, item):
        pass