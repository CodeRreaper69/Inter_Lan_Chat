#server.py
import sys
import socket


print("WELCOME TO INTER-LAN SECRET COMMUNICATION SERVICES\n")



# SERVER = "127.0.0.1"
#SERVER = "192.168.29.161"
SERVER = input("ENTER YOUR UNIQUE ADDRESS: ")
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
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER, PORT))

s.listen(5)

while True:
    print(f"[>] listening as {SERVER}:{PORT}")

    client = s.accept()
    print(f"[>] client connected {client[1]}")

    client[0].send("conected".encode())

    while True:
        cmd = input('>>> ')
        client[0].send(cmd.encode())

        if cmd.lower() in ['quit','exit', 'q', 'x']:
            break

        result = client[0].recv(1024).decode()
        print(result)

    client[0].close()

    cmd = input("wait for new client y/n: ")

    if cmd.lower() in ['n','no']:
        exit()


s.close()
