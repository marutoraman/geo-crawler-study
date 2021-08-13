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
        pass