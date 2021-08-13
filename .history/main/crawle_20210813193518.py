import os
import sys
import pandas as pd
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import fire
from engine.google import *

def crawle(keyword: str, lat: float, lng: float, page_limit: int=5):
    google = GoogleCrawler()
    items = google.crawle(q=keyword, latitude=lat, longitude=lng, max_page_num=page_limit)
    df = pd.DataFrame()
    for item in items:
        df = df.append(item.__dict__, ignore_index=True)
    now = datetime.datetime.now().strftime("%")
    df.to_excel("export_{}_{}_{}.xlsx")


if __name__ == "__main__":
    fire.Fire(crawle)