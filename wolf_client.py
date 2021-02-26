import socket
import time
import pygame
sock = socket.socket()
gr = True
wx = 0
wy = 0
planks = "000 000 000 000"
pygame.init()
size = width, height = 200, 200
screen = pygame.display.set_mode(size)
screen2 = pygame.Surface(screen.get_size())
if input() == "1":
    sock.connect(('localhost', 666))
    sock.send("1".encode())
    while gr:
        time.sleep(0.2)
        sock.send(planks.encode())
        f = sock.recv(2048).decode().split()
        wx = int(f[0])
        wy = int(f[1])
        print(wx, wy)
        for event in pygame.event.get():
            pks = planks.split()
            time.sleep(1)
            if event.type == pygame.QUIT:
                gr = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("1")
                    if "0" in pks[0]:
                        if pks[0].find("0") == 0:
                            pks[0] = "1" + pks[0][pks[0].find("0") + 1:]
                        elif pks[0].find("0") == 1:
                            pks[0] = pks[0][0] + "1" + pks[0][2]
                        elif pks[0].find("0") == 2:
                            pks[0] = pks[0][0] + pks[0][1] + "1"
                elif event.key == pygame.K_2:
                    if "0" in pks[1]:
                        if pks[1].find("0") == 0:
                            pks[1] = "1" + pks[1][pks[1].find("0") + 1:]
                        elif pks[1].find("0") == 1:
                            pks[1] = pks[1][0] + "1" + pks[1][2]
                        elif pks[1].find("0") == 2:
                            pks[1] = pks[1][0] + pks[1][1] + "1"
                elif event.key == pygame.K_3:
                    if "0" in pks[2]:
                        if pks[2].find("0") == 0:
                            pks[2] = "1" + pks[2][pks[2].find("0") + 1:]
                        elif pks[0].find("0") == 1:
                            pks[2] = pks[2][0] + "1" + pks[2][2]
                        elif pks[2].find("0") == 2:
                            pks[2] = pks[2][0] + pks[2][1] + "1"
                elif event.key == pygame.K_4:
                    if "0" in pks[3]:
                        if pks[3].find("0") == 0:
                            pks[3] = "1" + pks[3][pks[3].find("0") + 1:]
                        elif pks[3].find("0") == 1:
                            pks[3] = pks[3][0] + "1" + pks[3][2]
                        elif pks[3].find("0") == 2:
                            pks[3] = pks[3][0] + pks[3][1] + "1"
            planks = " ".join(pks)
elif input() == "2":
    sock.connect(('localhost', 666))
    sock.send("2".encode())
    sock.send("2".encode())
    while gr:
        time.sleep(0.2)
        sock.send((str(wx) + " " + str(wy)).encode())
        planks = sock.recv(2048).decode()
        print(planks)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gr = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    print("l")
                elif event.key == pygame.K_RIGHT:
                    print("r")
                elif event.key == pygame.K_DOWN:
                    print("d")
                elif event.key == pygame.K_UP:
                    print("u")
