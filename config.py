import pathlib
import os

# attempt at global variable config instead of passing a config var from main to menu to storage and back and for and and the entire program
# seems to be working

def load_config():
    env_file_name = os.getenv("INVENTORY_DATAFIL")
    
    if env_file_name is None:
        print("No \'INVENTORY_DATAFIL\' environment variable set. defaulting to \'servers.json\'")
        return pathlib.Path("servers.json")
    else:
        #print(f"Obtained \'{env_file_name}\' from system variable INVENTORY_DATAFIL")
        return pathlib.Path(env_file_name)

# TODO: make this a list with DATAFILE, REPORTDIR and so on
CONFIG = load_config()
