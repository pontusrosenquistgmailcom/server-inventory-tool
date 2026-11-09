# Written answers to questions!

### 1. Välj tre olika konstruktioner i koden, till exempel ett villkor, en loop och en funktion med parametrar och return. Förklara hur syntaxen fungerar och vad koden gör.


TOUGH QUESTION
FOLLOW UP LATER!


### 2. Varför passar en lista med dictionaries för att lagra servrarna? Vilka datatyper har värdena i en server?

I WILL HAVE TO THINK ABOUT IT ALRIGHT


### 3. Varför sparar du data i JSON men exporterar rapporten som CSV?

.json is a widely adopted data format that many other systems can read. one could theoretically use the servers.json 'database' in a different script or application. many programming languages have standard or well established libraries that allows for easy reading/writing of .json files.

.csv is useful for non-programmers who want to utilize the contents of our 'database' in a excel/access/calc sheet context

### 4. Hur är programmet uppdelat i moduler och funktioner? Vilket ansvar har varje fil?

main.py:
Program entry point
- main()
- uses cli.py in case of commandline arguments, storage.py to load stored server data, menu.py to run console interactions

config.py:
- reads environment variable INVENTORY_DATAFIL and provides CONFIG for easy access

cli.py:
- cli_mode() for command line logic and workflow. 
- binds and parses arguments
- calls upon storage.py and statuschecker for various support functions and logic

storage.py:
- load_data(): reads stored server data
- save_data(): writes the server dictionary list to servers.json
- export_data_csv(): exports the runtime dictionary list content to .csv report file
- Contains a heap of various helper functions to add, remover and display the content of the server dictionary list

menu.py:
- main_menu(): this is the loop that print menu option text, match user input to case in switch and handles several user input validations
- calls upon storage.py and statucchecker.py for logic

statuschecker.py:
- update_all_servers(): performs the 'status' check/update for each server in the server_list
- update_select_server(): performs status check/update for selected server. calls upon storage.py to save_data()



### 5. Vilka moduler från standardbiblioteket använder du och till vad?

sys: Detect what OS we are executing in. to exit the program with apropriate exit code. detect if we should run in console mode or CLI mode. 

argparse: to bind and parse CLI arguments

subprocess: to help us run the ping program from the python script (or rather spawn a process with ping and read the results)

datetime: help us always export to a unique report file (based on time of report request) and to add a timestamp to when a server was checked for its online/offline status

os: obtain the INVENTORY_DATAFIL environment variable

pathlib: help us handle paths for files and directories used by the python script

json: to make reading from and writing to json files extremely simple.

csv: to make exporting to .csv extemely simple.

### 6. Ge tre exempel på god praxis från din kod och förklara varför de är bra.

Fairly consistent use of only English across code and comments. HOWEVER several of the course requirements/targets list various variable/environment names in swedish. will see if we can have the changed to english to remove the last SWEnglish.

Most variables are using snake_case (execption: CONFIG)

Logic is split into their separate 'domain files', CLI stuff in the cli.py file, storage stuff in the storage.py file etc. main.py is very minimal, only calls upon the different 'support' functions to start the program (check for arguments, load server data from json -> if args do cli_mode logic, else run main_menu console logic).

### 7. Vilka källor och hjälpmedel har du använt och till vad? Det kan till exempel vara kursboken, dokumentation, forum eller AI-verktyg.

All of the course documents

https://www.datacamp.com/tutorial/python-switch-case: this has info on the ``match`` syntax used for a few switch case statements in the menus.

AI: copilot, I asked for pointers about ``argparse`` (prompt: "Hello CoPilot, could you help explain/elaborate on the 'argparse' standard library in Python?" -> provided several examples and various points and ideas. not sure how accurate it is). also several syntax clarifications or "is it bad to do something with python like this..."

google -> stackoverflow and various other sourses for syntax questions and clarifications
