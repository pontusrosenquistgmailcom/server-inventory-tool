import subprocess
import os
import datetime

from storage import save_data

def update_select_server(server_list, server):
    print("Hello from update_SELECT_server(...) function")
    print("")
    output = subprocess.run(
        ["ping", "-n", "1", f"{server['adress']}"],
        capture_output=True,
        text=True
    )
    if output.returncode == 0:
        print("Server ping response: OK")
        server['status'] = "up"
        
    else:
        print("No ping response from server")
        server['status'] = "down"

    server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_data(server_list)


def update_all_servers(server_list):

    for server in server_list:
        output = subprocess.run(
            ["ping", "-n", "1", f"{server['adress']}"],
            capture_output=True,
            text=True
        )
        if output.returncode == 0:
            #print("Server ping response: OK")
            server['status'] = "up"
        else:
            #print("No ping response from server")
            server['status'] = "down"
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    save_data(server_list)
    