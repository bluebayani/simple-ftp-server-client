import os
import sys
import socket

COMMANDS = ["get", "put", "ls", "quit"]

if __name__ == '__main__':
    # EXAMPLE: python3 server.py 12000
    if len(sys.argv) != 2:
        print("USAGE: python3 server.py <PORT>")
        sys.exit()

    port = sys.argv[1]

    # create socket
    servSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind socket to port
    servSocket.bind(('', int(port)))
    # listen for incoming connections
    servSocket.listen(1)

    # cannot bind
    if not servSocket:
        print("Failed bind to a port")
        sys.exit()

    while True:
        # keep listening for connections until user ends process
        print("Listening on port... " + port)
        cliSocket, addr = servSocket.accept()
        print("Connected to... " + addr[0])

        # need to get the buffer from the client and perform the appropriate serverside action
        # TO DO: check if buffer[0] == COMMANDS[0] "get"
        # TO DO: check if buffer[0] == COMMANDS[1] "put"
        # TO DO: check if buffer[0] == COMMANDS[2] "ls"
        # TO DO: check if buffer[0] == COMMANDS[3] "quit"
