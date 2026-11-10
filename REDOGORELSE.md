# Written answers to questions!

### 1. Välj tre olika konstruktioner i koden, till exempel ett villkor, en loop och en funktion med parametrar och return. Förklara hur syntaxen fungerar och vad koden gör.

added explanations in #comments in the code blocks below

about a *loop* found in main_menu() from menu.py:

```python
def main_menu(server_list): # define/create the function, the (server_list) means we want to have a list of servers passed along when we call upon this function
    while True: # the recurring loop. this will keep looping (as it is always True) until we choose to sys.exit() or return.

        show_menu_text() # this helper function contains all the UI text that show the available options.

        menu_option = input("Select Menu option: ").strip() # we request userinput and store it in the menu_option variable .strip() removes empty spaces at start and end

        match menu_option: # match acts as a switch case in python, where the previously aquired menu_option is used as input. I am not sure if this is a better solution than a multi if elif 'ladder' 
            case "1": # in case of user input 1
                storage.show_all_servers(server_list) # calls the show_all_servers() function found in storage.py and passes along the server_list list of data
            case "2": # in case of user input 2
                # EDIT: upon examining this I might move this into its own 'helper' function in menu.py :^)
                user_input = input("Select environment [prod, test, dev]: ").lower().strip() # we ask for new user input and use the .lower() function to help combat different case inputs: ProD or deV or TEST will be accepted even tough the stored environments are all lowercase.
                if user_input == "prod" or user_input == "test" or user_input == "dev": # here we check if you read the previous input instruction :) and only proceed if input is valid
                    storage.show_select_server(server_list, user_input) # if input is OK we call upon the show_select_server() function from storage.py and pass along the server_list server data and the user defined user_input variable (which we have made sure is only prod test or dev)
                else:
                    print("Available environments are: [PROD] [TEST] [DEV]") # if you misspelt your environment we end up with this info message
            case "3":
                add_server(server_list) # calls the add_server() function where more user input will be handled
            case "4":
                remove_server(server_list) # calls the remove_server() function where more user input will be handled
            case "5":
                user_input = input("Enter server name or adress: ").strip()
                server = storage.select_server(server_list, user_input) # this function from storage.py returns a server dictionary if you entered a valid name or adress, if no matching server was found it will return None
                if server == None: # if we did not find a server we inform user
                    print("Server not found") # informative message
                else:
                    statuschecker.update_select_server(server_list, server) # else we use said server to run the updare_select_server() function from statuschecker.py
                    print(f"Server \'{server['namn']}\' status updated to \'{server['status']}\'") # we now display a short message with the updated server status (you will be informed of if it is up or down)
            case "6":
                print("Checking all servers...") # informative message, if servers are down the subprocess operations in the helper functions will take a few seconds to complete, this message is designed to make the user wait a little bit while the script is working
                if statuschecker.update_all_servers(server_list) == 0: # the update_all_servers() function from statuschecker.py will loop through the provided server_list and check each server entry. If one or more servers are offline the function will return 1, all up = return 0
                    print("All servers are online") # everything is fine
                else:
                    print("One or more servers are offline") # if one or more servers are down/offline we will print this information.
            case "7":
                storage.export_data_csv(server_list)
            case "8"| "e" | "q" | "x" | "E" | "Q" | "X": # the match ... case "...": allows us to specify multiple valid inputs with the OR operator | here, to allow us to exit from just hitting x, q or e into the menu input
                print("Exiting program") # inform user of their choice
                return # this return will exit the main_menu() function and the program will continue running the next steps in the main() function in the main.py file
            case _: # this is the default case, whenever user does not enter either of the specified cases (1-8 and the secret qexQEX exit options) we will end up here
                print("Please only use option 1-8") # information about what is 'valid' input for the main_menu() loop. this is the end of the loop and we will return to the 'start' 'while True:' and do it all over again!

```


about a *function and its parameters and return* found in update_all_server() from statuschecker.py:

```python
def update_all_servers(server_list): # define update_all_servers(server_list) function. we want the server data stored in a list to be passed along when this is called upon
    down_count = 0 # counter to keep track of how many servers are the be considered 'offline'
    for server in server_list: # simple loop to loop at each dictionary in the list

        # if windows
        if platform == "win32": # here we use the platform variable from sys library to check what OS we are on. internet says win32 means windows
            output = subprocess.run( # we use the subprocess.run() to acces the ping program. store the result in variable 'output'
                ["ping", "-n", "1", f"{server['adress']}"], # the 'command line' adapted for windows we pass along to the subprocess. note how we grab the address from the specific server using the f"{server['adress']}"
                capture_output=True,
                text=True
            )
        # elif linux (or macOS but i don't have a mac to test on)
        elif platform == "linux" or platform == "linux2" or "darwin": # same platform from sys check here but for linux & macOS
            output = subprocess.run(
                ["ping", "-c", "1", f"{server['adress']}"], # command line adapted for linux
                capture_output=True,
                text=True
            )


        if output.returncode == 0: # if the returncode is 0 we set the status to 'up'
            #print("Server ping response: OK") # old dev debug message :)
            server['status'] = "up"
        else:
            #print("No ping response from server")
            server['status'] = "down"
            down_count += 1 # in order to keep track of if there are serverd down we increase the down_count here
        server['senast_kontrollerad'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # use the datetime library to add the current time to our server
    
    save_data(server_list) # after the entire server_list has been handled we save our changes to the .json data file.
    if down_count == 0: # if all servers are up/responding to ping we return 0
        return 0
    else: # else we return 1, to indicate that 1 or more servers were down/not responding to ping
        return 1
```

aboiut a *condition* found in main() from main.py

```python
if len(sys.argv) > 1: # sys.argv contains the length of any passed arguments. if that length is over 1 we want to keep running the script in CLI mode
    cli.cli_mode(server_list, args)

```



### 2. Varför passar en lista med dictionaries för att lagra servrarna? Vilka datatyper har värdena i en server?

because we want to store several different servers whose related data is their own. each server has their own name, adress and other information. 

the list functionality in python makes it easy to loop through all servers to select a specific one, add a new server or remove an unwanted one fairly easily.

list with dictionaries also work well with the .json saving of data after exiting the program and the .csv export

in my implementation all the variables are of the string type. the last_checked variable contains a strftime str (still just a str though). if we wanted to store 'port' or something similar perhaps it should be stored as an int


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

All of the course documents and the various examples provided there

https://www.datacamp.com/cheat-sheet/markdown-cheat-sheet-23: markdown syntax help

https://www.datacamp.com/tutorial/python-switch-case: this has info on the ``match`` syntax used for a few switch case statements in the menus.

AI: copilot (and others), I asked for pointers about ``argparse`` (prompt: "Hello CoPilot, could you help explain/elaborate on the 'argparse' standard library in Python?" -> provided several examples and various points and ideas. not sure how accurate it is). also several syntax clarifications or "is it bad to do something with python like this..." questions either in a dedicated LLM convo or the google AI summary

google -> stackoverflow and various other sourses for syntax questions and clarifications
