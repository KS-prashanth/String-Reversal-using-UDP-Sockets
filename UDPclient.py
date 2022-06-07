import socket

# Find the reversed string


if __name__ == "__main__":
    host = "127.0.0.1"
    port = 4455
    addr = (host, port)

    def my_function(x):
        return x[::-1]

    """ Creating the UDP socket """
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        data = input("Enter a word: ")
        

        if data == "!EXIT":
            data = data.encode("utf-8")
            client.sendto(data, addr)

            print("Disconneted from the server.")
            break
        
        

        data = data.encode("utf-8")
        client.sendto(data, addr)

        data, addr = client.recvfrom(1024)
        data = data.decode("utf-8")
        data = my_function(data)
        print(f"Server: {data}")