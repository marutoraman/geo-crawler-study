
class Item():

    def __init__(
        self, title: str, url: str, keyword: str, 
        latitude: float, longitude: float):
        self.title = title
        self.url = url
        self.keyword = keyword 
        self.latitude = latitude
        self.longitude = longitude
        self.rank = rank