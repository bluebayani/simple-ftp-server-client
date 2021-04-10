import os
import sys
import socket

COMMANDS = ["get", "put", "ls", "quit"]

if __name__ == '__main__':
    # EXAMPLE: python3 client.py <your ip address> 12000
    if len(sys.argv) != 3:
        print("USAGE: python3 client.py <SERVER> <PORT>")
        sys.exit()

    server = sys.argv[1]
    port = sys.argv[2]

    # create socket
    cliSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to server
    cliSocket.connect((server, int(port)))
    print("Connected to " + server + " on port " + str(port))

    # cannot connect
    if not cliSocket:
        print("Failed to connect to " + server)
        sys.exit()

    buffer = ""

    while True:
        buffer = (input("ftp> ")).lower().split()
        # EXAMPLE: ftp> ls text.txt
        # buffer = ['ls', 'text.txt']

        # perform the appropriate client side action
        # TO DO: check if buffer[0] == COMMANDS[0] "get"
        # TO DO: check if buffer[0] == COMMANDS[1] "put"
        # TO DO: check if buffer[0] == COMMANDS[2] "ls"
        # TO DO: check if buffer[0] == COMMANDS[3] "quit"
