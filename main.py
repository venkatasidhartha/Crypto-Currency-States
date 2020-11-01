import requests
from prettytable import PrettyTable

def cryptoCurrency():
    request = requests.get("https://api.coincap.io/v2/assets").json()
    id = []
    rank = []
    priceUsd = []
    changePercent24Hr = []
    #getting data in form of dictionary
    data = request["data"]
    #converting dictionary to list
    for dataList in data:
        #converting list to dictionary
        dict = dataList
        id.append(dict["id"])
        rank.append(dict["rank"])
        priceUsd.append(dict["priceUsd"])
        changePercent24Hr.append(dict["changePercent24Hr"])

    Columns = ["Rank", "Name", "Price", "Percentage"]
    myTable = PrettyTable()
    myTable.add_column(Columns[0],rank)
    myTable.add_column(Columns[1],id)
    myTable.add_column(Columns[2],priceUsd)
    myTable.add_column(Columns[3],changePercent24Hr)
    print(myTable)



cryptoCurrency()