import SettingsUI
from PyQt5.QtWidgets import QDialog


class SettingsWindow(QDialog, SettingsUI.Ui_Dialog):
    def __init__(self):
        super(SettingsWindow, self).__init__()

        self.setupUi(self)

        self.DialogButtonBox.accepted.connect(self.accept_button_SLOT)
        self.DialogButtonBox.rejected.connect(self.reject_button_SLOT)
        # self.ConnectButton.clicked.connect(self.onConnect)
        # self.SettingsButton.clicked.connect(self.onSettings)

    def accept_button_SLOT(self):
        print("Zatwierdzono")
        self.close()

    def reject_button_SLOT(self):
        print("Anulowano")
