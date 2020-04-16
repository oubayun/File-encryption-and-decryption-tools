# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_en_decryption.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # 固定窗口大小
        MainWindow.resize(800, 460)
        MainWindow.setFixedSize(800, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.line = QtWidgets.QFrame(MainWindow)
        self.line.setGeometry(QtCore.QRect(10, 385, 781, 10))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.filepath = QtWidgets.QTextEdit(MainWindow)
        self.filepath.setGeometry(QtCore.QRect(110, 410, 461, 31))
        self.filepath.setObjectName("filepath")
        self.private_key = QtWidgets.QTextBrowser(MainWindow)
        self.private_key.setGeometry(QtCore.QRect(410, 40, 380, 306))
        self.private_key.setObjectName("private_key")
        self.decryption = QtWidgets.QRadioButton(MainWindow)
        self.decryption.setGeometry(QtCore.QRect(580, 415, 52, 20))
        self.decryption.setChecked(True)
        self.decryption.setObjectName("decryption")
        self.publickey = QtWidgets.QLabel(MainWindow)
        self.publickey.setGeometry(QtCore.QRect(10, 12, 27, 16))
        self.publickey.setObjectName("publickey")
        self.privatekey = QtWidgets.QLabel(MainWindow)
        self.privatekey.setGeometry(QtCore.QRect(410, 10, 27, 20))
        self.privatekey.setObjectName("privatekey")
        self.public_key = QtWidgets.QTextBrowser(MainWindow)
        self.public_key.setGeometry(QtCore.QRect(10, 40, 380, 306))
        self.public_key.setObjectName("public_key")
        self.encryption = QtWidgets.QRadioButton(MainWindow)
        self.encryption.setGeometry(QtCore.QRect(640, 415, 52, 20))
        self.encryption.setObjectName("encryption")
        self.en_decryption = QtWidgets.QLabel(MainWindow)
        self.en_decryption.setGeometry(QtCore.QRect(10, 417, 89, 16))
        self.en_decryption.setObjectName("en_decryption")
        self.apply = QtWidgets.QPushButton(MainWindow)
        self.apply.setGeometry(QtCore.QRect(700, 409, 87, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.apply.sizePolicy().hasHeightForWidth())
        self.apply.setSizePolicy(sizePolicy)
        self.apply.setObjectName("apply")
        self.generate = QtWidgets.QPushButton(MainWindow)
        self.generate.setGeometry(QtCore.QRect(700, 350, 87, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.generate.sizePolicy().hasHeightForWidth())
        self.generate.setSizePolicy(sizePolicy)
        self.generate.setObjectName("generate")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件加解密工具"))
        self.decryption.setText(_translate("MainWindow", "解密"))
        self.publickey.setText(_translate("MainWindow", "公钥"))
        self.privatekey.setText(_translate("MainWindow", "私钥"))
        self.encryption.setText(_translate("MainWindow", "加密"))
        self.en_decryption.setText(_translate("MainWindow", "加密&解密文件"))
        self.apply.setText(_translate("MainWindow", "应用(A)"))
        self.generate.setText(_translate("MainWindow", "生成(G)"))
