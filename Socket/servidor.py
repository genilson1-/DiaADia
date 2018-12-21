import socket
import sys
from _thread import start_new_thread
import time

HOST = '' # all availabe interfaces
PORT = 8888 # arbitrary non privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# bind socket
s.bind((HOST, PORT))
print("[-] Socket Bound to port " + str(PORT))
s.listen(10)
print("Listening...")

def client_thread(conn):
    conn.send(b"Welcome to the Server. Type messages and press enter to send.\n")
    data = conn.recv(1024)
    if (data == b'Ola'):
        while (True):
        # break
            reply = b"OK . . " + data
            conn.send(reply)
            time.sleep(1)
            conn.send(b'teste')
    else:
        conn.send(b'wrong')
        conn.close()
    conn.close()

while True:
    # blocking call, waits to accept a connection
    conn, addr = s.accept()
    print("[-] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,))

s.close()
