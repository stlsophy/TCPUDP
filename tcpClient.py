#!usr/bin/python3
import socket

def Main():
	host = '127.0.0.1'
	port = 8080

	s = socket.socket()
	#connect to server
	s.connect((host, port))

	message = input("->")
	while message !='q':
		s.send(message.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		print ("Received from server: " + data)
		message = input("->")
	s.close()

if __name__ == '__main__':
	Main()


