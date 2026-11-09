import storage
import menu
import sys
import cli

def main():
    # obtain CLI input
    args = cli.cli_args()
    
    # load server data from json storage
    server_list = storage.load_data()

    if len(sys.argv) > 1:
        cli.cli_mode(server_list, args)

    else:
        # Main Menu UI loop
        print("Server Status Tool v0.3.5 (Early Morning edition)")
        menu.main_menu(server_list)


    # end of program | maybe remove as most operations save serverdata when updated
    storage.save_data(server_list)
# def main() end


if __name__ == "__main__":
    main()
