import socket
import threading

class Client():
    def __init__(self):
        self.sock = None
        self.thread = None
        self.server_address = None
        self.isConnected = False
        self.textStatus = "Nie połączono"

    def run(self):
        while self.isConnected:
            data = self.sock.recv(32)
            if data:
                print(data.decode())

    def connect(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (address, port)
        try:
            self.sock.connect(self.server_address)
            self.isConnected = True
            self.textStatus = "Połączono"
            self.thread = threading.Thread(target=self.run).start()
        except Exception as e:
            self.isConnected = False
            self.textStatus = e
            return

    def send(self, data):
        try:
            self.sock.sendall(str(data + '\n').encode())
        except socket.error:
            return False
        return True

    def close(self):
        try:
            self.sock.close()
            self.textStatus = "Zakończono połączenie"
        except Exception as e:
            self.textStatus = e
        self.isConnected = False
        self.server_address = None
        self.thread = None
        self.sock = None
        return

if __name__ == "__main__":
    client = Client("127.0.0.1", 10000)
    while (True):
        client.send(input())
