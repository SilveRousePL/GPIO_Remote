import sys
import SettingsUI
from PyQt5.QtWidgets import QDialog


class SettingsWindow(QDialog, SettingsUI.Ui_Dialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.setupUi(self)

        # self.ConnectButton.clicked.connect(self.onConnect)
        # self.SettingsButton.clicked.connect(self.onSettings)

    def accept(self):
        print("Naciśnięto Connect")
        if(True):
            self.SliderR.setEnabled(True)
            self.SliderG.setEnabled(True)
            self.SliderB.setEnabled(True)
            self.SliderH.setEnabled(True)
            self.SliderS.setEnabled(True)
            self.SliderV.setEnabled(True)
            self.RainbowButton.setEnabled(True)

    def reject(self):
        SettingsUI.setupUi(self)
