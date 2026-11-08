import subprocess
import os
import datetime
from sys import platform

from storage import save_data

def update_select_server(server_list, server):
    # if windows
    if platform == "win32":
        output = subprocess.run(
            ["ping", "-n", "1", f"{server['adress']}"],
            capture_output=True,
            text=True
        )
    # elif linux (or macOS but i don't have a mac to test on)
    elif platform == "linux" or platform == "linux2" or "darwin":
        output = subprocess.run(
            ["ping", "-c", "1", f"{server['adress']}"],
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
    