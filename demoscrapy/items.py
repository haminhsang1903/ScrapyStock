# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ticker = scrapy.Field()
    # jsonRes = scrapy.Field()
    # TODO
    TradingDate = scrapy.Field()
    Time = scrapy.Field()
    StockCode = scrapy.Field()
    KLCPLH = scrapy.Field()
    KLCPNY = scrapy.Field()
    ClosePrice = scrapy.Field()
    PriorClosePrice = scrapy.Field()
    CeilingPrice = scrapy.Field()
    FloorPrice = scrapy.Field()
    TotalVol = scrapy.Field()

    # TotalValue"",""MtCap"",""Session3_Price"",""Diff_Price"",""DiffPercent_Price"",""Avg_Buy"",""Avg_Sell"",""Matching_Volume"",""Matching_Value""
class ScrawlliststockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StockCode = scrapy.Field() 
    ISINCode = scrapy.Field()
    FIGICode = scrapy.Field()
    Name = scrapy.Field()
    KLDKNY = scrapy.Field()
    KLLT = scrapy.Field()
    DateNY = scrapy.Field()

class ScrawlliststockItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StockCode = scrapy.Field()  
    ISINCode = scrapy.Field() # Mã 
    FIGICode = scrapy.Field() # Mã FIGI
    Name = scrapy.Field() 
    KLDKNY = scrapy.Field() # Khối lượng đăng ký niêm yết
    KLLH = scrapy.Field() # Khối lượng lưu hành
    DateNY = scrapy.Field() # Ngày niêm yết

class ReportfinancialvietstockSpiderItem(scrapy.Item):

    Ticker = scrapy.Field()
    Trailing_EPS = scrapy.Field() 
    Book_value_per_share_BVPS = scrapy.Field() 
    PE = scrapy.Field() 
    PB = scrapy.Field() 
    ROE = scrapy.Field() 
    ROA = scrapy.Field()
    Assets = scrapy.Field()  
    Cash_on_hand_gold_silver_gemstones = scrapy.Field()
    Balances_with_SBV = scrapy.Field()
    Balances_with_and_loans_to_other_credit_institutions = scrapy.Field()
    Trading_securities = scrapy.Field()
    Derivatives_other_fin_assets = scrapy.Field()
    Loans_adv_and_fin_leases_to_customers = scrapy.Field()
    Inv_securities = scrapy.Field()
    Cap_Contribution_long_term_inv = scrapy.Field()
    Fixed_assets = scrapy.Field()
    Inv_properties = scrapy.Field()
    Other_assets = scrapy.Field()
    Total_assets = scrapy.Field()
    L_E = scrapy.Field()
    Amounts_due_to_Gov_t_and_SBV = scrapy.Field()
    Deposits_and_borrowings_from_other_credit_institutions = scrapy.Field()
    Deposits_from_customers = scrapy.Field()
    Derivatives_other_fin_Liabi = scrapy.Field()
    Other_borrowed_funds = scrapy.Field()
    Valuable_papers_issued = scrapy.Field()
    Other_liabi = scrapy.Field()
    Cap_Reserves = scrapy.Field()
    Mino_Interest = scrapy.Field()
    NII = scrapy.Field()
    Net_fee_and_commission_income = scrapy.Field()
    Net_profit_from_trading_foreign_currencies_and_gold = scrapy.Field()
    Net_profit_from_trading_of_trading_securities = scrapy.Field() 
    Net_profit_from_sale_of_inv_Securities = scrapy.Field()
    Net_other_income = scrapy.Field()
    Income_from_inv_in_other_entities = scrapy.Field()
    Operating_expense = scrapy.Field()
    Operating_profit_before_provision_for_credit_losses = scrapy.Field()
    Provisions_for_credit_losses = scrapy.Field()
    PBT = scrapy.Field()
    Net_PAT = scrapy.Field()
    PAT_for_SPC = scrapy.Field()
    EPS = scrapy.Field()
    NR = scrapy.Field()
    COGS = scrapy.Field()
    GP = scrapy.Field()
    Financial_income = scrapy.Field()
    Fin_Expenses = scrapy.Field()
    Selling_expenses = scrapy.Field()
    G_A = scrapy.Field()
    Operating_profit = scrapy.Field()
    Other_profit = scrapy.Field()
    PL_of_inv_in_AJV = scrapy.Field()
    PL_of_inv_In_AJV_1 = scrapy.Field()
    Current_assets = scrapy.Field()
    CCE = scrapy.Field()
    Short_term_inv = scrapy.Field()
    Short_term_rece = scrapy.Field()
    Inventories = scrapy.Field()
    Other_CA = scrapy.Field()
    Non_curr_assets = scrapy.Field()
    Inv_Properties_1 = scrapy.Field()
    Long_term_inv = scrapy.Field()
    Liabilities = scrapy.Field()
    Short_term_liabi = scrapy.Field()
    Long_term_liabi = scrapy.Field()
    Owner_s_equity_ = scrapy.Field() 
    Charter_capital = scrapy.Field()
    Share_premium = scrapy.Field()
    RE = scrapy.Field()
    E_L = scrapy.Field()
    Gross_profit_margin = scrapy.Field()
    Net_profit_margin = scrapy.Field()
    Short_term_ratio = scrapy.Field()
    Interest_coverage = scrapy.Field()
    Liabilities_to_assets = scrapy.Field()
    Debt_to_equity = scrapy.Field()
    Non_CA  = scrapy.Field()
    Owner_s_equity  = scrapy.Field()
    Cash_ratio  = scrapy.Field()
    Liabilities_to_equity  = scrapy.Field()
    Total_NR = scrapy.Field()
    Total_direct_insurance_operating_expenses = scrapy.Field()
    Gross_insurance_operating_profit = scrapy.Field()
    Profit_from_insurance_operating = scrapy.Field()
    Profit_from_fin_Act = scrapy.Field()
    Total_profit = scrapy.Field()
    PAT_ = scrapy.Field()
    Long_term_rece = scrapy.Field()
    Other_Non_CR = scrapy.Field()
    Goodwill = scrapy.Field()
    Reserves = scrapy.Field()
    # ['Trailing_EPS',
    #  'Book_value_per_share_(BVPS)',
    #   'P/E',
    #    'P/B', 
    #    'ROE',
    #     'ROA']
# class ResultFinancialItem(scrapy.Item):
#     ID
