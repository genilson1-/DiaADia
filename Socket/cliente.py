# -*- coding: utf-8 -*-
import socket
import time

def recebeOla():

    HOST = ''              # Endereco IP do Servidor
    PORT = 8000            # Porta que o Servidor esta
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    con, cliente = tcp.accept()
    while True:
        msg = con.recv(1024)
        if not msg: break
        if (msg == "Ola"):
            con.close()
            return True
        else:
            return False

def enviaMsg():
    HOST = '127.0.0.1'
    PORT = 9000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)
    tcp.connect(dest)
    while(True):
        tcp.send(b"Foi, deu certo")
        time.sleep(1)

    tcp.close()

while (not recebeOla()):
    print('ainda nao')
    time.sleep(1)

print('comeca a enviar')
enviaMsg()
