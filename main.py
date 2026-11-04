import storage


print("Hello world!")
print("Server Status Tool v0.0.1 (Late Night edition)")


server_list = storage.load_data()

for server in server_list:
    print(f"Name: {server['namn']} - Role: {server['roll']}")








# end of program

storage.save_data(server_list)