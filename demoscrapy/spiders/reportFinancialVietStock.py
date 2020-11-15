import scrapy
from scrapy.loader import ItemLoader
from scrapy.http import JsonRequest
from demoscrapy.items import ReportfinancialvietstockSpiderItem
from scrapy.http.request.form import FormRequest
import json
import sqlite3
from datetime import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd
import logging
logging.basicConfig(filename='test.log', level=logging.INFO)


class ReportfinancialvietstockSpider(scrapy.Spider):
    name = 'reportFinancialVietStock'
    
    start_urls = 'https://finance.vietstock.vn/data/financeinfo'
    # def __init__(self, **kwargs):
    #     start_urls = ['https://finance.vietstock.vn/data/financeinfo']

    #     super().__init__(**kwargs)

    def start_requests(self):
        # TODO setup for tickers
        # Set data for Request
        connection = sqlite3.connect("C:\\Users\\adven\\Desktop\\Angular\\Python\\ScrapyStock\\demoscrapy\\VietStockDB.db")
        cursor = connection.cursor()
        
        rows = cursor.execute("SELECT StockCode, DateNY FROM listStock").fetchall()

        for StockCode, DateNY in rows:           
            ts = DateNY
            date_now =  datetime.today().strftime('%d-%m-%Y')
            start_date = datetime.fromtimestamp(ts).strftime('%d-%m-%Y')      
            difference_in_years = int(date_now[6:])-int(start_date[6:]) 

            ticker = StockCode
            page = difference_in_years
            headers = {
                    "Connection": "keep-alive",
                    "Accept": "*/*",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.193 Safari/537.36 Edg/86.0.622.68",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "Origin": "https://finance.vietstock.vn",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://finance.vietstock.vn/{}/tai-chinh.htm".format(ticker),
                    "Accept-Language": "en-US,en;q=0.9"
            }
            queries = {
                    "Code": str(ticker),
                    "ReportType": "BCTT",
                    "ReportTermType": "2",
                    "Unit": "1000000",
                    "Page": str(page),
                    "PageSize": "4"
            }
                
            yield FormRequest(url=self.start_urls, formdata=queries, headers=headers,  callback=self.parse, meta={'ticker': ticker})
            

    def parse(self, response):
        # TODO parsejson item line
        jsonitem = json.loads(response.text)
        # print(jsonitem)
        for i in range(1,5): 
            # TermCode = jsonitem[0]          
            # Get TermCode in Array[0]    
            try:      
                TermCode = jsonitem[0][i-1]['TermCode']
                YearPeriod = jsonitem[0][i-1]['YearPeriod']
            except Exception as e:
                print(response.meta['ticker'])
                continue
            # print('Kết quả kinh doanh')   
            items = ReportfinancialvietstockSpiderItem()
            items['Ticker'] = response.meta['ticker']+'_'+str(TermCode)+'_'+str(YearPeriod)
            for item in jsonitem[1]['Kết quả kinh doanh']:
                itemfm = item['NameMobileEn'].replace(' ', '_').replace('.','').replace('/','').replace(',','').replace('&_','').replace('-','_').replace('&', '_').replace("""'""",'_').replace("(",'').replace(")",'')
                if itemfm == 'PL_of_inv_In_AJV':
                    itemfm = 'PL_of_inv_In_AJV_1'
                if itemfm == 'Inv_Properties':
                    itemfm = 'Inv_Properties_1'
                try:
                    items[itemfm] = 0.0 if item['Value{}'.format(i)] is None else item['Value{}'.format(i)]
                except Exception as e:
                    logging.info(itemfm)
            # print('Cân đối kế toán')     
            for item in jsonitem[1]['Cân đối kế toán']:
                itemfm = item['NameMobileEn'].replace(' ', '_').replace('.','').replace('/','').replace(',','').replace('&_','').replace('-','_').replace('&', '_').replace("""'""",'_').replace("(",'').replace(")",'')
                # items[itemfm] = 0.0 if item['Value{}'.format(i)] is None else item['Value{}'.format(i)]
                if itemfm == 'PL_of_inv_In_AJV':
                    itemfm = 'PL_of_inv_In_AJV_1'
                if itemfm == 'Inv_Properties':
                    itemfm = 'Inv_Properties_1'
                try:
                    items[itemfm] = 0.0 if item['Value{}'.format(i)] is None else item['Value{}'.format(i)]
                except Exception as e:
                    logging.info(itemfm)
            # # print('Chỉ số tài chính') 
            for item in jsonitem[1]['Chỉ số tài chính']:
                itemfm = item['NameMobileEn'].replace(' ', '_').replace('.','').replace('/','').replace(',','').replace('&_','').replace('-','_').replace('&', '_').replace("""'""",'_').replace("(",'').replace(")",'')
                # items[itemfm] = 0.0 if item['Value{}'.format(i)] is None else item['Value{}'.format(i)]
                # il.add_value(itemfm,item['Value{}'.format(i)]) 
                if itemfm == 'PL_of_inv_In_AJV':
                    itemfm = 'PL_of_inv_In_AJV_1'
                if itemfm == 'Inv_Properties':
                    itemfm = 'Inv_Properties_1'
                try:
                    items[itemfm] = 0.0 if item['Value{}'.format(i)] is None else item['Value{}'.format(i)]
                except Exception as e:
                    logging.info(itemfm)
            yield items
        
        
