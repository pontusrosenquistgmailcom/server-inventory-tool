import subprocess
import os
import datetime
from sys import platform

from storage import save_data

def ping_windows(server):
    output = subprocess.run(
            ["ping", "-n", "1", "-w", "5000", f"{server['adress']}"],
            capture_output=True,
            text=True
        )
    return output

def ping_linux(server):
    output = subprocess.run(
            ["ping", "-c", "1", "-W", "5", f"{server['adress']}"],
            capture_output=True,
            text=True
        )
    return output

def update_select_server(server_list, server):
    # if windows
    if platform == "win32":
        output = ping_windows(server)

    # elif linux (or macOS but i don't have a mac to test on)
    elif platform == "linux" or platform == "linux2" or "darwin":
        output = ping_linux(server)

    if output.returncode == 0:
        server['status'] = "up"
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(server_list)
        return 0
        
    else:
        server['status'] = "down"
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        save_data(server_list)
        return 1



def update_all_servers(server_list):
    down_count = 0
    for server in server_list:

        # if windows
        if platform == "win32":
            output = ping_windows(server)

        # elif linux (or macOS but i don't have a mac to test on)
        elif platform == "linux" or platform == "linux2" or "darwin":
            output = ping_linux(server)

        if output.returncode == 0:
            server['status'] = "up"
        else:
            server['status'] = "down"
            down_count += 1
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    save_data(server_list)
    if down_count == 0:
        return 0
    else:
        return 1