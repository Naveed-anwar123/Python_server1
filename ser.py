'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
c=[] 

HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5188 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    sys.exit()
     
print('Socket bind complete')
 
s.listen(2)
print('Socket now listening')
 
def server():
	count=0
	def clientthread(conn):
  	   
	    conn.send('Welcome to the server. Type something and hit enter\n----->') #send only takes string
	    while True:
		    data = c[1].recv(1024)
		    reply = 'Client1...' + data
		    if not data: 
		    	break
		     
		    c[0].sendall(reply)
	    conn.close()

	def clientthread1(conn):

	    conn.send('Welcome to the server. Type something and hit enter\n----->')
	    while True:
		data = c[0].recv(1024)
                reply = 'Client2...' + data
		if not data: 
		    break
	     
		c[1].sendall(reply)
	    conn.close()
	while 1:
	    conn, addr = s.accept()
	    count=count+1
	    print ('Connected with ' + addr[0] + ':' + str(addr[1]))
	    if conn not in c:
	    	c.append(conn)
		print (count)
	    if(count==2):
	    	start_new_thread(clientthread , (c[0],))	
	    	start_new_thread(clientthread1 ,(c[1],))
	s.close()

if __name__=="__main__":
	server()

