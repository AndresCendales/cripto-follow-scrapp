import scrapy
import datetime
from scrapy.crawler import CrawlerProcess

#Captura la fecha actual
DATE = datetime.date.today().strftime('%d-%m-%Y') 

#Captura la hora actual
#TIME = datetime.datetime.now().strftime('%MM-%HH')

class SpiderCoinbase(scrapy.Spider):
    """Spider para el website Coibase.com

    Returns:
        [Item]: Item con informacion scrapeada por cada url 
    """

    name = 'coinbase'
    start_urls = [  
            'https://www.coinbase.com/price/bitcoin',
            'https://www.coinbase.com/price/ethereum',
            'https://www.coinbase.com/price/litecoin',
            'https://www.coinbase.com/price/zcash'
    ]
    
    custom_settings = {
        #Guardar data en csv
        #'FEED_URI' : 'RUTA DEL ARCHIVO',
        #'FEED_FORMAT' : 'csv',
        #'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):
        crypto_currency = response.xpath('//h1[contains(@class,"TextElement__Spacer")]/text()').get()
        crypto_currency = crypto_currency.replace('(','')
        crypto_currency = crypto_currency.replace(')','')

        price = response.xpath('//span[contains(@class,"AssetChartAmount__Number")]/text()').get()
        price = float(price.replace(',',''))
        price = round(price,2)

        return {
            'date': DATE,
            #'time': TIME,
            'crypto_currency': crypto_currency,
            'price' : price,
            'source': 'coinbase',
        }


class SpiderCoinMarketCap(scrapy.Spider):
    """Spider para el website coin market cap

    Returns:
        [Item]: Item con informacion scrapeada por cada url 
    """

    name = 'coin_market_cap'

    start_urls = [  
            'https://coinmarketcap.com/es/currencies/bitcoin/',
            'https://coinmarketcap.com/es/currencies/ethereum/',
            'https://coinmarketcap.com/es/currencies/litecoin/',
            'https://coinmarketcap.com/es/currencies/zcash/'
    ]
    
    
    custom_settings = {
        #Guardar data en csv
        #'FEED_URI' : 'RUTA DEL ARCHIVO',
        #'FEED_FORMAT' : 'csv',
        #'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):

        crypto_currency = response.xpath('//div[contains(@class,"panel-header")]/h1/span/text()').get()
        crypto_currency = crypto_currency.replace('(','')
        crypto_currency = crypto_currency.replace(')','')
        price = response.xpath('//span[contains(@class,"panel-price__price")]/text()').get()
        
        price = price.replace(',','')
        price = price.replace('$','')
        price = float(price)
        

        return {
            'date': DATE,
            #'time': TIME,
            'crypto_currency': crypto_currency,
            'price' : price,
            'source': 'coin_market_cap'    
        }


class SpiderBeinCrypto(scrapy.Spider):
    """Spider para el website be in crypto

    Returns:
        [Item]: Item con informacion scrapeada por cada url 
    """

    name = 'be_in_crypto'
    start_urls = [  
            'https://es.beincrypto.com/precio/bitcoin/',
            'https://es.beincrypto.com/precio/ethereum/',
            'https://es.beincrypto.com/precio/litecoin/',
            'https://es.beincrypto.com/precio/zcash/'

    ]
    
    custom_settings = {
        #Guardar data en csv
        #'FEED_URI' : 'RUTA DEL ARCHIVO',
        #'FEED_FORMAT' : 'csv',
        #'FEED_EXPORT_ENCODING':'utf-8'
    }
    
    def parse(self, response):
        
        price = response.xpath('//div[@class = "top-block-row__col"]/div[@class = "row_val"]/text()').get()
        price = price.replace('&nbsp','')
        price =float(price)
        #price = price.replace(',','')
        
        crypto_currency_full = response.xpath('//div[contains(@class,"name")]/div[contains(@class,"sub-name")]/text()').get()
        crypto_currency = crypto_currency_full.split(",")


        return {
            'date': DATE,
            #'time': TIME,
            'crypto_currency': crypto_currency[0],
            'price' : price,
            'source': 'be_in_crypto', 
        }

