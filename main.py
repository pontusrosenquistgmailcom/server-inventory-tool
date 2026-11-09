import storage
import menu
import sys
import cli
import config

def main():
    # obtain CLI input
    args = cli.cli_args()

    # load config from environemnt variable
    #setting = storage.load_config()
    #print(f"Server data file set to: {config}")

    # load server data from json storage
    server_list = storage.load_data()

    if len(sys.argv) > 1:
        cli.cli_mode(server_list, args)

    else:
        # Main Menu UI loop
        print("Server Status Tool v0.3.2 (Late Night edition)")
        menu.main_menu(server_list)


    # end of program | maybe remove as most operations save serverdata when updated
    storage.save_data(server_list)
# def main() end


if __name__ == "__main__":
    main()
