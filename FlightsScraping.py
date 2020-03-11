from bs4 import BeautifulSoup # HTML data structure
from urllib.request import urlopen # Web client

# URl to web scrap from.
flights_url = "https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx"

uClient = urlopen(flights_url)