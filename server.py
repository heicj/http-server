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
		message = b''
		while True:
			data = conn.recv(1)
			
			if data == b'':
				break
			
			if data == b'\n':
				break
				
			message += data
			
		conn.send(message)
		conn.close()
		
		if message.decode() == 'q':
			break
		
	
	
	

server()