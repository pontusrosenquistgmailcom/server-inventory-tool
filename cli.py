import sys
import argparse
import storage
import statuschecker


# main.py was getting crowded

def cli_args():
    parser = argparse.ArgumentParser(
        description="Server Status Tool v0.3.5 (Early Morning edition)"
    )
    parser.add_argument(
        "--lista",
        action="store_true",
        help="List all servers"
    )
    parser.add_argument(
        "--miljo",
        choices=["prod", "test", "dev"],
        type=str.lower,
        help="List servers from a select environment (prod, test or dev)"
    )
    parser.add_argument(
        "--kontrollera",
        type=str,
        help="Check status of select server name or adress"
    )
    parser.add_argument(
        "--kontrollera-alla",
        action="store_true",
        help="Check status of all select servers"
    )
    parser.add_argument(
        "--export",
        action="store_true",
        help="Export server data to csv file"
    )

    # save CLI args
    return parser.parse_args()

def cli_mode(server_list, args):
    
    if args.lista and args.miljo:
        storage.show_select_server(server_list, args.miljo)
        return

    if args.lista:
        #print("hello from inside args.list")
        storage.show_all_servers(server_list)

    if args.kontrollera:
        #print("hello from inside args.check")
        server = storage.select_server(server_list, args.kontrollera)
        if server == None:
            print(f"\'{args.kontrollera}\' could not be found")
            sys.exit(1)
        sys.exit(statuschecker.update_select_server(server_list, server))

    if args.kontrollera_alla:
        #print("Hello from args.check_all()")
        sys.exit(statuschecker.update_all_servers(server_list))

    if args.export:
        storage.export_data_csv(server_list)
    
