import socket
import time
def client():
  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server_ip = 'localhost'
  server_port = 8000 
  server_address = (server_ip, server_port)
  client_socket.connect(server_address)
  print("Connection succesful!")
  try:
    while(1):
      print("Type 'quit' to quit.")
      data = client_socket.recv(80)
      print(f"Server says: {data.decode('utf-8')}")
      keyInput = input("Response: ")

      client_socket.sendall(bytes(keyInput, encoding='utf8'))
      if ((keyInput=='quit') or (keyInput=='Quit')):
        time.sleep(5)
        break
      else: 
         data = client_socket.recv(80)
         print(f"Server says: {data.decode('utf-8')}")
  finally:
      client_socket.close()

client()