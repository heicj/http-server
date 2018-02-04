import socket

RootDir = r"C:\Users\Charlie\Documents\code401\serverExample\webroot\webroot\webroot"


def response_ok():
	return "HTTP/1.1 200 OK"
	
def response_error():
	return "HTTP/1.1 500 Internal Server Error"

def openFile(path):
	import io
	#path = r"\sample.txt"
	f = open(RootDir + path)
	text = f.read()
	size = len(text)
	#print(size)
	
	#print(text)
	return text, size
	
def resolve_uri(path):
	data, size = openFile(path)
	CRLF = "\r\n"
	Host = "Host: 0"
	
	#data has the string of text from file
	#size has size
	#run response_ok function to get http first line
	ok = response_ok()
	header = "Host: (0), Size: (1)".format(Host, size) + CRLF
	packet = ok + CRLF + header + data + CRLF
	print(data)
	print(size)
	return packet


	
def parse_request(message):
	#takes byte string request and parses it
	str = message.decode()
	parts = str.split('\r\n')
	req = parts[0].split(' ')
	
	reqType = req[0]  #first part is GET
	resource = req[1] #gets resource part
	version = req[2] #gets version type
	host = parts[1] #gets host as host: (0)
	hostParts = host.split(' ')
	body = parts[3] #contains body content
	
	response = resource
	
	if reqType != "GET":
		response = "Not a GET request"
	
	if version != "HTTP/1.1":
		response = "version not supported"
	
	if hostParts[0] != 'host:':
		response = "Host not sent"
		
	return response



debug = False

def server():
	#start server running
	
	s = socket.socket()
	host = socket.gethostname()
	address = (host, 5000)
	s.bind(address)
	
	s.listen(1)
	
	
		
	while True:
		conn, addr = s.accept()

		if debug: print(conn)

		
		buffer_length = 8
		message_complete = False
		response = b''
		while not message_complete:
 	
			part = conn.recv(buffer_length)
			response += part
			if len(part)< buffer_length:
				break
 
				
		message = response
		
		#returns resource (file ext) from get request
		resource = parse_request(message)
		
		#runs openFile function using path 
		#openFile(resource)
		
		packet = resolve_uri(resource)
		
		strMessage = message.decode()
		
		#currently sends back resource path requested
		conn.send(packet.encode())
		print(resource)
		#openFile()
		
		
		#ok response
		if strMessage == "testOK":
			ok = response_ok()
			conn.send(ok.encode())
		
		#test sending error response
		if strMessage == "testError":
			error = response_error()
			conn.send(error.encode())
		
		conn.close()
		
		
		if message.decode() == 'q':
			break
		
	
	
	

server()