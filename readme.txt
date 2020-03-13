1. IMPORTANT -> It is very recomended to use Pycharm to run this project since it handles the venv and supports Hebrew
	1.1 You can download Pycharm from here - https://www.jetbrains.com/pycharm/download/download-thanks.html?platform=windows&code=PCC
2. Start a project using git and clone from this URL - https://github.com/zoliron/Python-Flights.git
3. Go to "Your project path"\Python-Flights\FlightsScrape\FlightsScraping\FlightsScraping\spiders and enter to the file Flights.py
	3.1 Edit the two variables:
		3.1.1 self.jsonFilePath: "Your project path"\Python-Flights\FlightsScrape\FlightsScraping\FlightsScraping\json/flights.json
		3.1.2 self.chromeDriverPath: "Your project path"\Python-Flights\FlightsScrape\FlightsScraping\chromedriver.exe
3. After these changes, start the two main classes:
	3.1 Start Crawler class - This class will crawel and get the flights information with 5 minutes data refresh.
	3.2 Start Searcher class - This class will give you the ability to do searches on the data (Terminal Program)
4. If the searcher doesnt show you information, try to restart both classes instead of waiting 5 minutes to refresh
5. Use https://www.iaa.gov.il/he-IL/airports/BenGurion/Pages/OnlineFlights.aspx to get idea what to search 
6. Explanation about the classes can be found in the files