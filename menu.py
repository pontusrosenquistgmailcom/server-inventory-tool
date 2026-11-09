# Menu logic for Server-Inventory-Tool

import storage
import statuschecker

def show_menu_text():
    print()
    print("1. Show all servers")
    print("2. Show servers in select environment")
    print("3. Add server")
    print("4. remove server")
    print("5. Check server")
    print("6. Check all servers")
    print("7. Export report (csv)")
    print("8. Exit program")
    print()


def add_server(server_list):
    print()
    i = 1
    while i != 0:
        i = 0
        user_server_name_input = input("Enter server name: ").strip()
        for server in server_list:
            if user_server_name_input.lower() == server['namn'].lower():
                print(f"That ({user_server_name_input})server name already exists. please select a unique server name.")
                i+=1
                break

    user_server_adress_input = input("Enter server adress: ").strip()
    i = 1
    while i!= 0:
        user_server_environment_input = input("Enter server environment[prod, test, dev]: ").strip().lower()
        match user_server_environment_input:
            case "prod" | "test" | "dev":
                i= 0
            case _:
                print("Please only use \'prod\' or \'test\' or \'dev\' as environment variables")

    user_server_role_input = input("Enter server role: ").strip()

    storage.add_new_server(
        server_list,
        user_server_name_input,
        user_server_adress_input,
        user_server_environment_input,
        user_server_role_input
    )

def remove_server(server_list):
    user_remove_server_name_input = input("Enter server name to remove: ").strip()
    for server in server_list:
        if user_remove_server_name_input == server['namn']:
            if server['miljo'] == "prod":
                user_input = input("Are you sure you want to remove this prod-env server (y/n): ")
                if user_input != "y":
                    print("Server removal canceled. returning to main menu.")
                    return
            storage.delete_server(server_list, server)
            print(f"Removed \'{server['namn']}\' from stored servers")
            return
    print(f"Server \'{user_remove_server_name_input}\' not found.")


def main_menu(server_list):
    while True:
        #print("Start of Menu loop")
        show_menu_text()

        menu_option = input("Select Menu option: ").strip()

        match menu_option:
            case "1":
                storage.show_all_servers(server_list)
            case "2":
                user_input = input("Select environment [prod, test, dev]: ").strip()
                storage.show_select_server(server_list, user_input)
            case "3":
                add_server(server_list)
            case "4":
                remove_server(server_list)
            case "5":
                user_input = input("Enter server name or adress: ").strip()
                server = storage.select_server(server_list, user_input)
                if server == None:
                    print("Server not found")
                else:
                    statuschecker.update_select_server(server_list, server)
                    print(f"Server \'{server['namn']}\' status updated to \'{server['status']}\'")
            case "6":
                print("Checking all servers...")
                if statuschecker.update_all_servers(server_list) == 0:
                    print("All servers are online")
                else:
                    print("One or more servers are offline")
            case "7":
                storage.export_data_csv(server_list)
            case "8"| "e" | "q" | "x" | "E" | "Q" | "X":
                print("Exiting program")
                return
            case _:
                print("Please only use option 1-8")











