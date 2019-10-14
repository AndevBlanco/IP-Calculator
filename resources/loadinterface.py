# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import ipaddress, time
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def info(self, MainWindow):
        self.result.setText("Buenos dias estimado e ilustre profesor jorge blanco, esta es la calculadora ip, digite la direccion ip y en el sigiente cuadro la máscara, no se acepta la ip con mascara en el mismo campo")
    def CIP(self, MainWindow):
        ipaddr=self.ip.toPlainText()
        netmask=self.mask.toPlainText()
        def subCalc(ipaddr, netmask):
            band=False
            try:
                ipv4=ipaddr+"/"+netmask
                ip=ipaddress.IPv4Network(ipv4, strict=False)
                firstoctect=int(str(ip).split('.')[0])
                ipclass=""
                if firstoctect==0:
                    self.result.setText("Esta es una ip")
                elif firstoctect>=1 and firstoctect<=126:
                    ipclass="Clase A - rango de la ip es de 1 a 126"
                elif firstoctect==127:
                    self.result.setText("Esta es una direccion de bucle invertido")
                elif firstoctect>=128 and firstoctect<=191:
                    ipclass="Clase B - rango de la ip es de 128 a 191"
                elif firstoctect>=192 and firstoctect<=223:
                    ipclass="Clase C - rango de la ip es de 192 a 223"
                elif firstoctect>=224 and firstoctect<=239:
                    ipclass="Clase D - Multicast"
                else:
                    ipclass="Clase E - Experimental"
            except ipaddress.AddressValueError:
                self.result.setText("Direccion ip no válida")
                band=True
            except ipaddress.NetmaskValueError:
                self.result.setText("Máscara de red no válida")
                band=True
            if band:
                self.result.setText("Datos no validos")
            else:
                cadena='IP {}'.format(ipclass)+"\n"+"La red es {}".format(ip.with_netmask)+"\n"+"Host minimo asignable {}".format(ip.network_address + 1)+"\n"+"Host maximo asignable {} ".format(ip.broadcast_address - 1)+"\n"+"La dirección de broadcast es {} ".format(ip.broadcast_address)
                self.result.setText(cadena)
        if("/" in ipaddr or self.ip.toPlainText()=="" or self.ip.toPlainText()==""):
            self.result.setText("Datos no validos")
        else:
            subCalc(ipaddr,netmask)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 381)
        MainWindow.setStyleSheet("background-color:#2b2c2e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ip = QtWidgets.QTextEdit(self.centralwidget)
        self.ip.setEnabled(True)
        self.ip.setGeometry(QtCore.QRect(40, 50, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.ip.setFont(font)
        self.ip.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ip.setStyleSheet("color:#e4e4e5;")
        self.ip.setReadOnly(False)
        self.ip.setOverwriteMode(False)
        self.ip.setObjectName("ip")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(660, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.calculate.setFont(font)
        self.calculate.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculate.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.calculate.setObjectName("calculate")
        self.calculate.clicked.connect(self.CIP)
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(660, 130, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help.setFont(font)
        self.help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.help.setObjectName("help")
        self.help.clicked.connect(self.info)
        self.mask = QtWidgets.QTextEdit(self.centralwidget)
        self.mask.setGeometry(QtCore.QRect(330, 50, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.mask.setFont(font)
        self.mask.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.mask.setStyleSheet("color:#e4e4e5;")
        self.mask.setReadOnly(False)
        self.mask.setOverwriteMode(False)
        self.mask.setObjectName("mask")
        self.time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(40, 290, 194, 31))
        self.time.setReadOnly(True)
        self.time.setObjectName("time")
        self.result = QtWidgets.QTextEdit(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(40, 110, 561, 161))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.result.setFont(font)
        self.result.setStyleSheet("color:#e4e4e5;")
        self.result.setReadOnly(True)
        self.result.setObjectName("result")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#e4e4e5;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 30, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#e4e4e5;")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 21))
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
    time.sleep(7)
    MainWindow.show()
    sys.exit(app.exec_())
