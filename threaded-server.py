### --- Multi - Threading Server --- ###

import socket, os
import threading
import subprocess
import pickle

def convert_to_secs(time):															#should be of format HH:MM:SS
    t = time.split(':')
    if int(t[0])<7:
    	hours = 17 + int(t[0])
    	mins = hours*60 + int(t[1])
    	return mins*60 + int(t[2])
    hours = abs(int(t[0]) - 7)
    mins = hours*60 + int(t[1])
    return mins*60 + int(t[2])

def roundoff(time):
	return 15 * round(time/15)														#approximated to 15 secs, change number to your fitting

class clientThread(threading.Thread):
    def __init__(self,host,port,addr,conn):
        threading.Thread.__init__(self)
        self.host=host
        self.port=port
        self.addr=addr
        self.conn=conn

    def run(self):
        print("Connected: ",self.addr)
        self.request = self.conn.recv(1048).decode('utf8').split(' ')
       	print(self.request)
        time = self.request[0]
       	location = self.request[1]												#Change path of excel files here. append it before location as per your structure.
       	time = convert_to_secs(time)
       	time = roundoff(time)
       	print(time)
       	print("Location found out to be "+location)
       	print("Getting information...")
       	#os.system("python3 "+location+".py {}",time)
       	res = subprocess.check_output(['python3',location+'.py',str(time)])
       	res = res.decode('utf-8')
       	res = res[2:].rstrip(']]\n').split(', ')
       	#res = list(map(lambda x: float(x), res))
       	data = pickle.dumps(res)
       	self.conn.send(data)
       	print("Values sent!")
       	print("Closing connection")
       	self.conn.close()



if __name__ == '__main__':
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host='127.0.0.1'
    while True:
        port=8888	#feel free to change it
        try:
            s.bind((host,port))
            break
        except socket.error as e:
            print("Port number is taken or an error occured!")
            continue

    s.listen(10)
    print("Server is up and listening for incoming connections!")
    while True:
        conn,addr = s.accept()
        thread = clientThread(host,port,addr,conn)
        thread.start()
