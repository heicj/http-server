import socket

def response_ok():
	return "HTTP/1.1 200 OK"
	
def response_error():
	return "HTTP/1.1 500 Internal Server Error"


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
		
		#print(conn)
		message = b''
		while True:
			data = conn.recv(1)
			
			if data == b'':
				break
			
			if data == b'\n':
				break
				
			message += data
			
		strMessage = message.decode()
		
		
		#ok response
		ok = response_ok()
		error = response_error()
		conn.send(error.encode())
		conn.close()
		
		
		if message.decode() == 'q':
			break
		
	
	
	

server()