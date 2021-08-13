from datetime import datetime as dt
from common.utility import *


def test_download_img():
    down_load_img(
        "https://images-na.ssl-images-amazon.com/images/I/61NkwFSq3KL._AC_SX425_.jpg", "./")


def test_delta_day():
    target = dt(2021, 5, 1)
    res = calc_day_delta(target, dt.now())
    print(res)

    assert res
