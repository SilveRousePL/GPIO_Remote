import socket
import threading

class Server():
    def __init__(self, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP/IP socket
        self.server_address = ('localhost', port)  # Bind the socket to the port
        self.thread = threading.Thread(target=self.run).start()

    def run(self):
        print('starting up on {} port {}'.format(*self.server_address))
        self.sock.bind(self.server_address)
        self.sock.listen(1)  # Listen for incoming connections
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = self.sock.accept()
            try:
                print('connection from', client_address)
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
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
