import os
import sys
import socket
from constants import *
from functions import *


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
        print("Listening on port " + port)
        cliSocket, addr = servSocket.accept()
        print("Connected to " + addr[0])

        while True:
            # get command from client socket
            fromClient = cliSocket.recv(40).decode("utf-8")

            # TO DO: send the specified <FILE NAME> to the client
            if fromClient == COMMANDS[0]:
                print("SUCCESSFULLY CALLED GET COMMAND.")

            # TO DO: download the specified <FILE NAME> from the client
            elif fromClient == COMMANDS[1]:
                print("SUCCESSFULLY CALLED PUT COMMAND.")

            # ls: lists files on server
            elif fromClient == COMMANDS[2]:
                print("SUCCESS. ls command invoked...")

                # get the names of the files on the server
                response = get_files()
                # Prepend 0's to the size string until the size is 10 bytes
                responseSize = prepend_zeros(len(response))
                # Prepend the size of the data to the file data
                data = responseSize + response
                # send the data to the client
                send_data(data, cliSocket)

            # quit: close the connection
            elif fromClient == COMMANDS[3]:
                cliSocket.close()
                print("SUCCESS. Connection closed...")
                break
