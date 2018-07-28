# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(206, 269)
        self.DialogButtonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.DialogButtonBox.setGeometry(QtCore.QRect(20, 230, 166, 26))
        self.DialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.DialogButtonBox.setObjectName("DialogButtonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 160, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.RedLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.RedLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.RedLabel.setObjectName("RedLabel")
        self.gridLayout.addWidget(self.RedLabel, 0, 0, 1, 1)
        self.GreenLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.GreenLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.GreenLabel.setObjectName("GreenLabel")
        self.gridLayout.addWidget(self.GreenLabel, 1, 0, 1, 1)
        self.BlueLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.BlueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.BlueLabel.setObjectName("BlueLabel")
        self.gridLayout.addWidget(self.BlueLabel, 2, 0, 1, 1)
        self.RedSpin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.RedSpin.setObjectName("RedSpin")
        self.gridLayout.addWidget(self.RedSpin, 0, 1, 1, 1)
        self.GreenSpin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.GreenSpin.setObjectName("GreenSpin")
        self.gridLayout.addWidget(self.GreenSpin, 1, 1, 1, 1)
        self.BlueSpin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.BlueSpin.setObjectName("BlueSpin")
        self.gridLayout.addWidget(self.BlueSpin, 2, 1, 1, 1)
        self.FreqSpin = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.FreqSpin.setObjectName("FreqSpin")
        self.gridLayout.addWidget(self.FreqSpin, 3, 1, 1, 1)
        self.FreqLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.FreqLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.FreqLabel.setObjectName("FreqLabel")
        self.gridLayout.addWidget(self.FreqLabel, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.RedLabel.setText(_translate("Dialog", "GPIO Red"))
        self.GreenLabel.setText(_translate("Dialog", "GPIO Green"))
        self.BlueLabel.setText(_translate("Dialog", "GPIO Blue"))
        self.FreqLabel.setText(_translate("Dialog", "PWM Frequency"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

