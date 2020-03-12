import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


class FlightsSpider(scrapy.Spider):
    name = 'flights'
    start_urls = [
        'https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        # self.driver.implicitly_wait(20)

    def parse(self, response):
        self.driver.get(response.url)
        timeout = 3
        element_present = expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'even'))
        WebDriverWait(self.driver, timeout).until(element_present)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        oddFlights = soup.find_all("tr", {"class": "odd"})
        evenFlights = soup.find_all("tr", {"class": "even"})
        evenFlights.pop(0)
        flights = oddFlights + evenFlights

        for flight in flights:
            yield {
                'company': flight.find("img", {"class": "logoImg"})['alt'],
                'flightNumber': flight.find("td", {"class": "FlightNum"}).get_text(),
                'cameFrom': flight.find("td", {"class": "FlightFrom"}).get_text(),
                'flightTime': flight.find("td", {"class": "FlightTime"}).get_text(),
                'finalTime': flight.find("td", {"class": "finalTime"}).get_text(),
                'terminalNumber': flight.find("td", {"class": "localTerminal"}).get_text(),
                'status': flight.find("td", {"class": "status"}).get_text(),
            }
