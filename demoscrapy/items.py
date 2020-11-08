# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DemoscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # ticker = scrapy.Field()
    jsonRes = scrapy.Field()
    # TODO
    # TradingDate = scrapy.Field()
    # TotalVolume = scrapy.Field()TotalValue"",""MtCap"",""Session3_Price"",""Diff_Price"",""DiffPercent_Price"",""Avg_Buy"",""Avg_Sell"",""Matching_Volume"",""Matching_Value""