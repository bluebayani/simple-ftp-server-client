import os
import sys
import socket
from constants import *
from functions import *

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
    print_commands()

    # cannot connect
    if not cliSocket:
        print("Failed to connect to " + server)
        sys.exit()

    buffer = ""

    while True:
        buffer = (input("ftp> ")).lower().split()
        # EXAMPLE: ftp> ls text.txt
        # buffer = ['ls', 'text.txt']
        # buffer[0] -> command
        # buffer[1] -> file name

        # download the specified <FILE NAME> from the server
        if buffer[0] == COMMANDS[0]:
            if len(buffer) == 2:
                send_data(buffer[0], cliSocket)
                # The name of the file
                fileName = buffer[1]
                get_funcCli(fileName, cliSocket)
            else:
                print("USEAGE: get <file name>")

        # upload the specified <FILE NAME> to the server
        elif buffer[0] == COMMANDS[1]:
            send_data(buffer[0], cliSocket)
            print("SUCCESSFULLY CALLED PUT COMMAND.")

        # print list of files on the server
        elif buffer[0] == COMMANDS[2]:
            send_data(buffer[0], cliSocket)
            # get size of response
            servResponseSize = receive_data(cliSocket, 10)

            if servResponseSize == "":
                print("FAILURE")
            else:
                print("SUCCESS: ls command invoked...")
                servResponse = receive_data(cliSocket, int(servResponseSize))
                print(servResponse)

        # quit command
        elif buffer[0] == COMMANDS[3]:
            send_data(buffer[0], cliSocket)
            # close the socket
            cliSocket.close()
            print("SUCCESS: Connection closed...")
            break
        else:
            print(buffer[0] + " is an invalid command.")
            print_commands()
