# Server status tool
CLI tool that provides status information of your servers

TODO: update README.md

## Requirements
python3.10 or later python package

## Features
Stores server information in json-datafile (default: `servers.json`)

Can set custom datafile in system variable `INVENTORY_DATAFIL`

Export server data to CSV file


## Usage
Run script in console:
``` python
python3 .\main.py
``` 
or use the command line arguments and switches such as:
``` python
python3 .\main.py --list
```
Available CLI options:
```
  -h, --help            # show this help message and exit
  --list                # List all servers
  --environment {prod,test,dev}
                        # List servers from a select environment (prod, test or dev)
  --check CHECK         # Check status of select server name or adress
  --check-all           # Check status of all select servers
  --export              # Export server data to csv file
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
├── servers.json        ← saved server data
├── .gitignore
└── README.md           ← You are here :D
```

