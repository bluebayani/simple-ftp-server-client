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
    serverPort = sys.argv[2]

    # create socket
    commandClientSocket = socket(AF_INET, SOCK_STREAM)
    # connect to server socket
    commandClientSocket.connect((server, int(serverPort)))
    print("Connected to " + server + " on data port " + str(serverPort))
    print_commands()

    # cannot connect
    if not commandClientSocket:
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
            print("GET")
        #    The name of the file
        #    fileName = buffer[1]
        #    get_funcCli(fileName, commandClientSocket)

        # upload the specified <FILE NAME> to the server
        # WORK ON HERE
        elif buffer[0] == COMMANDS[1]:
            path = os.path.dirname(os.path.abspath(__file__)) + '/client_files' + '/' + buffer[1]
            info = buffer[0] + " " + buffer[1] + " " + str(os.path.getsize(path))
            send_data(info, commandClientSocket)
            put_funcCli(buffer[1], int(serverPort)+1)

        # print list of files on the server
        elif buffer[0] == COMMANDS[2]:
            send_data(buffer[0], commandClientSocket)
            print("SUCCESSFULLY CALLED LS COMMAND.")

        # quit command
        elif buffer[0] == COMMANDS[3]:
            send_data(buffer[0], commandClientSocket)
            # close the socket
            commandClientSocket.close()
            print("SUCCESSFULLY CALLED QUIT COMMAND. Connection closed...")
            break
        else:
            print(buffer[0] + " is an invalid command.")
            print_commands()
