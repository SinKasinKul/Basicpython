import time
import socket 
s = socket.socket()          
s.connect(('10.0.112.165', 9004)) 
s.settimeout(1000)
s.send(b"LON\r")
time.sleep(1)
s.send(b"LOFF\r")



print(s.recv(1024).decode('utf-8'))
s.close()