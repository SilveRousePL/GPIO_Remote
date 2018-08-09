import socket
import threading
import time


class Server():
    def __init__(self, port):
        self.sock = None
        self.server_address = ('localhost', port)  # Bind the socket to the port
        self.thread = threading.Thread(target=self.run, daemon=1).start()

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
        print('Starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)
        self.sock.listen(1)  # Listen for incoming connections

        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            print(type(connection), client_address)
            try:
                print('connection from', client_address)
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(4096)
                    print('received {!r}'.format(data))
                    if data:
                        print('sending data back to the client')
                        connection.sendall(data)
                    else:
                        print('no data from', client_address)
                        break

            finally:
                # Clean up the connection
                connection.close()

if __name__ == "__main__":
    server = Server(10000)
    while True:
        time.sleep(1)
