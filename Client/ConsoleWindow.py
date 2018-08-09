import ConsoleUI
from PyQt5.QtWidgets import QDialog


class ConsoleWindow(QDialog, ConsoleUI.Ui_Dialog):
    def __init__(self):
        super(ConsoleWindow, self).__init__()

        self.setupUi(self)

        self.SendButton.clicked.connect(self._app.sendmessage)

        self.DialogButtonBox.accepted.connect(self.accept_button_SLOT)
        self.DialogButtonBox.rejected.connect(self.reject_button_SLOT)
        # self.ConnectButton.clicked.connect(self.onConnect)
        # self.SettingsButton.clicked.connect(self.onSettings)

    def send_button_SLOT(self):
        print("Send")

    def help_button_SLOT(self):
        print("Help")
