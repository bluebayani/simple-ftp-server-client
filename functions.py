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
