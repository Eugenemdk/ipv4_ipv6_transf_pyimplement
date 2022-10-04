import socket
def server():
    port=3000
    host=socket.gethostname()
    #server_socket=socket.socket(socket.AF_INET6)
    server_socket=socket.create_server(("",3000),family=socket.AF_INET6,dualstack_ipv6=True)        
    #bind host and port together
    #server_socket.bind((host,port))
    #define how many client erver can listen to simultaniously
    server_socket.listen(3)
    conn,address=server_socket.accept()
    print(f"Server's ip address:{str(address)}\n")
    print(f"Connection from : {str(address)}")
    while(True):
        #receive buffer
        data = conn.recv(1024).decode()
        if not data:
            break
        else:
            print(f"From connected user: {str(data)}")
            data=input("->")
            conn.send(data.encode())
    conn.close()
    
if __name__ == "__main__":
    server()
