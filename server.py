import os
import os.path
import sys
import socket
from server_functions import *
from client_functions import *
from constants import *
from functions import *

# TO DO: SUCCESS/FAILURE printing, data connection temporary,
# maybe separate the server and client functions

if __name__ == '__main__':
    # EXAMPLE: python3 server.py 12000
    if len(sys.argv) != 2:
        print("USAGE: python3 server.py <PORT>")
        sys.exit()

    commandPort = sys.argv[1]
    dataPort = int(sys.argv[1]) + 1

    # create socket
    commandServerSocket = socket(AF_INET, SOCK_STREAM)
    # bind socket to port
    commandServerSocket.bind(('', int(commandPort)))
    # listen for incoming connections
    commandServerSocket.listen(1)

    # create socket
    dataServerSocket = socket(AF_INET, SOCK_STREAM)
    # bind socket to port
    dataServerSocket.bind(('', int(dataPort)))
    # listen for incoming connections
    dataServerSocket.listen(1)

    if not commandServerSocket:
        print("Failed bind to a port for the command channel")
        sys.exit()
    elif not dataServerSocket:
        print("Failed bind to a port for the data channel")
        sys.exit()
    # keep listening for connections until user ends process
    print("Listening on port " + commandPort + " for commands and port " + str(dataPort) +
          " for data transfers")
    while True:
        dataClientSocket, dataClientAddr = commandServerSocket.accept()
        while True:
            # send the specified <FILE NAME> to the client
            fromDataClient = receive_data(dataClientSocket, 50)
            info_chunks = str(fromDataClient).split(' ')

            if info_chunks[0] == COMMANDS[0]:
                get_funcServ(dataServerSocket, dataPort)
                continue

                # download the specified <FILE NAME> from the client
            elif info_chunks[0] == COMMANDS[1]:
                put_funcServ(info_chunks[1], info_chunks[2],
                             dataServerSocket, dataPort)
                continue

            # TO DO: lists files on server
            elif info_chunks[0] == COMMANDS[2]:
                ls_funcServ(dataClientSocket)
                continue

            # quit command
            elif info_chunks[0] == COMMANDS[3]:
                quit_funcServ(dataClientSocket)
                break
