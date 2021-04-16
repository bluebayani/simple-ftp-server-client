import os
import os.path
import sys
import socket
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

    while True:
        # keep listening for connections until user ends process
        print("Listening on port " + commandPort + " for commands and port " + str(dataPort) +
              " for data transfers")
        dataClientSocket, dataClientAddr = commandServerSocket.accept()
        print("Connected to " + dataClientAddr[0])
        while True:
            # get command from data client socket
            fromDataClient = receive_data(dataClientSocket, 50)
            info_chunks = str(fromDataClient).split(' ')
            # TO DO: send the specified <FILE NAME> to the client
            if info_chunks[0] == COMMANDS[0]:
                # Receive file name from client
                fileName = receive_data(dataClientSocket, 10)
                get_funcServ(fileName, dataClientSocket)
                continue

                # TO DO: download the specified <FILE NAME> from the client
            elif info_chunks[0] == COMMANDS[1]:
                put_funcServ(info_chunks[1], info_chunks[2], dataServerSocket, dataPort)
                print("SUCCESSFULLY CALLED PUT COMMAND.")
                continue

            # TO DO: lists files on server
            elif info_chunks[0] == COMMANDS[2]:
                print("SUCCESSFULLY CALLED LS COMMAND.")

            # quit command
            elif info_chunks[0] == COMMANDS[3]:
                dataClientSocket.close()
                print("SUCCESSFULLY CALLED QUIT COMMAND. Connection closed...")
                break
