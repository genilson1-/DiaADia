# -*- coding: utf-8 -*-
import socket

def enviaOla():

    HOST = '127.0.0.1'
    PORT = 8000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    msg ="Olá"
    tcp.send(b"Ola")
    tcp.close()

def recebeDados():

    HOST = ''              # Endereco IP do Servidor
    PORT = 9000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    con, cliente = tcp.accept()
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(msg)

enviaOla()
recebeDados()
