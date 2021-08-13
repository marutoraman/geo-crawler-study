class HEADER():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36}"
    API_HEADRS = {
        'Content-Type': 'application/json; charset=utf-8',
    }


class URL():
    YAHOO_LOGIN = "https://login.yahoo.co.jp/config/login"
    SYUPPIN_URL = "https://auctions.yahoo.co.jp/sell/jp/show/submit?category=0"
    AMAZON_IMAGE_URL = "https://images-na.ssl-images-amazon.com/images/I"
    CATEGORY_SEARCH = "https://auctions.yahoo.co.jp/sell/jp/show/topsubmit?type=1"
    SYUPPIN_SUBMIT = "https://auctions.yahoo.co.jp/sell/jp/show/preview"
    SYUPPIN_CLOSE = "https://auctions.yahoo.co.jp/closeduser/jp/show/mystatus?select=closed&hasWinner=1"
    TORIHIKI_NAVI = "https://contact.auctions.yahoo.co.jp/seller/top?aid="
    AUCTION_PAGE = "https://page.auctions.yahoo.co.jp/jp/auction"


class SLACK_MESSAGE():
    START_MESSAGE = "起動が完了しました"
    ERROR_MESSAGE = "ストップエラーが発生しました。終了します。"


class SYUPPIN_STAT():
    SEARCHED = 0
    SYUPPIN_RESERVE = 1
    SYUPPIN = 2
    CLOSE_NOT_BUIED = 3
    CLOSE_BUIED = 4
    ERROR = 5
    SAISYUPPIN_RESERVE = 10
    LOW_STOCK_ERROR = 100
    PRICE_ERROR = 101


class TORIHIKI_STAT():
    BEFORE_START = 0
    BEFORE_PAY = 1
    AFTER_PAIED = 2
    BEFORE_SHIPPING = 3
    AFTER_SHIPPING = 4
    COMPLETED = 5
    CANCEL = 10
    ERROR = 11


class STAT():
    BEFORE_START = 0
    RESERVED = 1
    COMPLETED = 2


class STOCK_STAT():
    OK = 0
    NG = 1
    URL_ERROR = 9


class MESSAGE():
    DEFAUL_EVAL = "迅速な対応ありがとうございました。また機会がございましたら、宜しくお願いいたします。"
    COMPLETE_SHIPPING = "発送完了いたしました。到着までしばしお待ちいただきたく思います。\nこの度はご利用ありがとうございました。"


class LOCAL():
    TEMP_IMAGE_SAVE_PATH = "./tmp"


class PRICE():
    OFFSET_SAISYUPPIN = 100


class STOCK_CHECK_SETTING():
    MIN_STOCK_LIMMIT = 4
    MAX_SHIPPING_LEADTIME = 7
