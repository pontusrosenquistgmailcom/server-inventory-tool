# Server status tool
CLI tool that provides status information of your servers


## Requirements
python3.10 or later python package
ping (used in a subprocess)
Tested on Windows 11 26H2 and linux ubuntu 24.04

## Features
Lightweight Command-Line-Tool that can store your servers in a ubiquitous .json file
Quickly add or remove servers to your server watchlist
List all servers at once or look up only servers belonging to select environment
Status check a single server, or check all at once (in a sequence using ping)!
Export saved server data to the very portable .csv dataformat, all your Excel friends will love you!


server-inventory-tool will default its data storage to `servrar.json` users may set custom datafile name in system variable `INVENTORY_DATAFIL` example:

Windows:
``` powershell
# set INVENTORY_DATAFIL in your current session
$env:INVENTORY_DATAFIL = "servers.json"

# set INVENTORY_DATAFIL in your user profile (might require run as administrator if you want to target 'Machine')
[Environment]::SetEnvironmentVariable('INVENTORY_DATAFIL', 'servers.json', 'User')
```

Linux first one for session, second for permanent scope
```bash
export INVENTORY_DATAFIL="servers.json"

echo 'export INVENTORY_DATAFIL="servers.json" >> ~/.bashrc
```

to run the script in console mode do:

```
python3 ./main.py
```

to run the program in CLI mode:
```
python3 ./main.py --lista

python3 ./main.py --help
```


## Usage
Run script in console:
``` python
python3 .\main.py
``` 
or use the CLI arguments and switches to view all servers:
``` python
python3 .\main.py --lista
```

To view all servers in a specific environment:
``` python
python3 .\main.py --lista --miljo {prod,test,dev}
```

To check a specific server, if server is offline will exit with 1, else 0:
``` python
python3 .\main.py --kontrollera SERVERNAME
```

To check all servers, if one or more servers are offline will exit with 1, if all are online will exit with 0:
``` python
python3 .\main.py --kontrollera-alla
```

To export stored server data:
``` python
python3 .\main.py --export
```


Available CLI help:
```
  -h, --help            show this help message and exit
  --lista               List all servers
  --miljo {prod,test,dev}
                        List servers from a select environment (prod, test or dev)
  --kontrollera KONTROLLERA
                        Check status of select server name or adress
  --kontrollera-alla    Check status of all select servers
  --export              Export server data to csv file
```

## architecture
```
server-inventory-tool/
│
├── main.py             ← startpoint, main()
├── cli.py              ← read args and do command line logic
├── config.py           ← reads environment variable. act as global variable CONFIG
├── menu.py             ← console text menu UI. get user input
├── storage.py          ← load and save .json data, export to csv. display server lists
├── statuschecker.py    ← check/update server status
├── servrar.json        ← saved server data
├── .gitignore
└── README.md           ← You are here :D
```

main contains the program start logic for arguments, loading store data and deciding between console (menu) mode or CLI mode.

cli.py constains the CLI arguments and bindings as well all the switch case that is initiated if run in console mode

config.py loads the environment variable, or defaults to a default value

menu.py is the main console menu loop, it handles user input and much of the text that is printed in console mode

storage.py handles the reading of data and writing of data to .json and .csv. used by both cli.py and menu.py

statuschecker.py handles the ping:ing of servers. used by both cli.py and menu.py

