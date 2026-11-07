# Menu logic for Server-Inventory-Tool

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
                print("Add server! NYI")
                
            case "8"| "e" | "q" | "x" | "E" | "Q" | "X":
                print("Exiting program")
                return
            case _:
                print("Please only use option 1-8")











