from pyjsonq import JsonQ

"""
This class responsible for the searches in the JSON file
It works as a terminal program with multiple choices for searches
"""


class Searcher():
    def numbersToCategory(self, number):
        switcher = {
            0: "exit",
            1: "company",
            2: "flightNumber",
            3: "cameFrom",
            4: "flightTime",
            5: "finalTime",
            6: "terminalNumber",
            7: "status",
        }
        return switcher.get(number, "Choose again")

    def startSearcher(self):
        while 1:
            print('Welcome to flights searcher, Please select what do you want to search: ')

            print('1. Search by company')
            print('2. Search by flight number')
            print('3. Search by origin of the flight')
            print('4. Search by original landing time')
            print('5. Search by updated landing time')
            print('6. Search by landing terminal number')
            print('7. Search by flight status')
            print('0. Exit')

            selectionNumber = input('Choose your searching category: ')
            try:
                selectionCategory = self.numbersToCategory(int(selectionNumber))
            except:
                selectionCategory = "Wrong category"

            if selectionCategory == "company":
                company = input('Choose the company you want to search for: ')
                self.parseResult(selectionCategory, company)


            elif selectionCategory == "flightNumber":
                flightNumber = input('Choose the flight number you want to search for: ')
                self.parseResult(selectionCategory, flightNumber)

            elif selectionCategory == "cameFrom":
                cameFrom = input('Choose the origin of the flight you want to search for: ')
                self.parseResult(selectionCategory, cameFrom)

            elif selectionCategory == "flightTime":
                flightTime = input('Choose the original landing time you want to search for: ')
                self.parseResult(selectionCategory, flightTime)

            elif selectionCategory == "finalTime":
                finalTime = input('Choose the updated landing time you want to search for: ')
                self.parseResult(selectionCategory, finalTime)

            elif selectionCategory == "terminalNumber":
                terminalNumber = input('Choose the landing terminal number you want to search for: ')
                self.parseResult(selectionCategory, terminalNumber)

            elif selectionCategory == "status":
                status = input('Choose the status you want to search for: ')
                self.parseResult(selectionCategory, status)

            elif selectionCategory == "exit":
                exit()

            else:
                print('You chose wrong category, please choose again' + "\n")

    def parseResult(self, selectionCategory, searchingPhrase):
        try:
            json = JsonQ('json/flights.json')
            if selectionCategory == 'status':
                result = json.at('flights').where(selectionCategory, '=', searchingPhrase).get()
            else:
                result = json.at('flights').where_contains(selectionCategory, searchingPhrase).get()
            if not result:
                print("There are no flights from the company: " + selectionCategory)
            else:
                for i in range(0, len(result)):
                    company = result[i]['company'].strip()
                    flightNumber = result[i]['flightNumber'].strip()
                    cameFrom = result[i]['cameFrom'].strip()
                    flightTime = result[i]['flightTime'].strip()
                    finalTime = result[i]['finalTime'].strip()
                    terminalNumber = result[i]['terminalNumber'].strip()
                    status = result[i]['status'].strip()
                    print(
                        'Flight number ' + str(i + 1) + ': Company: ' + company + '    Flight Number: ' + flightNumber +
                        '    Flight origin: ' + cameFrom + '    Original landing time: ' + flightTime +
                        '    Updated landing time: ' + finalTime + '    Terminal Number: ' + terminalNumber +
                        '    Flight status: ' + status)
                print("\n")
        except:
            print("There is no flights information at the moment, please try again" + "\n")


if __name__ == '__main__':
    Searcher().startSearcher()
