#!usr/bin/python3
import socket

def Main():
	host = '127.0.0.1'
	port = 8080

	s = socket.socket()
	s.bind((host, port))

	s.listen(1)
	c, addr = s.accept()
	print ("Connection from: " + str(addr))
	while True:
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		print ("from connected user: " + data)
		data = data.upper()
		#send back the capitalized data to client
		print ("sending: " + data)
		c.send(data.encode('utf-8'))
	c.close()

if __name__ == '__main__':
	Main()


