from urllib.request import urlopen

import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
import scrapy

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(20)
driver.get("https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx")
timeout = 10
element_present = expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, 'odd'))
WebDriverWait(driver, timeout).until(element_present)

soup = BeautifulSoup(driver.page_source, "html.parser")
oddFlights = soup.find_all("tr", {"class": "odd"})
evenFlights = soup.find_all("tr", {"class": "even"})

# print(soup.prettify())
print(oddFlights)
print(evenFlights)