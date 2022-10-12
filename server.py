import socket
import random
from _thread import *

def client_handler(conn,addr):
	with conn:
		randnum = random.randrange(1,10)
		key = -1
		data = conn.recv(1024)
		data = int.from_bytes(data, 'big')
		key = data + randnum
		temp = weight - randnum
		dataSend = temp.to_bytes(10, 'big')
		conn.sendall(dataSend)
		print("step 2: sending..", dataSend)
		data = conn.recv(1024)
		data = int.from_bytes(data,'big')
		key += data
		key -= weight
		print(f"key of {addr} is:{key}")

def accept_connections(ServerSocket):
    conn, addr = ServerSocket.accept()
    print("Connected to ",addr)
    start_new_thread(client_handler, (conn, addr)) 

HOST = "127.0.0.1"
PORT = 3000
weight = 15

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	while True:
		accept_connections(s)
		

