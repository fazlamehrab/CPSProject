import socket, os, pickle

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = 'localhost'              #Change to the server ip
	port = 8888						#use server port number
	time = input("Time: ")
	location = input("Location: ")	#tln where n is a number(1,2,3)
	s.connect((host,port))
	print("Connected to: "+str(s.getpeername()[0])+"::"+str(s.getpeername()[1]))
	s.send((time+" "+location).encode())
	res = s.recv(4096)
	res = pickle.loads(res)
	res = list(map(lambda x: str(x), res))
	print("Cars in system: "+res[0])
	print("Stops count per car: "+res[1])
	print("Average time in system, seconds: "+res[2])
	print("Average speed, km/hr: "+res[3])
	s.close()
	print("Connection terminated!")

