import json
import pathlib
import datetime
import csv
import os
# global variable CONFIG | seems to only be needed here!
from config import CONFIG

# read config data from config.json DEPRECATED (moved to config.py)
#def load_config():
#    env_file_name = os.getenv("INVENTORY_DATAFIL")
#    
#    if env_file_name is None:
#        print("No \'INVENTORY_DATAFIL\' environment variable set. defaulting to servers.json")
#        return pathlib.Path("servers.json")
#    else:
#        print(f"obtained file name from env: \'{env_file_name}\'")
#        return pathlib.Path(env_file_name)


# read server information from servers.json
def load_data():

    if CONFIG.exists():    
        with CONFIG.open("r", encoding="utf-8") as file:
            return json.load(file)
    else:
        return []


# write server information to servers.json
def save_data(server_list):
    
    with open(CONFIG, "w", encoding="utf-8") as file:
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

    with open(report_name, "w", newline="", encoding="utf-8") as file:

        report = csv.DictWriter(
            file,
            fieldnames=["namn", "adress", "miljo", "roll", "status", "senast_kontrollerad"]
        )
        report.writeheader()
        report.writerows(server_list)

    print(f"Exported server data to: {report_name}")


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

# remove server from server_list array
def delete_server(server_list, server):
    server_list.remove(server)
    save_data(server_list)


# console stdout server list headers. make sure to sync the numbers/headers/columns between this function and the print_server_info
def print_table_headers():
    print(f"{'Server Name':<15} {'Adress':<15} {'Environment':<15} {'Role':<20} {'Status':<10} {'Last Checked':<15}")

# console stdout server info print in table format
def print_server_table_line(server):
    print(f"{server['namn']:<15} {server['adress']:<15} {server['miljo']:<15} {server['roll']:<20} {server['status']:<10} {server['senast_kontrollerad']:<15}")

def show_all_servers(server_list):
    print()
    print_table_headers()
          
    for server in server_list:
        print_server_table_line(server)
        #print(f"{server['namn']:<15} {server['adress']:<15} {server['miljo']:<15} {server['roll']:<20} {server['status']:<10} {server['senast_kontrollerad']:<15}")


def show_select_server(server_list, user_input):
    print()
    print_table_headers()
    for server in server_list:
        if user_input == server['miljo']:
            print_server_table_line(server)
            #print(f"{server['namn']:<15} {server['adress']:<15} {server['miljo']:<15} {server['roll']:<20} {server['status']:<10} {server['senast_kontrollerad']:<15}")


# TODO: move to storage.py remove and update menu.py
def select_server(server_list, user_input):
    for server in server_list:
            if user_input.lower() in server['namn'].lower() or user_input.lower() in server['adress'].lower():
                return server
    return None
