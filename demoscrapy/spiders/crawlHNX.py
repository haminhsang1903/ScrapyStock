import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import JsonRequest
from demoscrapy.items import ScrawlliststockItem
from scrapy.http.request.form import FormRequest
import json
import codecs
from bs4 import BeautifulSoup


class CrawlhnxSpider(scrapy.Spider):
    name = 'crawlHNX'
    # start_urls = ["https://www.reddit.com/r/cats"]
    start_urls = "https://www.hnx.vn/ModuleIssuer/List/ListSearch_Datas"

    def start_requests(self):
        # start_urls = ['https://finance.vietstock.vn']
        # Set the headers here. The important part is "application/json"
        # TODO setup for tickers
        for i in range(13):
            headers = {
                "Connection": "keep-alive",
                "Accept": "*/*",
                "X-Requested-With": "XMLHttpRequest",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68",
                "Content-Type": "application/x-www-form-urlencoded",
                "Origin": "https://www.hnx.vn",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.hnx.vn/vi-vn/cophieu-etfs/chung-khoan-ny.html",
                "Accept-Language": "en-US,en;q=0.9"
            }
            queries = {
                "p_issearch": "1",
                "p_keysearch": "0|0",
                "p_market_code": "",
                "p_orderby": "STOCK_CODE",
                "p_ordertype": "ASC",
                "p_currentpage": "1",
                "p_record_on_page": "10"
            }
            
            yield FormRequest(url=self.start_urls, formdata=queries, headers=headers,  callback=self.parse)

    def parse(self, response):

        # TODO parsejson item line json.loads()
        print(response.text)
        # jsonitems = json.loads(response.json)
        # print(response.body)
        # print(jsonitems['Content'])
        # for items in jsonitem['rows']:
            
        #     # print(items['cell'][1])
        #     il = ItemLoader(item=ScrawlliststockItem()) 
        #     il.add_value("StockCode", items['cell'][1]) # Get value cell of 1
        #     il.add_value("ISINCode", items['cell'][2])
        #     il.add_value("FIGICode", items['cell'][3])
        #     il.add_value("Name",items['cell'][4])
        #     il.add_value("KLDKNY", items['cell'][5])
        #     il.add_value("KLLT", items['cell'][6])# cái out put này đi đâu ? Dạ nó chỉ load rồi em in nó ra bên pipeline á !
        #     il.add_value("DateNY", items['cell'][7])
        #     yield il.load_item()
