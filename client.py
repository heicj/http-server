import socket
import sys
def client(message):
	#open a socket to server
	
	c = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
	#c.connect( , 5000) #takes a tuple. host name and port
	
	host = socket.gethostname()
	try:
		c.connect((host, 5000))
	except:
		print("connection failed")
	else:
		c.sendall(message.encode('utf8'))
	
	
	response = c.recv(len(message))
	print(response)
	return response
	#send message passed as argument to server
	
	#accumulate any reply sent by server into string
	#once recieved, close the socket
	#return message
	
if __name__ == '__main__':
	client(sys.argv[1])