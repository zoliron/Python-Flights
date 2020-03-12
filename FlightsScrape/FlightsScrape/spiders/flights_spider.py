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
        element_present = expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'odd'))
        WebDriverWait(self.driver, timeout).until(element_present)
        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        oddFlights = soup.find_all("tr", {"class": "odd"})
        evenFlights = soup.find_all("tr", {"class": "even"})

        for oddFlight in oddFlights:
            yield {
                'company': oddFlight.find_all("td", {"class": "flightIcons"})[0].get_text(),
                'flightNumber': oddFlight.find_all("td", {"class": "FlightNum"})[0].get_text(),
                'cameFrom': oddFlight.find_all("td", {"class": "FlightFrom"})[0].get_text(),
                'flightTime': oddFlight.find_all("td", {"class": "FlightTime"})[0].get_text(),
                'finalTime': oddFlight.find_all("td", {"class": "finalTime"})[0].get_text(),
                'terminalNumber': oddFlight.find_all("td", {"class": "localTerminal"})[0].get_text(),
                'status': oddFlight.find_all("td", {"class": "status"})[0].get_text(),
            }

        for evenFlight in evenFlights:
            yield {
                'company': oddFlight.find_all("td", {"class": "flightIcons"})[0].get_text(),
                'flightNumber': oddFlight.find_all("td", {"class": "FlightNum"})[0].get_text(),
                'cameFrom': oddFlight.find_all("td", {"class": "FlightFrom"})[0].get_text(),
                'flightTime': oddFlight.find_all("td", {"class": "FlightTime"})[0].get_text(),
                'finalTime': oddFlight.find_all("td", {"class": "finalTime"})[0].get_text(),
                'terminalNumber': oddFlight.find_all("td", {"class": "localTerminal"})[0].get_text(),
                'status': oddFlight.find_all("td", {"class": "status"})[0].get_text(),
            }
