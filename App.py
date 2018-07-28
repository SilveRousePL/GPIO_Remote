import sys
# from MainWindow import MainWindow
import SockClient

class App():
    def __init__(self, window):
        self.window = window
        self.client = SockClient.Client()
        self.recently_color = (0,0,0)

    def connect(self):
        if self.client.isConnected == True:
            self.client.close()
            self.writeConsole(self.client.textStatus)
            self.writeInfo(self.client.textStatus)
            self.window.SliderR.setEnabled(False)
            self.window.SliderG.setEnabled(False)
            self.window.SliderB.setEnabled(False)
            self.window.SliderH.setEnabled(False)
            self.window.SliderS.setEnabled(False)
            self.window.SliderV.setEnabled(False)
            self.window.RainbowButton.setEnabled(False)
            self.window.ConnectButton.setText("Połącz")
            return

        self.writeConsole('Connecting with {}:{}... '.format(self.window.IPLine.text(), self.window.PortLine.text()))
        self.client.connect(self.window.IPLine.text(), int(self.window.PortLine.text()))
        print(self.client.textStatus)
        print(type(self.client.textStatus))
        self.writeConsole(str(self.client.textStatus))
        self.writeInfo(str(self.client.textStatus))
        if self.client.isConnected == True:
            self.window.SliderR.setEnabled(True)
            self.window.SliderG.setEnabled(True)
            self.window.SliderB.setEnabled(True)
            self.window.SliderH.setEnabled(True)
            self.window.SliderS.setEnabled(True)
            self.window.SliderV.setEnabled(True)
            self.window.RainbowButton.setEnabled(True)
            self.window.ConnectButton.setText("Rozłącz")
        return self.client.isConnected

    def writeInfo(self, text):
        self.window.InfoLabel.setText(text)

    def writeConsole(self, text):
        self.window.TextBrowser.append(text)

    def sendColor(self, red, green, blue):
        if self.recently_color == (red,green,blue):
            return
        self.client.send("COLOR:" + str(red) + "," + str(green) + "," + str(blue))
        self.recently_color = (red,green,blue)

    def setLocalColor(self):
        text_brightness = "0, 0, 0"
        if self.window.SliderR.value() * 0.299 + self.window.SliderG.value() * 0.687 + self.window.SliderB.value() * 0.114 < 160:
            text_brightness = "255, 255, 255"
        self.window.LocalColor.setStyleSheet(
            "background-color: rgb(" + str(self.window.SliderR.value()) + "," + str(self.window.SliderG.value()) +
            "," + str(self.window.SliderB.value()) + ");\ncolor: rgb(" + text_brightness + ");")

        color_text = '#%02x%02x%02x' % (self.window.SliderR.value(), self.window.SliderG.value(), self.window.SliderB.value())
        self.window.LocalColor.setText("<html><head/><body><p>" + color_text + "</p></body></html>")

