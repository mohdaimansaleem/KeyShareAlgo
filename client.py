import socket
import random

HOST = "127.0.0.1"
PORT = 3000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.connect((HOST, PORT))
	key = int(input("Enter key greater than 10:"))
	randnum = random.randrange(1,10)
	key -= randnum
	print("step 1: sending..",key)
	dataSend = key.to_bytes(10,'big')
	s.sendall(dataSend)

	data = s.recv(1024)
	print("step 2: recieving..", data)
	dataSend = int.from_bytes(data, 'big') + randnum
	print("step 3: sending..", dataSend)
	dataSend = dataSend.to_bytes(10,'big')
	s.sendall(dataSend)