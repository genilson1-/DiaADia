# -*- coding: utf-8 -*-
import socket
import time

def enviaOla():

    HOST = '127.0.0.1'
    PORT = 8888
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    msg ="Olá"
    tcp.send(b"Ola")
    while(True):
        data = tcp.recv(1024)
        print(data)

    # tcp.close()

print('comeca a enviar')
enviaOla()
