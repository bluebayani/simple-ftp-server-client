# put all functions in this file
import os
import sys
import time
from constants import *


def print_commands():
    # client commands
    print("=======================================")
    print("| Accepted commands:                  |")
    print("| ftp> get <FILE NAME>                |")
    print("| ftp> put <FILE NAME>                |")
    print("| ftp> ls                             |")
    print("| ftp> quit                           |")
    print("=======================================")


def receive_data(socket, size):
    # receive data until all bytes are received
    return socket.recv(size).decode("utf-8")


def send_data(data, socket):
    data = data.encode("utf-8")
    sentBytes = 0
    # keep sending data from socket until all bytes are recieved
    while len(data) > sentBytes:
        sentBytes += socket.send(data[sentBytes:])


def prepend_zeros(data):
    # Get the size of the data read and convert it to string
    data = str(data)
    # Prepend 0's to the size string until the size is 10 bytes
    while len(data) < 10:
        data = "0" + data
    return data


def get_files():
    # return a variable with the names of the files from ./server_files/
    files = os.listdir(SERVER_FILES)
    server_files = ""
    for file in files:
        server_files += file + "  "
    server_files = server_files[:-2]
    return server_files


def get_funcCli(data, cliSocket):

    # The name of the file
    fileName = data

    # send server the name of the file
    send_data(fileName, cliSocket)

    fileData = ""

    # The size of the incoming file
    fileSize = 0

    # The buffer containing the file size
    fileSizeBuff = ""

    # Receive the first 10 bytes indicating the
    # size of the file
    fileSizeBuff = receive_data(cliSocket, 10)

    # Get the file size
    fileSize = int(fileSizeBuff)

    if fileSize != 0:
        print("The file size is", fileSize, "bytes transferred")

        print("File name is ", fileName)
    else:
        print("File does not exist in server.")


def get_funcServ(fileName, cliSocket):
    fileExist = False
    # check if file is in directory
    if os.path.isfile(SERVER_FILES + fileName):
        fileExist = True
        # Open the file
        fileObj = open(SERVER_FILES + fileName, "r")
        # The number of bytes sent
        numSent = 0
        # The file data
        fileData = None

        # Keep sending until all is sent
        while True:

            # Read 65536 bytes of data
            fileData = fileObj.read(65536)

            # Make sure we did not hit EOF
            if fileData:

                # Get the size of the data read
                # and convert it to string
                dataSizeStr = str(len(fileData))

                # Prepend 0's to the size string
                # until the size is 10 bytes
                while len(dataSizeStr) < 10:
                    dataSizeStr = "0" + dataSizeStr

                # Prepend the size of the data to the
                # file data.
                fileData = dataSizeStr + fileData
                send_data(fileData, cliSocket)
                print("SUCCESSFULLY CALLED GET COMMAND.")
            else:
                # breaks loop when done reading file
                break

    else:
        print("FAILURE: File not exist")
        fileData = ""
        dataSizeStr = str(len(fileData))

        # Prepend 0's to the size string
        # until the size is 10 bytes
        while len(dataSizeStr) < 10:
            dataSizeStr = "0" + dataSizeStr
        fileData = dataSizeStr
        send_data(fileData, cliSocket)

    if fileExist == True:
        fileObj.close()
