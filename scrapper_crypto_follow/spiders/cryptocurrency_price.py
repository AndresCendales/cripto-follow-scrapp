import scrapy
import datetime
from scrapy.crawler import CrawlerProcess

TODAY = datetime.date.today().strftime('%d-%m-%Y')
TIME = datetime.datetime.now().strftime('%HH-%MM')
#TIME = datetime.datetime.now()

OUTPUT = ''
USD_COP = 3792

class SpiderCoinbase(scrapy.Spider):
    name = 'coinbase'
    start_urls = [  
            'https://www.coinbase.com/price/bitcoin',
            'https://www.coinbase.com/price/ethereum',
            'https://www.coinbase.com/price/litecoin',
            'https://www.coinbase.com/price/zcash'
    ]
    
    custom_settings = {
        'FEED_URI' : f'/mnt/d/Platzi/Projects/crypto-follow-project/scrapper_crypto_follow/data/data.csv',
        'FEED_FORMAT' : 'csv',
        'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):
        crypto_currency = response.xpath('//h1[contains(@class,"TextElement__Spacer")]/text()').get()
        crypto_currency = crypto_currency.replace('(','')
        crypto_currency = crypto_currency.replace(')','')

        price = response.xpath('//span[contains(@class,"AssetChartAmount__Number")]/text()').get()
        price = float(price.replace(',',''))
        price = round(price / USD_COP,2)

        return {
            'date': TODAY,
            'time': TIME,
            'crypto_currency': crypto_currency,
            'price' : price,
            'currency': 'USD',            
            'source': 'coinbase'
        }


class SpiderCoinMarketCap(scrapy.Spider):
    name = 'Coin_Market_Cap'

    start_urls = [  
            'https://coinmarketcap.com/es/currencies/bitcoin/',
            'https://coinmarketcap.com/es/currencies/ethereum/',
            'https://coinmarketcap.com/es/currencies/litecoin/',
            'https://coinmarketcap.com/es/currencies/zcash/'
    ]
    
    
    custom_settings = {
        'FEED_URI' : f'/mnt/d/Platzi/Projects/crypto-follow-project/scrapper_crypto_follow/data/data.csv',
        'FEED_FORMAT' : 'csv',
        'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):

        crypto_currency = response.xpath('//div[contains(@class,"panel-header")]/h1/span/text()').get()

        price = response.xpath('//span[contains(@class,"panel-price__price")]/text()').get()
        
        price = price.replace(',','')
        price = price.replace('$','')
        price = float(price)
        

        return {
            'date': TODAY,
            'time': TIME,
            'crypto_currency': crypto_currency,
            'price' : price,
            'currency': 'USD',            
            'source': 'Coin Market Cap'
        }


class SpiderBeinCrypto(scrapy.Spider):
    name = 'be_in_crypto'
    start_urls = [  
            'https://es.beincrypto.com/precio/bitcoin/',
            'https://es.beincrypto.com/precio/ethereum/',
            'https://es.beincrypto.com/precio/litecoin/',
            'https://es.beincrypto.com/precio/zcash/'

    ]
    
    custom_settings = {
        'FEED_URI' : f'/mnt/d/Platzi/Projects/crypto-follow-project/scrapper_crypto_follow/data/data.csv',
        'FEED_FORMAT' : 'csv',
        'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):
        
        price = response.xpath('//div[@class = "top-block-row__col"]/div[@class = "row_val"]/text()').get()
        price = price.replace('&nbsp','')
        price =float(price)
        #price = price.replace(',','')
        
        crypto_currency_full = response.xpath('//div[contains(@class,"name")]/div[contains(@class,"sub-name")]/text()').get()
        crypto_currency = crypto_currency_full.split(",")


        return {
            'date': TODAY,
            'time': TIME,
            'crypto_currency': crypto_currency[0],
            'price' : price,
            'currency': 'USD',            
            'source': 'Be in Crypto'
        }

