# put all functions in this file
import os
import sys
import time
from constants import *
from socket import *


def print_commands():
    # client commands
    print("=======================================")
    print("| Accepted commands:                  |")
    print("| ftp> get <FILE NAME>                |")
    print("| ftp> put <FILE NAME>                |")
    print("| ftp> ls                             |")
    print("| ftp> quit                           |")
    print("=======================================")


def receive_data(sock, size):
    # receive data until all bytes are received
    return sock.recv(size).decode("utf-8")


def send_data(data, socket):
    data = data.encode("utf-8")
    sentBytes = 0
    # keep sending data from socket until all bytes are received
    while len(data) > sentBytes:
        sentBytes += socket.send(data[sentBytes:])


def put_funcServ(fileName, fileSize, dataServerSocket, dataServerPort):
    while True:
        print("Listening on port " + str(dataServerPort))
        dataClientSocket, addr = dataServerSocket.accept()
        print("Connected to " + addr[0])
        recvBuff = ""
        print(int(fileSize))
        while len(recvBuff) < int(fileSize):
            tmpBuff = receive_data(dataClientSocket, int(fileSize))
            if not tmpBuff:
                break
            recvBuff += tmpBuff
        print("Server Contents of file transferred")
        print(recvBuff)
        dataClientSocket.close()
        break
    path = os.path.dirname(os.path.abspath(__file__)) + '\\server_files' + '\\' + fileName
    f = open(path, "w+")
    f.write(recvBuff)
    f.close()


def put_funcCli(fileName, port):
    server = "127.0.0.1"
    clientDataSocket = socket(AF_INET, SOCK_STREAM)
    clientDataSocket.connect((server, int(port)))
    fileExist = False
    fileObj = ""
    path = os.path.dirname(os.path.abspath(__file__)) + '\\client_files' + '\\' + fileName
    # check if file is in directory
    if os.path.isfile(path):
        fileExist = True
        fileObj = open(path, "r")
        while True:
            fileData = fileObj.read(os.path.getsize(path))
            if fileData:
                send_data(fileData, clientDataSocket)
                print("SUCCESSFULLY CALLED PUT COMMAND.")
            else:
                # breaks loop when done reading file
                break
    else:
        print("FAILURE: File not exist")
    clientDataSocket.close()
    if fileExist:
        fileObj.close()


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
    path = os.path.dirname(os.path.abspath(__file__)) + '\\server_files' + '\\' + fileName
    if os.path.isfile(path):
        fileExist = True
        # Open the file
        fileObj = open(path, "r")

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
                fileData = dataSizeStr
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

    if fileExist:
        fileObj.close()
