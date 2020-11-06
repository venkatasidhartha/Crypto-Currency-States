import requests
from prettytable import PrettyTable

def request(URL):
    request = requests.get(URL).json()
    data = request["data"]
    dataStorage(data)

def dataStorage(data):
    id = []
    rank = []
    priceUsd = []
    changePercent24Hr = []
    for dataList in data:
        #converting list to dictionary
        dict = dataList
        id.append(dict["id"])
        rank.append(dict["rank"])
        priceUsd.append(dict["priceUsd"])
        changePercent24Hr.append(dict["changePercent24Hr"])
    displayTables(rank,id,priceUsd,changePercent24Hr)

def displayTables(rank,id,priceUsd,changePercent24Hr):
    Columns = ["Rank", "Name", "Price", "Percentage"]
    myTable = PrettyTable()
    myTable.add_column(Columns[0], rank)
    myTable.add_column(Columns[1], id)
    myTable.add_column(Columns[2], priceUsd)
    myTable.add_column(Columns[3], changePercent24Hr)
    print(myTable)


ApiUrl = "https://api.coincap.io/v2/assets"
request(ApiUrl)
