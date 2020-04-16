from PyQt5.QtWidgets import QApplication, QMainWindow
from file_en_decryption_ui import *
from Crypto.PublicKey import RSA
from PyQt5 import QtGui
import en_decrypt
import platform
import sys

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        # 生成密钥
        self.generate.clicked.connect(self.createkey)
        self.apply.clicked.connect(self.en_decryptionfile)

    def createkey(self):
        code = "muzilee_www.oubayun.com"
        # 生成 2048 位的 RSA 密钥
        key = RSA.generate(2048)
        encrypted_key = key.exportKey(passphrase=code,
                                      pkcs=8,
                                      protection="scryptAndAES128-CBC")
        # 生成私钥
        self.private_key.setText(str(encrypted_key, encoding="utf-8"))
        with open("rsa_private.key", "wb") as f:
            f.write(encrypted_key)
        # 生成公钥
        self.public_key.setText(
            str(key.publickey().exportKey(), encoding="utf-8"))
        with open("rsa_public.key", "wb") as f:
            f.write(key.publickey().exportKey())

    def en_decryptionfile(self):
        systemtype = platform.system()
        if systemtype == "Windows":
            filepathvalue = self.filepath.toPlainText().replace("file:///", "")
        else:
            filepathvalue = self.filepath.toPlainText().replace("file://", "")
        if filepathvalue:
            # 解密按钮值(True&False)
            decryptionvalue = self.decryption.isChecked()
            if str(decryptionvalue) == "True":
                destatus = en_decrypt.Descrypt(filepathvalue)
                self.public_key.setText(destatus)
            else:
                enstatus = en_decrypt.Encrypt(filepathvalue)
                self.private_key.setText(enstatus)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.setWindowIcon(QtGui.QIcon("logo.ico"))
    myWin.show()
    sys.exit(app.exec_())
