import socket

def response_ok(message):
		"""header
			request
			headers
			<crlf>
			message
			<crlf>
		"""
		host = socket.gethostname()
		REQUEST = "GET"
		VERSION = "HTTP/1.1"
		CRLF = "\r\n"
		OK = "200 OK"
		
		#message = str.encode(message)
		
		response = REQUEST + ' ' + VERSION + ' ' + OK + CRLF
		headers = "host: (0)".format(host) + CRLF
		head = response + headers
		body = message + CRLF
		return head + CRLF + body + CRLF


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
		"""message = b''
		while True:
			data = conn.recv(1)
			
			if data == b'':
				break
			
			if data == b'\n':
				break
				
			message += data
			
		strMessage = message.decode()
		httpResponse = response_ok(strMessage)	
		
		conn.send(httpResponse.encode())
		conn.close()
		
		if message.decode() == 'q':
			break"""
		
	
	
	

server()