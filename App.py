import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QObject, pyqtSignal
import MainWindow, MainUI
import SockClient
from threading import Lock


class App(QObject):
    receivedData = pyqtSignal(str)
    disconnected = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.client = None
        self.recently_color = (0, 0, 0)
        # self._console_lock = Lock()

        self.qapp = QApplication(sys.argv)
        self._window = MainWindow.MainWindow(self)
        self.initconn()
        self._window.show()
        sys.exit(self.qapp.exec_())

    def initconn(self):
        self.receivedData.connect(self.recvmessage)
        self.disconnected.connect(self.disconnect)

    def connecttoserver(self):
        self.client = SockClient.Client(self)
        self.client.connect(self._window.IPLine.text(), int(self._window.PortLine.text()))
        self.writeconsole(str(self.client.textStatus))
        self.writeinfo(str(self.client.textStatus))
        if self.client.isConnected is True:
            return True
        else:
            self.client = None
            return False

    def disconnect(self):
        self.client.close()
        self.writeconsole(self.client.textStatus)
        self.writeinfo(self.client.textStatus)
        self.client = None

    def writeinfo(self, text):
        self._window.InfoLabel.setText(text)

    def writeconsole(self, text):
        text = text.rstrip('\n')
        self._window.TextBrowser.append(text)

    def sendcolor(self, red, green, blue):
        if self.recently_color == (red, green, blue):
            return
        self.client.send("COLOR:" + str(red) + "," + str(green) + "," + str(blue))
        self.recently_color = (red, green, blue)

    def sendmessage(self):
        text = self._window.SendLine.text()
        if not text:
            return
        if self.client is None:
            self.writeconsole("<font color=\"red\">Nie można wysłać polecenia</font>")
            return
        self._window.SendLine.clear()
        self.writeconsole("<<< " + text)
        self.client.send(text)

    def recvmessage(self, text):
        self.writeconsole(">>> " + text)

    def setlocalcolor(self):
        text_brightness = "0, 0, 0"
        if self._window.SliderR.value() * 0.299 + self._window.SliderG.value() * 0.687 + self._window.SliderB.value() * 0.114 < 160:
            text_brightness = "255, 255, 255"
        self._window.LocalColor.setStyleSheet(
            "background-color: rgb(" + str(self._window.SliderR.value()) + "," + str(self._window.SliderG.value()) +
            "," + str(self._window.SliderB.value()) + ");\ncolor: rgb(" + text_brightness + ");")

        color_text = '#%02x%02x%02x' % (self._window.SliderR.value(), self._window.SliderG.value(), self._window.SliderB.value())
        self._window.LocalColor.setText("<html><head/><body><p>" + color_text + "</p></body></html>")

if __name__ == "__main__":
    app = App()