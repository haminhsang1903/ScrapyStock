from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import sqlite3
date_now =  datetime.today().strftime('%d-%m-%Y')
# start_date = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
start_date = datetime.fromtimestamp(1424710800).strftime('%d-%m-%Y')
# difference_in_years = relativedelta(date_now, start_date).years
params = {}
params1 = {}
params['Samg'] = 1
params1['Haha'] = 2
dataset = []
dataset.append(params)
dataset.append(params1)
connection = sqlite3.connect("C:\\Users\\adven\\Desktop\\Angular\\Python\\ScrapyStock\\demoscrapy\\VietStockDB.db")
cursor = connection.cursor()
        
rows = cursor.execute("SELECT StockCode, DateNY FROM listStock where StockCode = 'TCB'").fetchall()
# params.insert('Samg')
# params.add('Hiếu')
print(rows)
# print(dataset[0].get(list(dataset[0])))
# print(date_now[6:])
# difference_in_years = relativedelta(date_now, start_date).years  