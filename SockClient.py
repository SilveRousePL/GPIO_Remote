import socket
import threading


class Client():
    def __init__(self, app):
        self.sock = None
        self.thread = None
        self._app = app
        self.server_address = None
        self.isConnected = False
        self.textStatus = "Nie połączono"

    def run(self):
        while True:
            try:
                data = self.sock.recv(4096)
            except socket.timeout:
                if self.isConnected is False:
                    break
                continue
            except socket.error:
                break
            if data.decode() is '':
                self._app.disconnected.emit()
                break
            self._app.receivedData.emit(data.decode())

    def connect(self, address, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(0)
        self.sock.settimeout(1)
        self.server_address = (address, port)
        self._app.writeconsole('<i>Connecting with {}:{}...</i>'.format(address, port))
        try:
            self.sock.connect(self.server_address)
            self.isConnected = True
            self.textStatus = "Połączono"
            self.thread = threading.Thread(target=self.run, daemon=1).start()
        except Exception as e:
            self.isConnected = False
            self.textStatus = e
            return

    def send(self, data):
        try:
            self.sock.send(str(data + '\n').encode())
        except Exception:
            self._app.writeconsole("<font color=\"red\">Nie można wysłać polecenia</font>")
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
        return


if __name__ == "__main__":
    client = Client("127.0.0.1", 10000)
    while (True):
        client.send(input())
