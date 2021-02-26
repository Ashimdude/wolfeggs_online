import socket
import time
import os
import sys


sock = socket.socket()
sock.bind(('', 666))
sock.listen(3)
conn1, addr1 = sock.accept()
a = conn1.recv(2048).decode()
if a == "2":
    print("2")
    conn2 = conn1
    conn1, addr1 = sock.accept()
    a = conn1.recv(2048).decode()
elif a == "1":
    print("1")
    conn2, addr2 = sock.accept()
    a = conn2.recv(2048).decode()
gr = True
while gr:
    try:
        planks = conn1.recv(2048)
        wolf = conn2.recv(2048)
        conn2.send(planks)
        conn1.send(wolf)
    except:
        os.execv(sys.executable, ['python'] + sys.argv)
        sys.exit()
