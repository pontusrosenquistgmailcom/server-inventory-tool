import json
import pathlib
import datetime
import csv

# read server information from servers.json
def load_data():
    DATAFILE = pathlib.Path("servers.json")
    if DATAFILE.exists():    
        with DATAFILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []
    


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
def export_data_csv(server_list):
    reports_directory = pathlib.Path("reports")
    reports_directory.mkdir(exist_ok=True)
    now = datetime.datetime.now()

    report_name = (
        f"{reports_directory}/report_{now.strftime('%Y-%m-%d_%H%M%S')}.csv"
    )

    print(report_name)
    with open(report_name, "w", newline="", encoding="utf-8") as file:

        report = csv.DictWriter(
            file,
            fieldnames=["namn", "adress", "miljo", "roll", "status", "senast_kontrollerad"]
        )
        report.writeheader()
        report.writerows(server_list)



# add new server to server_list array
def add_new_server(server_list, name, adress, environment, role):
    #print("start of the storage.add_new_server(...) function")
    new_server = {
        "namn": name,
        "adress": adress,
        "miljo": environment,
        "roll": role,
        "status": "unknown",
        "senast_kontrollerad": ""
    }
    server_list.append(new_server)
    save_data(server_list)
    #print("End of storage.add_new_server(...) function")
