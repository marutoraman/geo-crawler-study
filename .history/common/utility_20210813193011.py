# -*- coding: utf-8 -*-
from datetime import datetime as dt
from pytz import timezone
import socket
import ssl
import urllib.error
import urllib.request
from urllib.parse import urlparse
import os
import datetime
import requests
import glob
from bs4 import BeautifulSoup as bs


def now_timestamp(mode="DB"):
    if mode == "DB":
        return dt.now().strftime("%Y-%m-%d %H:%M:%S")
    elif mode == "FILE":
        return dt.now().strftime("%Y-%m-%d-%H-%M-%S")
    else:
        return dt.now().strftime("%Y-%m-%d-%H-%M-%S")


def list_to_bool(l: list):
    bool_list = []
    for item in l:
        bool_list.append(False if item == "0" or item == 0 else True)

    return bool_list


def create_proxy_dict(id, password, host, port, proxy_flg=True):
    if proxy_flg:
        proxy_url = f"http://{id}:{password}@{host}:{port}"
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        return {}


def get_global_ip():
    return socket.gethostbyname(socket.gethostname())


def down_load_img(url, path):
    ''' URLを指定し、画像を指定のフォルダに配置する '''
    # ファイル名の作成
    # values = url.split('/')
    # filename = values[-1]
    # filename = filename.split('.')[0]
    # # ファイルパスの指定
    # if os.name == 'posix':
    #     path = '{}/{}.jpg'.format(path, filename)
    # elif os.name == 'nt':
    #     path = '{}\\{}.jpg'.format(path, filename)

    # 画像URLからダウンロード
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        with urllib.request.urlopen(url) as web_file:
            data = web_file.read()
            with open(path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)


def get_date_delta(delta):
    now = datetime.datetime.now()
    return now+datetime.timedelta(days=int(delta))


def padding_zero(text, num):
    return ("0"+text)[-num:]


def get_global_ip():
    url = 'http://www.trackip.net/ip'
    res = requests.get(url)
    if res.status_code >= 300:
        return "Not Found"
    return res.text


def delete_backfile(dir, limit_count=10):
    # 過去ログは削除
    files = sorted(glob.glob(f'{dir}/*'),
                   key=lambda f: os.stat(f).st_mtime, reverse=False)
    for i, file in enumerate(files):
        os.remove(file)
        if i > len(files) - limit_count:
            break


def calc_day_delta(source_dt: dt, target_dt: dt = dt.now()):
    delta_dt = source_dt - target_dt
    return delta_dt.days

def print_query(query):
    print(query.statement.compile(dialect=mysql.dialect(),
                                  compile_kwargs={"literal_binds": True}))
    
    
def get_domain(url:str):
    try:
        parse_obj = urlparse(url)    
        return parse_obj.netloc
    except:
        return None
