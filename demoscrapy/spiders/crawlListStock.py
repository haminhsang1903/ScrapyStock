import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import JsonRequest
from demoscrapy.items import ScrawlliststockItem
from scrapy.http.request.form import FormRequest
import json


class CrawlliststockSpider(scrapy.Spider):
    name = "crawlListStock"
    # start_urls = ["https://www.reddit.com/r/cats"]
    start_urls = "https://www.hsx.vn/Modules/Listed/Web/SymbolList"

    def start_requests(self):
        # start_urls = ['https://finance.vietstock.vn']
        # Set the headers here. The important part is "application/json"
        # TODO setup for tickers
        for i in range(13):
            headers = {
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68",
                "X-Requested-With": "XMLHttpRequest",
                "Sec-Fetch-Site": "same-origin",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Dest": "empty",
                "Referer": "https://www.hsx.vn/Modules/Listed/Web/Symbols?fid=18b12d5d2d554559bf10eeb90304ff2e&fbclid=IwAR0G5CpEyL-j1sgATy17cZ2zHmfkHKEQh9noOm7Jq-tsP9_lPiR99ZbvMxE",
                "Accept-Language": "en-US,en;q=0.9"
            }
            queries = {
                "pageFieldName1": "Code",
                "pageFieldValue1": "",
                "pageFieldOperator1": "eq",
                "pageFieldName2": "Sectors",
                "pageFieldValue2": "",
                "pageFieldOperator2": "",
                "pageFieldName3": "Sector",
                "pageFieldValue3": "00000000-0000-0000-0000-000000000000",
                "pageFieldOperator3": "",
                "pageFieldName4": "StartWith",
                "pageFieldValue4": "",
                "pageFieldOperator4": "",
                "pageCriteriaLength": "4",
                "_search": "false",
                "nd": "1605236186747",
                "rows": "30",
                "page": str(i+1),
                "sidx": "id",
                "sord": "desc"
            }
            
            yield FormRequest(url=self.start_urls, formdata=queries, headers=headers,  callback=self.parse)

    def parse(self, response):

        # TODO parsejson item line
        jsonitem = json.loads(response.text)
        # print(jsonitem['rows'][0]['cell'])
        for items in jsonitem['rows']:
            # if items['cell'][1]:
            # else:
            #     items['cell'][1] = None
            # print(items['cell'][1])
            il = ItemLoader(item=ScrawlliststockItem()) 
            il.add_value("StockCode", items['cell'][1]) # Get value cell of 1
            il.add_value("ISINCode", items['cell'][2])
            il.add_value("FIGICode", items['cell'][3])
            il.add_value("Name",items['cell'][4])
            il.add_value("KLDKNY", items['cell'][5])
            il.add_value("KLLH", items['cell'][6])# cái out put này đi đâu ? Dạ nó chỉ load rồi em in nó ra bên pipeline á !
            il.add_value("DateNY", items['cell'][7])
            yield il.load_item()
