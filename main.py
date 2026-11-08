import storage
import menu


def main():

    print("Hello world!")
    print("Server Status Tool v0.2.1 (Late Night edition)")

    # load config from envi variable
    config = storage.load_config()

    print(f"Config file set to: {config}")

    # load server data from json storage
    server_list = storage.load_data()

    # Main Menu UI loop
    menu.main_menu(server_list)


    # end of program
    storage.save_data(server_list)
# def main() end


if __name__ == "__main__":
    main()
