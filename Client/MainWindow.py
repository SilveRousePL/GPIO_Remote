import colorsys
import MainUI
import SettingsWindow
from PyQt5.QtWidgets import QApplication, QDialog


class MainWindow(QDialog, MainUI.Ui_Dialog):

    def __init__(self, app):
        super(MainWindow, self).__init__()
        self._app = app

        self.setupUi(self)
        self.setWindowTitle("GPIO Remote")

        self.child_window = None

        self.ConnectButton.clicked.connect(self.connect_button_SLOT)
        self.SettingsButton.clicked.connect(self.settings_button_SLOT)
        self.RainbowButton.clicked.connect(self.rainbow_button_SLOT)
        self.MoreButton.clicked.connect(self.more_button_SLOT)

        self.SliderR.actionTriggered.connect(self.RGB_slider_SLOT)
        self.SliderG.actionTriggered.connect(self.RGB_slider_SLOT)
        self.SliderB.actionTriggered.connect(self.RGB_slider_SLOT)
        self.SliderH.actionTriggered.connect(self.HSV_slider_SLOT)
        self.SliderS.actionTriggered.connect(self.HSV_slider_SLOT)
        self.SliderV.actionTriggered.connect(self.HSV_slider_SLOT)

    def connect_button_SLOT(self):
        self.ConnectButton.setEnabled(False)
        if self._app.connecttoserver() is True:
            self.SliderR.setEnabled(True)
            self.SliderG.setEnabled(True)
            self.SliderB.setEnabled(True)
            self.SliderH.setEnabled(True)
            self.SliderS.setEnabled(True)
            self.SliderV.setEnabled(True)
            self.ConnectButton.clicked.disconnect()
            self.ConnectButton.clicked.connect(self.disconnect_button_SLOT)
            self.RainbowButton.setEnabled(True)
            self.ConnectButton.setText("Rozłącz")
        self.ConnectButton.setEnabled(True)

    def disconnect_button_SLOT(self):
        self.ConnectButton.setEnabled(False)
        self.ConnectButton.clicked.disconnect()
        self._app.disconnected.emit()
        self.ConnectButton.clicked.connect(self.connect_button_SLOT)
        self.SliderR.setEnabled(False)
        self.SliderG.setEnabled(False)
        self.SliderB.setEnabled(False)
        self.SliderH.setEnabled(False)
        self.SliderS.setEnabled(False)
        self.SliderV.setEnabled(False)
        self.RainbowButton.setEnabled(False)
        self.ConnectButton.setText("Połącz")
        self.ConnectButton.setEnabled(True)

    def settings_button_SLOT(self):
        self.child_window = SettingsWindow.SettingsWindow()
        self.child_window.show()

    def rainbow_button_SLOT(self):
        self._app.writeconsole("<b><i>Rzygam tęczą</i></b>")

    def more_button_SLOT(self):
        if self.geometry().width() == 668:
            self.MoreButton.setText("Mniej <<")
            self.resize(1000, 276)
        else:
            self.MoreButton.setText("Więcej >>")
            self.resize(668, 276)

    def RGB_slider_SLOT(self):
        h, s, v = colorsys.rgb_to_hsv(self.SliderR.value(), self.SliderG.value(),
                                      self.SliderB.value())
        self.SliderH.setValue(h * 1535)
        self.SliderS.setValue(s * 255)
        self.SliderV.setValue(v)

        self._app.setlocalcolor()
        self._app.sendcolor(self.SliderR.value(), self.SliderG.value(), self.SliderB.value())

    def HSV_slider_SLOT(self):
        r, g, b = colorsys.hsv_to_rgb(self.SliderH.value() / 1535, self.SliderS.value() / 255,
                                      self.SliderV.value() / 255)
        self.SliderR.setValue(r*255)
        self.SliderG.setValue(g*255)
        self.SliderB.setValue(b*255)

        self._app.setlocalcolor()
        self._app.sendcolor(self.SliderR.value(), self.SliderG.value(), self.SliderB.value())

