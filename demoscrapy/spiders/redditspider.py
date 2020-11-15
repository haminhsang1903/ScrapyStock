import scrapy
# from scrapy.spiders import Spider
from demoscrapy.items import DemoscrapyItem
from scrapy.loader import ItemLoader
from scrapy.http import JsonRequest
from scrapy.http.request.form import FormRequest
import json


class RedditSpider(scrapy.Spider):
    name = "reddit"
    # start_urls = ["https://www.reddit.com/r/cats"]
    start_urls = "https://finance.vietstock.vn/data/gettradingresult"

    def start_requests(self):
        # start_urls = ['https://finance.vietstock.vn']
        # Set the headers here. The important part is "application/json"
        # TODO setup for tickers
        # for ticker in tickers:
        headers = {
            "Connection": "keep-alive",
            "Accept": "*/*",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36 Edg/86.0.622.63",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://finance.vietstock.vn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://finance.vietstock.vn/TCB/thong-ke-giao-dich.htm?grid=market",
            "Accept-Language": "en-US,en;q=0.9",
        }
        data = {
            "Code": "TCB",
            "OrderBy": "",
            "OrderDirection": "desc",
            "PageIndex": "1",
            "PageSize": "10",
            "FromDate": "2018-05-22",
            "ToDate": "2020-11-07",
            "ExportType": "default",
            "Cols": "TKLGD,TGTGD,VHTT,GD3,TGG,TGPTG,BQM,BQB,KLGDKL,GTGDKL",
            "ExchangeID": "1"
        }
        cookies = {
            '_ga': 'ga1.3.1850311231.1604374787',
            '_gid': 'ga1.3.126066724.1604835253',
            'finance_viewedstock': 'tcb,',
            'language': 'vi-vn',
            'isshowlogin': 'true',
            '__gads': 'id=b9a6aa2ec92c012a-22d43ad087c400d2:t=1604374787:rt=1604421617:s=alni_myhvd6d4yrprdjqjams7ulx3ubc_a',
            'cto_bundle': 'dewzc19bnxk4ctlhoef2t2gwqnc0dmx2u1rqdjfqwudvdnpbv2ntwuneelq0tndot3f1zu5pvmvpu2pzq0hcjtjczvylmkixrvp5a1cyehzwsvh6qmhlsmvqjtjczfvnuljqrmlljtjcnkdnvcuyqk9vsvdwmlzwd0swufvstmngv3prdnjur1zmrfroymu',
            'marketgidstorage': '%7b%220%22%3a%7b%22svspr%22%3a%22https%3a%2f%2ffinance.vietstock.vn%2fvnm%2ftai-chinh.htm%3ftab%3dctkh%22%2c%22svsds%22%3a1%2c%22tejndeedj%22%3a%22qmjvvaim5%22%7d%2c%22c756865%22%3a%7b%22page%22%3a11%2c%22time%22%3a1604407451284%7d%7d',
            '__requestverificationtoken': 'hedg-j2mullsj-tukbozwljd4gt1u4o6mauxyihjowghslsmhbgykimvyf4sxshgnvcmsvfff_d76n8whighn474w9jqhotp0sfzajcau6y1',
            '__oaue': 'false',
            'asp.net_sessionid': 'upunkqc05wtmn1nzzcx40xga',
            'adasiauserip': '115.77.123.31',
        }

        yield FormRequest(url=self.start_urls, formdata=data, headers=headers, cookies=cookies, callback=self.parse)

    def parse(self, response):

        # TODO parsejson item line
        jsonitem = json.loads(response.text)
        # print(jsonitem['Data'])
        for item in jsonitem['Data']:
            il = ItemLoader(item=DemoscrapyItem())
            il.add_value("TradingDate", item['TradingDate'])
            il.add_value("Time", item['Time'])
            yield il.load_item()


# scrapy crawl +name -o filename.json
