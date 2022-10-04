import socket
def client():
    port=3000
    host=socket.gethostname()
    client_socket=socket.socket(socket.AF_INET)
    client_socket.connect((host,port))
   
    message=input("->")
    
    while message.lower().strip()!="bye":
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print(f"Received from server: {str(data)}")
        message=input("->")
        
    client_socket.close()

if __name__ =='__main__':
    client()