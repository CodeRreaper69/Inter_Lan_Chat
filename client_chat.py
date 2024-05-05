import sys
import subprocess
import socket
import time


print("WELCOME TO INTER-LAN SECRET COMMUNICATION SERVICES\n")



# SERVER = "127.0.0.1"
#SERVER = "192.168.29.161"
SERVER = input("ENTER UNIQUE ADDRESS OF YOUR FRIEND: ")
print("\n")
ch = input("HAS YOUR FRIEND STARTED CHATTING?(y/n) ")
print("\n")
ch1 = input("ARE YOU BOTH ON THE SAME WIFI?(y/n) ")
print("\n")
if ch == "y" and ch1 == "y":
   print("START CHATTING")
   
else:
   print("Exiting in few Seconds")
   time.sleep(5)
   exit()

PORT = 4444

s = socket.socket()
s.connect((SERVER, PORT))

# Receive initial message from server
msg = s.recv(1024).decode()
print('[*] Server:', msg)

while True:
    # Prompt the user for a command
    user_input = input("[>] ")

    if user_input.lower() in ['q', 'quit', 'exit', 'x']:
        s.send(user_input.encode())
        break

    # Send the command to the server
    s.send(user_input.encode())

    # Receive and display the result from the server
    result = s.recv(4096).decode()  # Adjust buffer size as needed
    print(result)

s.close()

