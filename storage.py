import json
import pathlib

# read server information from servers.json
def load_data():
    DATAFILE = pathlib.Path("servers.json")

    with DATAFILE.open("r", encoding="utf-8") as file:
        return json.load(file)


# write server information to servers.json
def save_data(server_list):
    
    with open("servers.json", "w", encoding="utf-8") as file:
        json.dump(
            server_list,
            file,
            indent=2,
            ensure_ascii=False
        )


# 1. export server info to CSV file
# 2. give csv file to friends who enjoy excel :)
def export_data_csv():
    print("Do the data export to CSV thing...")