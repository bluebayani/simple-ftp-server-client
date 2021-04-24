# CLIENT FUNCTIONS
import os
import sys
import time
from socket import *
from constants import *
from functions import *


def get_funcCli(data, port, server):
    clientDataSocket = socket(AF_INET, SOCK_STREAM)
    clientDataSocket.connect((server, int(port)))
    # The name of the file
    fileName = data
    # length of fileName to know bytes being sent to server
    fileNameSize = str(len(fileName))
    fileNameStr = prepend_zeros(fileNameSize) + fileName
    # send server the name of the file
    send_data(fileNameStr, clientDataSocket)

    fileData = ""
    # The size of the incoming file
    fileSize = 0
    # The buffer containing the file size
    fileSizeBuff = ""
    # Receive the first 10 bytes indicating the
    # size of the file
    fileSizeBuff = receive_data(clientDataSocket, 10)
    # Get the file size
    fileSize = int(fileSizeBuff)
    # retrieves the data
    fileData = receive_data(clientDataSocket, fileSize)
    if fileSize != 0:
        print("File name: ", fileName)
        print("File size: ", fileSize, "bytes")

        path = CLIENT_FILES + fileName
        f = open(path, "w+")
        f.write(fileData)
        f.close()
        clientDataSocket.close()
    else:
        print("File does not exist in server.")
        clientDataSocket.close()


def put_funcCli(fileName, port, server):
    clientDataSocket = socket(AF_INET, SOCK_STREAM)
    clientDataSocket.connect((server, int(port)))
    fileExist = False
    fileObj = ""
    path = CLIENT_FILES + fileName

    # check if file is in directory
    if os.path.isfile(path):
        fileExist = True
        fileObj = open(path, "r")
        while True:
            fileData = fileObj.read(os.path.getsize(path))
            if fileData:
                send_data(fileData, clientDataSocket)
            else:
                # breaks loop when done reading file
                break
        print("File name: ", fileName)
        print("File size: ", str(os.path.getsize(path)), "bytes")
    else:
        print("File not exist")
    clientDataSocket.close()
    if fileExist:
        fileObj.close()


def ls_funcCli(commandClientSocket):
    # get size of response
    servResponseSize = receive_data(commandClientSocket, 10)

    if servResponseSize == "":
        print("No files in server")
    else:
        servResponse = receive_data(
            commandClientSocket, int(servResponseSize))
        print(servResponse)


def quit_funcCli(commandClientSocket):
    # close the socket
    commandClientSocket.close()
