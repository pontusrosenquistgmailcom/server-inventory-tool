import storage
import menu


def main():

    print("Hello world!")
    print("Server Status Tool v0.0.2 (Late Night edition)")

    # load server data from json storage
    server_list = storage.load_data()

    # Main Menu UI loop
    menu.main_menu(server_list)


    # end of program
    storage.save_data(server_list)
# def main() end


if __name__ == "__main__":
    main()
