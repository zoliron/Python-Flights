# -*- coding: utf-8 -*-
import logging
import os
import time

import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from ..items import FlightsscrapingItem

"""
This class defines how the spider works, how it retrieves data from the page and parse it,
Then sends the data to the class Items
"""


class FlightsSpider(scrapy.Spider):
    name = 'Flights'
    start_urls = [
        'https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx'
    ]

    def __init__(self):
        self.jsonFilePath = 'F:\Workspace\Python-Flights\FlightsScrape\FlightsScraping\FlightsScraping\json/flights.json'
        self.chromeDriverPath = "F:\Workspace\Python-Flights\FlightsScrape\FlightsScraping\chromedriver.exe"
        self.deleteFlights(self.jsonFilePath)
        self.driver = webdriver.Chrome(self.chromeDriverPath)
        self.driver.implicitly_wait(20)

    # How to parse the information from the page
    def parse(self, response):
        items = FlightsscrapingItem()
        self.driver.get(response.url)

        # Making the driver to wait until the condition is met (Waiting for the table to load to click on the button
        # to see all the flights)
        element_present = expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, 'כל הטיסות'))
        WebDriverWait(self.driver, 10).until(element_present)
        allFlightsButton = self.driver.find_element_by_link_text('כל הטיסות')
        allFlightsButton.click()

        # Making the driver to wait until the condition is met (waiting for the full table to load)
        element_present = expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, 'חזרה לתצוגת דפדוף'))
        WebDriverWait(self.driver, 10).until(element_present)

        # Making the driver to wait until the condition is met (waiting for the JS flights info table)
        # element_present = expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'even'))
        # WebDriverWait(self.driver, 10).until(element_present)

        # Getting the HTML data from the page
        soup = BeautifulSoup(self.driver.page_source, "html.parser")

        # Getting the odd flights from the table
        oddFlights = soup.find_all("tr", {"class": "odd"})

        # Getting the even flights from the table
        evenFlights = soup.find_all("tr", {"class": "even"})

        # Removing the first item in the Resultset because its not a flight
        evenFlights.pop(0)

        # Join the two result sets to get one result set to enumerate
        flights = oddFlights + evenFlights

        i = 0
        # Enumerate over the flights to extract the data
        for flight in flights:
            i = i + 1
            try:
                items['company'] = flight.find("img", {"class": "logoImg"})['alt'],
                items['flightNumber'] = flight.find("td", {"class": "FlightNum"}).get_text(),
                items['cameFrom'] = flight.find("td", {"class": "FlightFrom"}).get_text(),
                items['flightTime'] = flight.find("td", {"class": "FlightTime"}).get_text(),
                items['finalTime'] = flight.find("td", {"class": "finalTime"}).get_text(),
                items['terminalNumber'] = flight.find("td", {"class": "localTerminal"}).get_text(),
                items['status'] = flight.find("td", {"class": "status"}).get_text(),

                yield items
            except:
                logging.warning('Flight number ' + str(i) + ' got into an error')
                print('Flight number ' + str(i) + ' got into an error')

        self.driver.close()

    def deleteFlights(self, jsonFilePath):
        try:
            # Removing the old file before getting the new data
            os.remove(jsonFilePath)
            print('File has been removed successfully')
        except:
            print('Could not remove the file')
            pass

    def fixJsonFile(self, jsonFilePath):
        with open(jsonFilePath, 'rb+') as fp:
            fp.truncate(fp.seek(-1, os.SEEK_END))
            print('Last character has been deleted')

        with open(jsonFilePath, 'a') as fp:
            fp.write(']}')
            print('Json file has been fixed')


if __name__ == '__main__':
    process = CrawlerProcess(get_project_settings())

    process.crawl(FlightsSpider)
    process.start()  # the script will block here until the crawling is finished
