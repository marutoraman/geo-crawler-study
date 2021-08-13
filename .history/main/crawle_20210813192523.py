import fire
from engine.google import *

def crawle(keyword: str, lat: float, lng: float, page_limit: int=5):
    google = GoogleCrawler()
    items = google.crawle(q=keyword, latitude=lat, longitude=lng, max_page_num=page_limit)
    print(items[0].__dict__)