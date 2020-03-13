import logging

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from FlightsScrape.FlightsScraping.FlightsScraping.spiders.Flights import FlightsSpider


def crawlJob():
    """
    Job to start spiders.
    Return Deferred, which will execute after crawl has completed.
    """
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    return runner.crawl(FlightsSpider)


def scheduleNextCrawl(null, sleep_time):
    """
    Schedule the next crawl
    """
    reactor.callLater(sleep_time, crawl)


def crawl():
    """
    A "recursive" function that schedules a crawl 300 seconds after
    each successful crawl.
    """
    # crawlJob() returns a Deferred
    d = crawlJob()
    # call schedule_next_crawl(<scrapy response>, n) after crawl job is complete
    d.addCallback(scheduleNextCrawl, 10)
    d.addErrback(catchError)


def catchError(failure):
    print(failure.value)


if __name__ == '__main__':
    logging.warning('Starting')
    # Schedule crawler every 5 minutes (every time that the site refreshes)
    crawl()

    # Starting the process
    reactor.run()