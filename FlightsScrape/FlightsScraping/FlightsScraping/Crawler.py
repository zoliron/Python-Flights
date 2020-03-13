import logging

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from FlightsScrape.FlightsScraping.FlightsScraping.spiders.Flights import FlightsSpider

"""
This class defines how the Crawler operates the spider,
"""


class Crawler():
    def crawlJob(self):
        """
        Job to start spiders.
        Return Deferred, which will execute after crawl has completed.
        """
        settings = get_project_settings()
        runner = CrawlerRunner(settings)
        return runner.crawl(FlightsSpider)

    def scheduleNextCrawl(self, null, sleep_time):
        """
        Schedule the next crawl
        """
        reactor.callLater(sleep_time, self.crawl)

    def crawl(self):
        """
        A "recursive" function that schedules a crawl 300 seconds after
        each successful crawl.
        """
        # crawlJob() returns a Deferred
        d = self.crawlJob()
        # call schedule_next_crawl(<scrapy response>, n) after crawl job is complete
        d.addCallback(self.scheduleNextCrawl, 300)
        d.addErrback(self.catchError)

    def catchError(self, failure):
        print(failure.value)

    def startCrawling(self):
        # Schedule crawler every 5 minutes (every time that the site refreshes)
        self.crawl()

        # Starting the process
        reactor.run()


if __name__ == '__main__':
    logging.warning('Starting')
    Crawler().startCrawling()
