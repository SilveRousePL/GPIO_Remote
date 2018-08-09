# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ConsoleUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 541)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 561, 521))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TextBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.TextBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.TextBrowser.setObjectName("TextBrowser")
        self.verticalLayout.addWidget(self.TextBrowser)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SendLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.SendLine.setMaximumSize(QtCore.QSize(16777215, 100))
        self.SendLine.setMaxLength(1000)
        self.SendLine.setObjectName("SendLine")
        self.horizontalLayout_2.addWidget(self.SendLine)
        self.SendButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.SendButton.setEnabled(True)
        self.SendButton.setMaximumSize(QtCore.QSize(40, 100))
        self.SendButton.setObjectName("SendButton")
        self.horizontalLayout_2.addWidget(self.SendButton)
        self.HelpButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HelpButton.sizePolicy().hasHeightForWidth())
        self.HelpButton.setSizePolicy(sizePolicy)
        self.HelpButton.setMaximumSize(QtCore.QSize(20, 100))
        self.HelpButton.setObjectName("HelpButton")
        self.horizontalLayout_2.addWidget(self.HelpButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.SendLine.setPlaceholderText(_translate("Dialog", "Komenda"))
        self.SendButton.setText(_translate("Dialog", "Send"))
        self.HelpButton.setText(_translate("Dialog", "?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

