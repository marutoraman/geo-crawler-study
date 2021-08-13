from bs4 import BeautifulSoup
from common.utility import now_timestamp
import os
import zipfile
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

from common.logger import set_logger
from config.const import *
logger = set_logger(__name__)


class Driver():

    def __init__(self, headless_flg: bool = True, 
                 is_proxy:bool=False, proxy_user:str=None, proxy_pass:str=None, proxy_host:str=None, proxy_port:str=None):
        self.headless_flg = headless_flg
        self.proxy_url=f"https://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}" if is_proxy else None
        self.proxy_user = proxy_user
        self.proxy_pass = proxy_pass
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port        
        self.options = None
        self.driver = self.set_driver()

    def set_driver(self):
        # Chromeドライバーの読み込み
        self.options = ChromeOptions()

        # ヘッドレスモードの設定
        # if self.headless_flg:  # Linux　➙　本番環境のためHeadless
        #     self.options.add_argument('--headless')

        #logger.info(f"headless:{self.headless_flg} ")

        #self.options.add_argument('--user-agent=' + HEADER.USER_AGENT)
        # # self.options.add_argument('log-level=3')
        # # options.add_argument('--ignore-certificate-errors')
        # # options.add_argument('--ignore-ssl-errors')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--incognito')          # シークレットモードの設定を付与
        # # options.add_argument('disable-infobars')  # AmazonLinux用

        # # ChromeのWebDriverオブジェクトを作成する。
        # try:
        #     # driver = Chrome(options=options)
        #     driver = Chrome(ChromeDriverManager().install(), options=options)
        #     # driver = webdriver.Remote(command_executor='http://selenium-hub:4444/wd/hub',
        #     #                           options=options)
        #     logger.info("chrome driver起動成功")
        #     return driver
        # except Exception as e:
        #     logger.error(f"driver起動エラー:{e}")
        #     return None
        
        # ヘッドレスモードの設定
        if self.headless_flg:
            self.options.add_argument('--headless')
        
        # プロキシ設定
        if self.proxy_url != None:
            self._add_proxy_option() # Proxy設定

        self.options.add_argument('--user-agent=' + HEADER.USER_AGENT)
        #self.options.add_argument('log-level=3')
        #self.options.add_argument('--ignore-certificate-errors')
        #self.options.add_argument('--ignore-ssl-errors')
        
        #self.options.add_argument('--incognito')          # シークレットモードの設定を付与
        self.options.add_argument('--no-sandbox')          # docker環境では必須
        self.options.add_argument('disable-infobars') # AmazonLinux用
        logger.info(f"driver_info: headless:{self.headless_flg} / proxy_url:{self.proxy_url}")
        
        # ChromeのWebDriverオブジェクトを作成する。
        try:
            driver = Chrome(ChromeDriverManager().install(), chrome_options=self.options)
            logger.info("chrome driver起動成功")
            
            
            return driver
        except Exception as e:
            logger.error(f"driver起動エラー:{e}")
            raise Exception(f"driver起動エラー:{e}")
    
    def _add_proxy_option(self):
        manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

        background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (self.proxy_host, self.proxy_port, self.proxy_user, self.proxy_pass)

        pluginfile = 'proxy_auth_plugin.zip'

        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)
            self.options.add_extension(pluginfile)

    def set_geo_location(self, allowed_url:str, latitude:float, longitude:float):
        self.driver.execute_cdp_cmd(
            "Browser.grantPermissions",
            {
                "origin": allowed_url + "/*",
                "permissions": ["geolocation"]
            },
        )

        # 緯度、経度、緯度・経度の誤差(単位：m)を設定する
        self.driver.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",
            {
                "latitude": latitude,
                "longitude": longitude,
                "accuracy": 100,
            },
        )

    def wait_for_element(self, element_name: str, element_kind: str, wait_limit=100):
        wait = WebDriverWait(self.driver, wait_limit)  # 指定要素が表示されるまで待つ
        if element_kind == "ID":
            by = By.ID
        elif element_kind == "CSS_SELECTOR":
            by = By.CSS_SELECTOR
        elif element_kind == "CSS_NAME":
            by = By.CLASS_NAME
        elif element_kind == "NAME":
            by = By.NAME
        else:
            by = By.CSS_SELECTOR
        wait.until(expected_conditions.visibility_of_element_located(
            (by, element_name)))

    def select_element_by_name(self, name: str, select_text: str, mode: str = "", by: str = "NAME"):
        if by == "NAME":
            select_element = self.driver.find_element_by_name(name)
        elif by == "ID":
            select_element = self.driver.find_element_by_id(name)
        else:
            select_element = self.driver.find_element_by_css_selector(name)
        select_object = Select(select_element)
        # Select an <option> based upon its text
        if mode == "VALUE":
            select_object.select_by_value(select_text)
        else:
            select_object.select_by_visible_text(select_text)
        return select_object.first_selected_option

    def click_element_by_css_selector(self, selector):
        elms = self.driver.find_elements_by_css_selector(selector)
        if len(elms) >= 1:
            elms[0].click()
            return True
        return False

    def get_text_element_by_css_selector(self, selector):
        elms = self.driver.find_elements_by_css_selector(selector)
        if len(elms) >= 1:
            return elms[0].text
        return ""

    def save_screenshot(self, folder_path="screen_shot"):
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        page_width = self.driver.execute_script(
            'return document.body.scrollWidth')
        page_height = self.driver.execute_script(
            'return document.body.scrollHeight')
        self.driver.set_window_size(page_width, page_height)
        filename = f"error_{now_timestamp(mode='FILE')}.png"
        filepath = os.path.join(os.getcwd(), folder_path, filename)
        print(filepath)
        print(self.driver.get_screenshot_as_file(filepath))

    def exchange_soup(self) -> BeautifulSoup:
        return BeautifulSoup(self.driver.page_source, features="html.parser")

    def quit(self):
        self.driver.quit()

    def __del__(self):
        self.quit()
