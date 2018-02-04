import socket
import sys

debug = True

def request(message):
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
		RESOURCE = '/'
		
		
		
		request = REQUEST + ' ' + RESOURCE + ' ' + VERSION + CRLF
		headers = "host: (0)".format(host) + CRLF
		head = request + headers
		body = message + CRLF
		req = head + CRLF + body
		if debug: print(req)
		return req

def parse_http(message):
	res = message.decode()
	
	
	
def client(message):
	#open a socket to server
	
	#c = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	c = socket.socket()
	if debug: print(c)
	#c.connect( , 5000) #takes a tuple. host name and port
	
	host = socket.gethostname()
	if debug: print(host)
	
	try:
		c.connect((host, 5000))
	except:
		print("connection failed")
	else:
	
		httpMessage = request(message)
		
		c.sendall(httpMessage.encode())
		"""
		if eom == "close":
			c.close()
			return
		elif eom == "LF":
			c.send(str.encode("\n"))
		"""
		
		#raw = c.recv(len(message))
		buffer_length = 8
		message_complete = False
		response = ''
		while not message_complete:
 	
			part = c.recv(buffer_length)
			response += part.decode('utf8')
			if len(part)< buffer_length:
				break
 
				
		message = response
		
		c.close()
		
		print(message)
		return message
		

	
if __name__ == '__main__':
	client(sys.argv[1])