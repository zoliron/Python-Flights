# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import logging
import os


class FlightsscrapingPipeline(object):
    def __init__(self):
        logging.warning('Initializing Pipeline')

    def open_spider(self, spider):
        logging.warning('Open Spider')
        self.file = codecs.open('json/flights.json', 'w', encoding='utf-8')
        header = '{"flights":' + "\n" '['
        self.file.write(header)

    def close_spider(self, spider):
        logging.warning('Close Spider')
        footer = ']}'
        self.file.seek(-1, os.SEEK_END)
        self.file.truncate()
        self.file.write(footer)
        self.file.close()

    def process_item(self, item, spider):
        company = item['company'][0]
        flightNumber = item['flightNumber'][0]
        cameFrom = item['cameFrom'][0]
        flightTime = item['flightTime'][0]
        finalTime = item['finalTime'][0]
        terminalNumber = item['terminalNumber'][0]
        status = item['status'][0]
        data = {'company': company, 'flightNumber': flightNumber, 'cameFrom': cameFrom, 'flightTime': flightTime,
                'finalTime': finalTime, 'terminalNumber': terminalNumber, 'status': status}
        line = json.dumps(data, indent=4) + ','
        # line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
