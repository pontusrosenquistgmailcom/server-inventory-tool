# Menu logic for Server-Inventory-Tool

from storage import(
    add_new_server,
    export_data_csv
)

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

def show_table_headers():
    print(f"{'Server Name':<15} {'Adress':<15} {'Environment':<15} {'Role':<20} {'Status':<15} {'Last Checked':<15}")

def show_all_servers(server_list):
    print()
    show_table_headers()
          
    for server in server_list:
        print(f"{server['namn']:<15} {server['adress']:<15} {server['miljo']:<15} {server['roll']:<20} {server['status']:<15} {server['senast_kontrollerad']:<15}")


def show_select_server(server_list, user_input):
    print()
    #print(f"{'Server Name':<15} {'Adress':<15} {'Environment':<15} {'Role':<20} {'Status':<15} {'Last Checked':<15}")
          
    for server in server_list:
        if user_input.lower() in server['namn'].lower() or user_input.lower() in server['adress'].lower():
            show_table_headers()
            print(f"{server['namn']:<15} {server['adress']:<15} {server['miljo']:<15} {server['roll']:<20} {server['status']:<15} {server['senast_kontrollerad']:<15}")
            return

    print(f"No matching server name \'{user_input}\'")

def add_server(server_list):
    print()
    i = 1
    while i != 0:
        i = 0
        user_server_name_input = input("Enter server name: ").strip()
        for server in server_list:
            if user_server_name_input.lower() == server['namn'].lower():
                print("That server(name) already exists. please select a unique server name.")
                i+=1
                break

    user_server_adress_input = input("Enter server adress: ").strip()
    user_server_environment_input = input("Enter server environment[prod, test, dev]: ").strip().lower()
    user_server_role_input = input("Enter server role: ").strip()

    add_new_server(
        server_list,
        user_server_name_input,
        user_server_adress_input,
        user_server_environment_input,
        user_server_role_input
    )



def main_menu(server_list):
    while True:
        print("Start of Menu loop")
        show_menu_text()

        menu_option = input("Select Menu option: ").strip()

        match menu_option:
            case "1":
                show_all_servers(server_list)
            case "2":
                user_input = input("Enter server name or adress: ").strip()
                show_select_server(server_list, user_input)
            case "3":
                add_server(server_list)
            case "4":
                print("Remove server! NYI")
            case "5":
                print("Check server")
            case "6":
                print("Check all servers")
            case "7":
                print("Export csv report")
                export_data_csv(server_list)
            case "8"| "e" | "q" | "x" | "E" | "Q" | "X":
                print("Exiting program")
                return
            case _:
                print("Please only use option 1-8")











