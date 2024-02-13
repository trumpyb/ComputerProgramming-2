import rsa
import socket
import threading

public_key, private_key = rsa.newkeys(1024)
DEFAULT_IP_PORT = ("127.0.0.1", 9999)
choice = input("Server or Client (s/c)")

if choice == "s":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(DEFAULT_IP_PORT)
  server.listen()
  print("Waiting for connection")
  client, addr = server.accept()
  print("Connected to", addr)
  client.send(public_key.save_pkcs1())
  public_parter = rsa.PublicKey.load_pkcs1(client.recv(1024))
  print("Use 'Ctrl+C' to disconnect.")
elif choice == "c":
  print("Connecting to server...",end="")
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(DEFAULT_IP_PORT)
  print("Success! Connected to", client.getpeername())
  public_parter = rsa.PublicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1())
  print("Use 'Ctrl+C' to disconnect")
else: exit()

def sendMsg(c):
  while True:
    try:
      msg = input()
      print("\033[1A" + "\033[K", end = "")
      c.send(rsa.encrypt(msg.encode(), public_parter))
      print("\033[91mYou: \033[0m" + msg)
    except: exit()
      
def recvMsg(c):
  while True:
    try:
      msg = rsa.decrypt(c.recv(1024), private_key)
      print("\033[94mPartner: \033[0m" + msg.decode())
    except:
      input("Partner has Disconnected. Press enter to exit")
      exit()

try:
  send_thread = threading.Thread(target=sendMsg, args=(client,)).start()
  recv_thread = threading.Thread(target=recvMsg, args=(client,)).start()
except: pass