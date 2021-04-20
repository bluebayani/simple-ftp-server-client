# SERVER FUNCTIONS
import os
import sys
import time
from socket import *
from constants import *
from functions import *


def get_funcServ(dataServerSocket, dataServerPort):
    # print("Listening on port " + str(dataServerPort))
    dataClientSocket, addr = dataServerSocket.accept()
    # print("Connected to " + addr[0])
    fileNameSize = receive_data(dataClientSocket, 10)
    fileNameSize = int(fileNameSize)
    fileName = receive_data(dataClientSocket, fileNameSize)
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
                # Get the size of the data read and convert it to string
                # Prepend 0's to the size string until the size is 10 bytes
                dataSizeStr = prepend_zeros(len(fileData))
                # Prepend the size of the data to the file data.
                fileData = dataSizeStr + fileData
                send_data(fileData, dataClientSocket)
                print("SUCCESS: Called get")
                dataClientSocket.close()
            else:
                # breaks loop when done reading file
                break
    else:
        print("FAILURE: File not exist")
        fileData = ""
        dataSizeStr = prepend_zeros(len(fileData))
        fileData = dataSizeStr
        send_data(fileData, dataClientSocket)
        dataClientSocket.close()
    if fileExist:
        fileObj.close()


def put_funcServ(fileName, fileSize, dataServerSocket, dataServerPort):
    while True:
        dataClientSocket, addr = dataServerSocket.accept()
        recvBuff = ""
        while len(recvBuff) < int(fileSize):
            tmpBuff = receive_data(dataClientSocket, int(fileSize))
            if not tmpBuff:
                break
            recvBuff += tmpBuff
        print("SUCCESS: Called put")
        print("File Name: " + fileName)
        print("File Size: " + str(fileSize))
        print("Content of file:")
        print(recvBuff)
        dataClientSocket.close()
        break
    path = SERVER_FILES + fileName
    f = open(path, "w+")
    f.write(recvBuff)
    f.close()


def get_files():
    # return a variable with the names of the files from ./server_files/
    files = os.listdir(SERVER_FILES)
    # print(files)
    server_files = ""
    if len(files) == 0:
        server_files = "No files on server"
    else:
        for file in files:
            server_files += file + "  "
        server_files = server_files[:-2]
    return server_files


def ls_funcServ(dataClientSocket):
    # get the names of the files on the server
    response = get_files()
    if(response != "No files on server"):
        print("SUCCESS:  Called ls")
    else:
        print("FAILURE: No files on server")
    # Prepend 0's to the size string until the size is 10 bytes
    responseSize = prepend_zeros(len(response))
    # Prepend the size of the data to the file data
    data = responseSize + response
    # send the data to the client
    send_data(data, dataClientSocket)


def quit_funcServ(dataClientSocket):
    print("SUCCESS: Called quit")
    dataClientSocket.close()
