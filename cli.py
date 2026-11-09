import sys
import storage
import argparse
import statuschecker
import menu

def cli_args():
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

    # save CLI args
    return parser.parse_args()

def cli_mode(server_list, args):
    
    if args.list and args.environment:
        menu.show_select_server(server_list, args.environment)
        return

    if args.list:
        #print("hello from inside args.list")
        menu.show_all_servers(server_list)

    if args.check:
        #print("hello from inside args.check")
        server = menu.select_server(server_list, args.check)
        if server == None:
            print(f"\'{args.check}\' could not be found")
            sys.exit(1)
        sys.exit(statuschecker.update_select_server(server_list, server))

    if args.check_all:
        #print("Hello from args.check_all()")
        sys.exit(statuschecker.update_all_servers(server_list))

    if args.export:
        storage.export_data_csv(server_list)
    
