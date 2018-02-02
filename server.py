import socket


def server():
	#start server running
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	s = socket.socket()
	host = socket.gethostname()
	address = (host, 5000)
	s.bind(address)
	
	s.listen(1)
	while True:
		conn, addr = s.accept()
		print(conn)
	
		buffer_length = 8
		message_complete = False
		while not message_complete:
			
			part = conn.recv(buffer_length)
			response = part.decode('utf8')
			if len(part)< buffer_length:
				break
		
		message = response.encode('utf8')
		print(message)
		conn.send(message)


server()