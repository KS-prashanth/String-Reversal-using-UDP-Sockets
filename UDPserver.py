
import socket

# Find the reversed string
def my_function(x):
  return x[::-1]

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    print("SERVER STARTED ")
    """ Creating the UDP socket """
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    """ Bind the host address with the port """
    server.bind((host, port))

    while True:
        data, addr = server.recvfrom(1024)
        data = data.decode("utf-8")
        print(f"The Enterd data is {data}")

        if data == "!EXIT":
            print("Client disconnected.")
            break
        
        data = data.encode("utf-8")
        server.sendto(data, addr)

        data = my_function(data)  
        print(f"Client: {data}")

       