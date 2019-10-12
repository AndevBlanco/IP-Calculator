# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(525, 334)
        MainWindow.setStyleSheet("background-color:#2b2c2e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(450, 250, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equal.setFont(font)
        self.equal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.equal.setObjectName("equal")
        self.ip = QtWidgets.QTextEdit(self.centralwidget)
        self.ip.setEnabled(True)
        self.ip.setGeometry(QtCore.QRect(20, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ip.setFont(font)
        self.ip.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ip.setStyleSheet("color:#e4e4e5;")
        self.ip.setReadOnly(False)
        self.ip.setOverwriteMode(False)
        self.ip.setObjectName("ip")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(330, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calculate.setFont(font)
        self.calculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.calculate.setObjectName("calculate")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(330, 250, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help.setFont(font)
        self.help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.help.setObjectName("help")
        self.inp2 = QtWidgets.QTextEdit(self.centralwidget)
        self.inp2.setGeometry(QtCore.QRect(170, 30, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inp2.setFont(font)
        self.inp2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inp2.setStyleSheet("color:#e4e4e5;")
        self.inp2.setReadOnly(False)
        self.inp2.setOverwriteMode(False)
        self.inp2.setObjectName("inp2")
        self.time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(70, 260, 194, 31))
        self.time.setReadOnly(True)
        self.time.setObjectName("time")
        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(20, 80, 281, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.result.setFont(font)
        self.result.setStyleSheet("color:#e4e4e5;")
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#e4e4e5;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#e4e4e5;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 525, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.equal.setText(_translate("MainWindow", "="))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.help.setText(_translate("MainWindow", "Help"))
        self.label.setText(_translate("MainWindow", "IP Address"))
        self.label_2.setText(_translate("MainWindow", "Netmask"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

