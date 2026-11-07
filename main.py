import storage
import menu

print("Hello world!")
print("Server Status Tool v0.0.2 (Late Night edition)")


server_list = storage.load_data()


menu.main_menu(server_list)


#menu.show_all_servers(server_list)

#menu.show_select_server(server_list)



# end of program

storage.save_data(server_list)