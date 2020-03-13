# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

"""
This class defines how the items retrieved from the page will be stored,
Then sends the data to the class Pipelines for storing it in JSON file
"""


class FlightsscrapingItem(scrapy.Item):
    # define the fields for your item here like:
    company = scrapy.Field()
    flightNumber = scrapy.Field()
    cameFrom = scrapy.Field()
    flightTime = scrapy.Field()
    finalTime = scrapy.Field()
    terminalNumber = scrapy.Field()
    status = scrapy.Field()
