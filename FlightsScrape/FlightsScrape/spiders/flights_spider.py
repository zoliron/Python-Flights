import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

from ..items import FlightsScrapeItem


class FlightsSpider(scrapy.Spider):
    name = 'flights'
    start_urls = [
        'https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        # self.driver.implicitly_wait(20)

    # How to parse the information from the page
    def parse(self, response):
        items = FlightsScrapeItem()
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
        element_present = expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'even'))
        WebDriverWait(self.driver, 10).until(element_present)

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
                print('Flight number ' + str(i) + ' got into an error')
