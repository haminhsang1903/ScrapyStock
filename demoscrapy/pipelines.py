# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy import signals
from scrapy.exporters import CsvItemExporter

import sqlite3
import time
import datetime
class DemoscrapyPipeline:
    def process_item(self, item, spider):
        return item

class VietStockExport(object):
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open('vietstockexport_bctc_demo.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

#TODO class export sqlite
# import sqlite3
class ExportToSQLite(object):

    # def spider_opened(self, spider):
        
    
    def process_item(self, item, spider): 
        try:
            self.connection = sqlite3.connect("VietStockDB.db")
            self.cursor = self.connection.cursor()  
            # res = item['TradingDate'][0][6:16]
            # print(int(res))
            self.cursor.execute("INSERT INTO dailyprice VALUES (%d,%d)"%
                            (int(item['TradingDate'][0][6:16])/1000,int(item['Time'][0][6:16])/1000))

            self.connection.commit()

            self.cursor.close()
            self.connection.close()
        except Exception as e:
            print("Error %s" % (str(e)))
        return item

    def spider_closed(self, spider):
        self.cursor.close()
        self.connection.close()



class ScrawlliststockPipeline:
    def process_item(self, item, spider):
        try:
            self.connection = sqlite3.connect("C:\\Users\\adven\\Desktop\\Angular\\Python\\ScrapyStock\\demoscrapy\\VietStockDB.db")
            self.cursor = self.connection.cursor()  
            # print(item['Name'][0])
            # DateNY,FIGICode,ISINCode,KLDKNY,KLLT,Name,StockCode
            self.cursor.execute("INSERT INTO listStock(DateNY,FIGICode,ISINCode,KLDKNY,KLLT,Name,StockCode) VALUES (?,?,?,?,?,?,?)",
                            (
                                int(time.mktime(datetime.datetime.strptime(item['DateNY'][0], "%d/%m/%Y").timetuple())), 
                                item['FIGICode'][0],item['ISINCode'][0],
                                float(item['KLDKNY'][0].replace(".","").replace(",",".")),
                                float(item['KLLT'][0].replace(".","").replace(",",".")),
                                item['Name'][0],
                                item['StockCode'][0]
                            )
            )

            self.connection.commit()
            
            self.cursor.close()
            self.connection.close()
            # ua replace o tren chu anh = =encode utf-8
        except Exception as e:
            print(e)
        # print(item['StockCode']) # Em muốn lấy cái value của StockCode hà mà nó ra
        return item

class reportFinancialVietStock:
    def process_item(self, item, spider):
        try:
            self.connection = sqlite3.connect("C:\\Users\\adven\\Desktop\\Angular\\Python\\ScrapyStock\\demoscrapy\\VietStockDB.db")
            self.cursor = self.connection.cursor()  
            data = [
                                item['Ticker'] ,
                                item['Trailing_EPS'] ,   
                                item['Book_value_per_share_BVPS'] ,   
                                item['PE'] ,   
                                item['PB'] ,   
                                item['ROE'] ,   
                                item['ROA'] ,  
                                item['Assets'] ,    
                                item['Cash_on_hand_gold_silver_gemstones'] ,  
                                item['Balances_with_SBV'] ,  
                                item['Balances_with_and_loans_to_other_credit_institutions'] ,  
                                item['Trading_securities'] ,  
                                item['Derivatives_other_fin_assets'] ,  
                                item['Loans_adv_and_fin_leases_to_customers'] ,  
                                item['Inv_securities'] ,  
                                item['Cap_Contribution_long_term_inv'] ,  
                                item['Fixed_assets'] ,  
                                item['Inv_properties'] ,  
                                item['Other_assets'] ,  
                                item['Total_assets'] ,  
                                item['L_E'] ,  
                                item['Amounts_due_to_Gov_t_and_SBV'] ,  
                                item['Deposits_and_borrowings_from_other_credit_institutions'] ,  
                                item['Deposits_from_customers'] ,
                                item['Derivatives_other_fin_Liabi'] , 
                                item['Other_borrowed_funds'] ,  
                                item['Valuable_papers_issued'] ,  
                                item['Other_liabi'] ,  
                                item['Cap_Reserves'] ,  
                                item['Mino_Interest'] ,  
                                item['NII'] ,  
                                item['Net_fee_and_commission_income'] ,  
                                item['Net_profit_from_trading_foreign_currencies_and_gold'] ,  
                                item['Net_profit_from_trading_of_trading_securities'] ,   
                                item['Net_profit_from_sale_of_inv_Securities'] ,  
                                item['Net_other_income'] ,  
                                item['Income_from_inv_in_other_entities'] ,  
                                item['Operating_expense'] ,  
                                item['Operating_profit_before_provision_for_credit_losses'] ,  
                                item['Provisions_for_credit_losses'] ,  
                                item['PBT'] ,  
                                item['Net_PAT'] ,  
                                item['PAT_for_SPC'] ,  
                                item['EPS'] ,
                                item['NR'] ,
                                item['COGS'],
                                item['GP'],
                                item['Financial_income'],
                                item['Fin_Expenses'],
                                item['Selling_expenses'],
                                item['G_A'],
                                item['Operating_profit'],
                                item['Other_profit'],
                                item['PL_of_inv_in_AJV'],
                                item['Current_assets'],
                                item['CCE'],
                                item['Short_term_inv'],
                                item['Short_term_rece'],
                                item['Inventories'],
                                item['Other_CA'],
                                item['Non_curr_assets'],
                                item['Inv_Properties_1'],
                                item['Long_term_inv'],
                                item['Liabilities'],
                                item['Short_term_liabi'],
                                item['Long_term_liabi'],
                                item['Owner_s_equity_'],
                                item['Charter_capital'],
                                item['Share_premium'],
                                item['RE'],
                                item['E_L'],
                                item['Gross_profit_margin'],
                                item['Net_profit_margin'],
                                item['Short_term_ratio'],
                                item['Interest_coverage'],
                                item['Liabilities_to_assets'],
                                item['Debt_to_equity'],
                                item['Non_CA'],
                                item['Owner_s_equity'],
                                item['Cash_ratio'],
                                item['Liabilities_to_equity'],
                                item['PL_of_inv_In_AJV_1'],
                                item['Total_NR'],
                                item['Total_direct_insurance_operating_expenses'],
                                item['Gross_insurance_operating_profit'],
                                item['Profit_from_insurance_operating'],
                                item['Profit_from_fin_Act'],
                                item['Total_profit'],
                                item['PAT_'],
                                item['Long_term_rece'],
                                item['Other_Non_CR'],
                                item['Goodwill'],
                                item['Reserves'],
                                
            ]
            # # print(data)
            self.cursor.execute("""INSERT INTO reportFinancialVietStock
                                (
                                Ticker,
                                Trailing_EPS,   
                                Book_value_per_share_BVPS,   
                                PE,   
                                PB,   
                                ROE,   
                                ROA,  
                                Assets,    
                                Cash_on_hand_gold_silver_gemstones,  
                                Balances_with_SBV,  
                                Balances_with_and_loans_to_other_credit_institutions,  
                                Trading_securities,  
                                Derivatives_other_fin_assets,  
                                Loans_adv_and_fin_leases_to_customers,  
                                Inv_securities,  
                                Cap_Contribution_long_term_inv,  
                                Fixed_assets,  
                                Inv_properties,  
                                Other_assets,  
                                Total_assets,  
                                L_E,  
                                Amounts_due_to_Gov_t_and_SBV,  
                                Deposits_and_borrowings_from_other_credit_institutions,  
                                Deposits_from_customers,
                                Derivatives_other_fin_Liabi, 
                                Other_borrowed_funds,  
                                Valuable_papers_issued,  
                                Other_liabi,  
                                Cap_Reserves,  
                                Mino_Interest,  
                                NII,  
                                Net_fee_and_commission_income,  
                                Net_profit_from_trading_foreign_currencies_and_gold,  
                                Net_profit_from_trading_of_trading_securities,   
                                Net_profit_from_sale_of_inv_Securities,  
                                Net_other_income,  
                                Income_from_inv_in_other_entities,  
                                Operating_expense,  
                                Operating_profit_before_provision_for_credit_losses,  
                                Provisions_for_credit_losses,  
                                PBT,  
                                Net_PAT,  
                                PAT_for_SPC,  
                                EPS,
                                NR,
                                COGS,
                                GP,
                                Financial_income,
                                Fin_Expenses,
                                Selling_expenses,
                                G_A,
                                Operating_profit,
                                Other_profit,
                                PL_of_inv_in_AJV,
                                Current_assets,
                                CCE,
                                Short_term_inv,
                                Short_term_rece,
                                Inventories,
                                Other_CA,
                                Non_curr_assets,
                                Inv_Properties_1,
                                Long_term_inv,
                                Liabilities,
                                Short_term_liabi,
                                Long_term_liabi,
                                Owner_s_equity_,
                                Charter_capital,
                                Share_premium,
                                RE,
                                E_L,
                                Gross_profit_margin,
                                Net_profit_margin,
                                Short_term_ratio,
                                Interest_coverage,
                                Liabilities_to_assets,
                                Debt_to_equity,
                                Non_CA,
                                Owner_s_equity,
                                Cash_ratio,
                                Liabilities_to_equity,
                                PL_of_inv_In_AJV_1,
                                Total_NR,
                                Total_direct_insurance_operating_expenses,
                                Gross_insurance_operating_profit,
                                Profit_from_insurance_operating,
                                Profit_from_fin_Act,
                                Total_profit,
                                PAT_,
                                Long_term_rece,
                                Other_Non_CR,
                                Goodwill,
                                Reserves
                                )
                                VALUES (?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?,?,?,?,?,?,?,?
                                       ,?,?,?
                                       )"""
            ,
                                data
            )
                            # (
                                   
                            # )
            # )

            self.connection.commit()
            # self.cursor.close()
            # self.connection.close()
        
        except Exception as e:
            print(e)
        # print(item['StockCode']) # Em muốn lấy cái value của StockCode hà mà nó ra
        return item