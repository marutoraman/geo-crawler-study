from common.driver import *
from bs4 import BeautifulSoup as bs
from models.item import *

from common.logger import set_logger
logger = set_logger(__name__)

GOOGLE_URL = "https://google.co.jp"
SEARCH_URL = "https://www.google.com/search?q={q}&rlz=1C1QABZ_jaJP923JP923&oq=test&aqs=chrome..69i57j69i59l2j69i60l3j69i65l2.2813j0j4&sourceid=chrome&ie=UTF-8"


class GoogleCrawler():
    
    @staticmethod
    def crawle(q:str, latitude:float, longitude:float, max_page_num=10):
        # Driverを起動して緯度経度をセット
        driver = Driver()
        driver.set_geo_location(GOOGLE_URL, latitude, longitude)
        # 検索結果を表示
        url = SEARCH_URL.format(q=q)
        items = []
        rank = 1
        for page in range(max_page_num):
            driver.driver.get(url)
            # 結果を解析
            soup = bs(driver.driver.page_source, "html.parser")
            item_elms = soup.select(".yuRUbf")
            for item_elm in item_elms:
                url = item_elm.select_one("a").get("href")
                items.append(
                    Item(
                        title=item_elm.select_one("h3").text, 
                        url=item_elm.select_one("a").get("href"),
                        rank=rank,
                        keyword=q,
                        latitude=longitude,
                        longitude=longitude
                    )
                )
                logger.info(f"rank: {rank} | {item_elm.select_one('h3').text}")
                rank += 1
            next_page_url = soup.select_one("#pnnext").get("href") if soup.select_one("#pnnext") != None else None
            if next_page_url == None:
                logger.info(f"最終ページです。 page:{page+1}")
                break
            url = f"{GOOGLE_URL}{next_page_url}"
            logger.info(f"crawled page:{page+1}")
    
        return items