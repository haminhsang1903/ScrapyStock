import  scrapy
# from scrapy.spiders import Spider
class RedditSpider(scrapy.Spider):
    name = "reddit"
    # start_urls = ["https://www.reddit.com/r/cats"]

    def start_requests(self):
        # start_urls = ['https://finance.vietstock.vn']
        start_urls = "https://finance.vietstock.vn/data/gettradingresult" 
    # Set the headers here. The important part is "application/json"
        headers =  {
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
            "_ga": "GA1.2.504380669.1604667120",
            "_gid": "GA1.2.450566067.1604667122",
            "language": "vi-VN",
            "isShowLogin": "true",
            "adAsiaUserIp": "123.25.131.195",
            "ASP.NET_SessionId": "xqwcyhb2mdrxinyngnsibjgq",
            "__RequestVerificationToken": "sZUCpnkeZGRFMBu8BNWFunp-xmj2HVCLo-qhnkHBeJg_UwPCOyveOWGUFrZPDF9eh1x2ymjXNqgbQ8WmeWRjW96OHA86xlwUJ3pcmbN5LPw1",
            "vts_usr_lg": "84973C532F14478C3AFA7A9367E1CDCCEDC45B6F268C786B53BEF7E5E5E8C1CE74F6593ACC6BF6FA12AB4FB8C0DD54433E46A461CCA95805848EB497C1CFEFED767AFDB0E48582467BE6B58F87F96717435C32D65BF54218D132868910C6E3C128644A139C3FC4D7D73878D08D4F257F3A3F0794075F1787758E7996C53461BC",
            "vst_usr_lg_token": "sCv0R4x26kidyZQgQhP4Zg==",
            "MarketGidStorage": "%7B%220%22%3A%7B%7D%2C%22C756865%22%3A%7B%22page%22%3A1%2C%22time%22%3A1604718497160%7D%7D",
            "cto_bundle": "RxKyIl9VQmplOFNQbTVnTlNpUTFsWUJqbDJmUFpVbnJQRldGSHB6SGJ1MW9NVE1wbFliM2ZNVVl3MmUlMkJMQXdHMkE4JTJGNkVidHJzWTI0cUpnVkwyY3pZUlJpeUhnT2JDTkRRaFRwNk9Ga2FNYW1Mb1ZnMEFCbGtmTm5VUnRoYjNBbVhUSyUyRmJkbTMzWFBGN01HVEFxOW80eCUyQjlGUSUzRCUzRA",
            "finance_viewedstock": "TCB,",
            "_gat_UA-1460625-2": "1",
            "__gads": "ID=63e0c31d1ad41ce4:T=1604748921:S=ALNI_MY02GWvEFhxHTNNGPGOO4Cv9UCCiA"
    }    
        
        yield scrapy.http.Request(start_urls,headers = headers, method='POST', cookies = cookies,)

    def parse(self, response):
        # with open("post.html",'wb') as f:
        #     f.write(response.body)
        yield response.json()
        
        
# scrapy crawl +name -o filename.json