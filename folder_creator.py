# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'folder_creator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 781, 141))
        self.groupBox.setObjectName("groupBox")
        self.btnProcurar = QtWidgets.QPushButton(self.groupBox)
        self.btnProcurar.setGeometry(QtCore.QRect(700, 40, 75, 23))
        self.btnProcurar.setObjectName("btnProcurar")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 61, 16))
        self.label.setObjectName("label")
        self.edtCaminho = QtWidgets.QLineEdit(self.groupBox)
        self.edtCaminho.setEnabled(True)
        self.edtCaminho.setGeometry(QtCore.QRect(10, 40, 681, 20))
        self.edtCaminho.setReadOnly(True)
        self.edtCaminho.setObjectName("edtCaminho")
        self.chkPath = QtWidgets.QCheckBox(self.groupBox)
        self.chkPath.setGeometry(QtCore.QRect(10, 70, 141, 17))
        self.chkPath.setChecked(False)
        self.chkPath.setObjectName("chkPath")
        self.btnCriarPastas = QtWidgets.QPushButton(self.groupBox)
        self.btnCriarPastas.setGeometry(QtCore.QRect(10, 100, 75, 23))
        self.btnCriarPastas.setObjectName("btnCriarPastas")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 150, 781, 421))
        self.groupBox_2.setObjectName("groupBox_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 761, 391))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Criador de Pastas"))
        self.groupBox.setTitle(_translate("MainWindow", "Escolher caminho"))
        self.btnProcurar.setText(_translate("MainWindow", "Procurar 📁"))
        self.label.setText(_translate("MainWindow", "Caminho:"))
        self.chkPath.setText(_translate("MainWindow", "Utilizar caminho atual"))
        self.btnCriarPastas.setText(_translate("MainWindow", "Criar Pastas"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Logs"))