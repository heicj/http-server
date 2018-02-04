import socket


def response_ok():
	return "HTTP/1.1 200 OK"
	
def response_error():
	return "HTTP/1.1 500 Internal Server Error"


	
def parse_request(message):
	#takes byte string request and parses it
	str = message.decode()
	parts = str.split('\r\n')
	req = parts[0].split(' ')
	
	reqType = req[0]  #first part is GET
	resource = req[1] #gets resource part
	version = req[2] #gets version type
	host = parts[1] #gets host as host: (0)
	body = parts[3] #contains body content
	
	if reqType != "GET":
		raise NotImplementedError('Not a GET request')
	
	if version != "HTTP/1.1":
		raise Exception("version not supported")
	
	if host == None:
		raise Exception("Host not sent")
		
	return resource
	#print(req[0]) #first part is GET
	#print(req[1]) #second part is resource
	#print(req[2]) #3rd part is version
	#print('whole thing: ', parts) #prints out whole request along with body
	#print('get request: ', parts[0]) #prints out whole request line
	#print('host: ', parts[1]) #prints host  host: (0)
	#print('body : ', parts[3]) #prints body
	
	
	
	#only accept GET requests other requests should raise appropriate python exception
	
	#only accept http/1.1 requests other wise raise exception
	
	#validate host header if not raise exception
	
	#validate message is well formed else raise exception
	
	#if no exceptions should return URI from the request


debug = False

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
		httpMessage = parse_request(message)
		strMessage = message.decode()
		conn.send(httpMessage.encode())
		print(httpMessage)
		
		
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