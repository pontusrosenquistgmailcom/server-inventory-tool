import storage
import menu
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Server Status Tool"
)
parser.add_argument(
    "--list",
    action="store_true",
    help="List all servers"
)
parser.add_argument(
    "--environment",
    choices=["prod", "test", "dev"],
    help="only list servers from a select environment (prod, test or dev): --environment prod"
)
parser.add_argument(
    "--check",
    type=str,
    help="Check status of select server name: --check web01"
)
parser.add_argument(
    "--check-all",
    action="store_true",
    help="check status of all select servers"
)
parser.add_argument(
    "--export",
    action="store_true",
    help="Export server data to csv file"
)

def main():

    #print("Hello world!")
    print("Server Status Tool v0.3.1 (Late Night edition)")

    # save CLI args
    args = parser.parse_args()

    # load config from envi variable
    config = storage.load_config()

    print(f"Config file set to: {config}")

    # load server data from json storage
    server_list = storage.load_data()

    if len(sys.argv) > 1:
        print("CLI args detected")

    else:
        # Main Menu UI loop
        menu.main_menu(server_list)


    # end of program
    storage.save_data(server_list)
# def main() end


if __name__ == "__main__":
    main()
