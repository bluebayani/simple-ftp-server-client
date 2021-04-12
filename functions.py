# put all functions in this file
import os
import sys
import time


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
    # keep sending data from socket until all bytes are recieved
    while len(data) > sentBytes:
        sentBytes += socket.send(data[sentBytes:])
