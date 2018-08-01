import sys, colorsys
import MainUI
import App
import SettingsWindow
from PyQt5.QtWidgets import QApplication, QDialog


class MainWindow(QDialog, MainUI.Ui_Dialog):

    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("GPIO Remote")

        self._app = app

        self.ConnectButton.clicked.connect(self.connect_Slot)
        self.SettingsButton.clicked.connect(self.settings_Slot)
        self.RainbowButton.clicked.connect(self.rainbow_Slot)
        self.MoreButton.clicked.connect(self.more_Slot)
        self.SendButton.clicked.connect(self.send_Slot)
        self.SendLine.returnPressed.connect(self.send_Slot)

        self.SliderR.actionTriggered.connect(self.slideRGB_Slot)
        self.SliderG.actionTriggered.connect(self.slideRGB_Slot)
        self.SliderB.actionTriggered.connect(self.slideRGB_Slot)
        self.SliderH.actionTriggered.connect(self.slideHSV_Slot)
        self.SliderS.actionTriggered.connect(self.slideHSV_Slot)
        self.SliderV.actionTriggered.connect(self.slideHSV_Slot)

    def send_Slot(self):
        text = self.SendLine.text()
        if not text:
            return
        self.SendLine.clear()
        self._app.writeconsole("<<< " + text)
        self._app.client.send(text)

    def connect_Slot(self):
        self._app.connect()

    def settings_Slot(self):
        window = SettingsWindow.SettingsWindow()
        window.show()

    def rainbow_Slot(self):
        print("Rzygam tęczą!")

    def more_Slot(self):
        if self.geometry().width() == 668:
            self.MoreButton.setText("Mniej <<")
            self.resize(1000, 276)
        else:
            self.MoreButton.setText("Więcej >>")
            self.resize(668, 276)

    def slideRGB_Slot(self):
        h, s, v = colorsys.rgb_to_hsv(self.SliderR.value(), self.SliderG.value(),
                                      self.SliderB.value())
        self.SliderH.setValue(h * 1535)
        self.SliderS.setValue(s * 255)
        self.SliderV.setValue(v)

        self._app.setlocalcolor()
        self._app.sendcolor(self.SliderR.value(), self.SliderG.value(), self.SliderB.value())

    def slideHSV_Slot(self):
        r, g, b = colorsys.hsv_to_rgb(self.SliderH.value() / 1535, self.SliderS.value() / 255,
                                      self.SliderV.value() / 255)
        self.SliderR.setValue(r*255)
        self.SliderG.setValue(g*255)
        self.SliderB.setValue(b*255)

        self._app.setlocalcolor()
        self._app.sendcolor(self.SliderR.value(), self.SliderG.value(), self.SliderB.value())

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
