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
		
		#message = str.encode(message)
		
		request = REQUEST + ' ' + VERSION + CRLF
		headers = "host: (0)".format(host) + CRLF
		head = request + headers
		body = message + CRLF
		req = head + CRLF + body + CRLF
		return req
def parse_http(message):
	return message.body
	
def client(eom, message):
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
	
		message = request(message)
		c.sendall(message.encode())
		
		if eom == "close":
			c.close()
			return
		elif eom == "LF":
			c.send(str.encode("\n"))
		
		raw = c.recv(len(message))
		result = raw.decode()
		
		c.close()
		
		print(result)
		return result
		

	
if __name__ == '__main__':
	if len(sys.argv) <= 2:
		print("client EOM message")
	else:
		client(sys.argv[1], sys.argv[2])