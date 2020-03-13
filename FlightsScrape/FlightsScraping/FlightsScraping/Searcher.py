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
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('company', company).get()
                    if not result:
                        print("There are no flights from the company: " + company)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")


            elif selectionCategory == "flightNumber":
                flightNumber = input('Choose the flight number you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('flightNumber', flightNumber).get()
                    if not result:
                        print("There are no flights with the flight number': " + flightNumber)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "cameFrom":
                cameFrom = input('Choose the origin of the flight you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('cameFrom', cameFrom).get()
                    if not result:
                        print("There are no flights from this origin: " + cameFrom)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "flightTime":
                flightTime = input('Choose the original landing time you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('flightTime', flightTime).get()
                    if not result:
                        print("There are no flights with this original landing time: " + flightTime)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "finalTime":
                finalTime = input('Choose the updated landing time you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('finalTime', finalTime).get()
                    if not result:
                        print("There are no flights that supposed to land at that time: " + finalTime)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "terminalNumber":
                terminalNumber = input('Choose the landing terminal number you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where_contains('terminalNumber', terminalNumber).get()
                    if not result:
                        print("There are no flights landing in this terminal: " + terminalNumber)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "status":
                status = input('Choose the status you want to search for: ')
                try:
                    json = JsonQ('json/flights.json')
                    result = json.at('flights').where('status', '=', status).get()
                    if not result:
                        print("There are no flights with this status: " + status)
                    else:
                        for i in range(0, len(result)):
                            print(result[i])
                    print("\n")
                except:
                    print("There is no flights information at the moment, please try again" + "\n")

            elif selectionCategory == "exit":
                exit()

            else:
                print('You chose wrong category, please choose again' + "\n")


if __name__ == '__main__':
    Searcher().startSearcher()
