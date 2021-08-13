import os
import sys
import pandas as pd
import datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import fire
from engine.google import *

def crawle(keyword: str, lat: float, lng: float, page_limit: int=5):
    pass


if __name__ == "__main__":
    fire.Fire(crawle)