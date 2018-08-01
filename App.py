import sys
from PyQt5.QtWidgets import QApplication, QDialog
import MainWindow
import SockClient
from threading import Lock


class App():
    def __init__(self):
        self.client = SockClient.Client(self)
        self.recently_color = (0, 0, 0)
        self._console_lock = Lock()

        self.app = QApplication(sys.argv)
        self._window = MainWindow.MainWindow(self)
        self._window.show()
        sys.exit(self.app.exec_())

    def connect(self):
        if self.client.isConnected is False:
            self.client.connect(self._window.IPLine.text(), int(self._window.PortLine.text()))
            self.writeconsole(str(self.client.textStatus))
            self.writeinfo(str(self.client.textStatus))
            if self.client.isConnected is True:
                self._window.SliderR.setEnabled(True)
                self._window.SliderG.setEnabled(True)
                self._window.SliderB.setEnabled(True)
                self._window.SliderH.setEnabled(True)
                self._window.SliderS.setEnabled(True)
                self._window.SliderV.setEnabled(True)
                self._window.RainbowButton.setEnabled(True)
                self._window.ConnectButton.setText("Rozłącz")
        else:
            self.disconnect()

    def disconnect(self):
        if self.client.isConnected is True:
            self.client.close()
            self.writeconsole(self.client.textStatus)
            self.writeinfo(self.client.textStatus)
            self._window.SliderR.setEnabled(False)
            self._window.SliderG.setEnabled(False)
            self._window.SliderB.setEnabled(False)
            self._window.SliderH.setEnabled(False)
            self._window.SliderS.setEnabled(False)
            self._window.SliderV.setEnabled(False)
            self._window.RainbowButton.setEnabled(False)
            self._window.ConnectButton.setText("Połącz")

    def writeinfo(self, text):
        self._window.InfoLabel.setText(text)

    def writeconsole(self, text):
        self._console_lock.acquire(timeout=0.5)
        text = text.rstrip('\n')
        self._window.TextBrowser.append(text)
        self._console_lock.release()

    def sendcolor(self, red, green, blue):
        if self.recently_color == (red, green, blue):
            return
        self.client.send("COLOR:" + str(red) + "," + str(green) + "," + str(blue))
        self.recently_color = (red, green, blue)

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