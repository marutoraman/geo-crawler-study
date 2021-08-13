from common.driver import * 


def test_driver():
    driver = Driver(True)
    driver.driver.get("https://www.amazon.co.jp/dp/B06VW79S1L")
    driver.quit()
    
    driver = Driver(False)
    driver.driver.get("https://www.amazon.co.jp/dp/B06VW79S1L")
    driver.quit()
    
    
def test_proxy():
    driver = Driver(headless_flg=True, is_proxy=True, proxy_host="zproxy.lum-superproxy.io",proxy_port="22225",proxy_user="lum-customer-hl_86e0768f-zone-zone1-country-jp",proxy_pass="9hpzwk3jsqpm")
    driver.driver.get("http://www.trackip.net/ip")
    print(driver.driver.page_source)