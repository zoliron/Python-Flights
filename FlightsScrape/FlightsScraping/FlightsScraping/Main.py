import threading

from FlightsScrape.FlightsScraping.FlightsScraping.Crawler import Crawler
from FlightsScrape.FlightsScraping.FlightsScraping.Searcher import Searcher

if __name__ == '__main__':
    t1 = threading.Thread(target=Crawler().startCrawling()).start()
    t2 = threading.Thread(target=Searcher().startSearcher()).start()
