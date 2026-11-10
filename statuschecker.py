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
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(server_list)
        return 0
        
    else:
        #print("No ping response from server")
        server['status'] = "down"
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(server_list)
        return 1



def update_all_servers(server_list):
    down_count = 0
    for server in server_list:

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
            down_count += 1
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    save_data(server_list)
    if down_count == 0:
        return 0
    else:
        return 1