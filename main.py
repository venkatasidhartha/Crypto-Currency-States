import requests
from prettytable import PrettyTable

class cryptoCurrency:
    def request(self,URL):
        request = requests.get(URL).json()
        # getting data in form of dictionary
        data = request["data"]
        self.dataStorage(data)

    def dataStorage(self,data):
        id = []
        rank = []
        priceUsd = []
        changePercent24Hr = []
        # converting dictionary to list

        for dataList in data:
            # converting list to dictionary
            dict = dataList
            id.append(dict["id"])
            rank.append(dict["rank"])
            priceUsd.append(dict["priceUsd"])
            changePercent24Hr.append(dict["changePercent24Hr"])
        self.displayTables(rank, id, priceUsd, changePercent24Hr)

    def displayTables(self,rank, id, priceUsd, changePercent24Hr):
        Columns = ["Rank", "Name", "Price", "Percentage"]
        myTable = PrettyTable()
        myTable.add_column(Columns[0], rank)
        myTable.add_column(Columns[1], id)
        myTable.add_column(Columns[2], priceUsd)
        myTable.add_column(Columns[3], changePercent24Hr)
        print(myTable)

currency = cryptoCurrency()
ApiUrl = "https://api.coincap.io/v2/assets"
currency.request(ApiUrl)
