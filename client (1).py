
import socket               # Import socket module
def Client():
	s = socket.socket()         
	host = socket.gethostname()
	port = 5188                # Reserve a port for your service.

	s.connect((host, port))
	#m = input("Enter")
	#s.sendall(m.encode())
	m=s.recv(1024)
	print (m)
	
	            # Close the socket when done

if __name__=="__main__":
	Client()
