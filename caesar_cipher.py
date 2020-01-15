"""
    This is a caesar encryption decryption program. It takes a text and a key number
    for encryption or decryption. It returns the encrypted or decrypted text based
    on the called method. Two methods are available, which are encry(shift,text) and
    decry(shift,text)

"""
from PyQt5 import QtCore, QtGui, QtWidgets

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = {"0":"zero","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}

class enc_dec():

    def __init__(self, shift,text):
        self.shift = shift
        self.text = text

    #encrypt the text to cypher by shifting with user inp num
    def encry(shift, text):
        """
        Encryption method, takes key number and (plain text) string
        """
        cypher= ""               #output cypher text, initially null
        text = text.lower()     #work on lower case string only
        shift = int(shift)      #parse string to int number
        for i in text:
            if i.isdigit():
                text = text.replace(i,number[i])
        #loop in text and add each encrypted char to cypher string
        for i in text:
            if i.isalpha():
                txt_num = alphabet.index(i) #get the index of the char
                txt_num += shift            #shift the index by user inp
                if(txt_num > 25):           #if index out of range, loop back
                    txt_num %= 26
                cypher += alphabet[txt_num]
            elif i.isspace():
                cypher += " "       #if char is space
            else:
                cypher += i

        return(cypher)

    #decrypt the text to cypher by shifting with user inp num
    def decry(shift,text):
        """
        Decryption method, takes key number and (cipher text) string
        """
        plain= ""               #output plain text, initially null
        text = text.lower()     #work on lower case string only
        shift = int(shift)      #parse string to int number

        for i in text:
            if (i.isalpha()):
                txt_num = alphabet.index(i)
                txt_num -= shift
                if(txt_num < 0):
                    txt_num = 26 -abs(txt_num)
                plain = plain + alphabet[txt_num]
            elif i.isspace():
                plain += " "
            else:
                plain += i
        return(plain)


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caesar_cipher.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #QPlainTextEdit which the input is typed
        self.InputField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.InputField.setGeometry(QtCore.QRect(90, 50, 431, 121))
        self.InputField.setMouseTracking(True)
        self.InputField.setObjectName("InputField")

        #QLineEdit which the encryption key is typed in
        self.key_in = QtWidgets.QLineEdit(self.centralwidget)
        self.key_in.setGeometry(QtCore.QRect(160, 220, 141, 51))
        self.key_in.setObjectName("key_in")

        #the decryption button
        self.dec_button = QtWidgets.QPushButton(self.centralwidget)
        self.dec_button.setGeometry(QtCore.QRect(420, 220, 91, 51))
        self.dec_button.setObjectName("dec_button")

        #the encryption button
        self.enc_button = QtWidgets.QPushButton(self.centralwidget)
        self.enc_button.setGeometry(QtCore.QRect(310, 220, 81, 51))
        self.enc_button.setObjectName("enc_button")

        #labelindicating the InputField
        self.input_label = QtWidgets.QLabel(self.centralwidget)
        self.input_label.setGeometry(QtCore.QRect(30, 90, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")

        #labelindicating the key_in QLineEdit
        self.Enc_lable = QtWidgets.QLabel(self.centralwidget)
        self.Enc_lable.setGeometry(QtCore.QRect(30, 230, 111, 41))
        self.Enc_lable.setObjectName("Enc_lable")

        #QTextBrowser where the output text is displayed
        self.output_field = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_field.setGeometry(QtCore.QRect(90, 290, 431, 231))
        self.output_field.setObjectName("output_field")

        #line dividing the input section and button control & key input section
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 270, 541, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        #line dividing the output section and button control & key input section
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 200, 541, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        #lableindicating the window
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(30, 10, 400, 31))
        font = QtGui.QFont()
        font.setFamily("Vemana2000")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")

        #labelindicating the output field
        self.Output_label = QtWidgets.QLabel(self.centralwidget)
        self.Output_label.setGeometry(QtCore.QRect(20, 390, 421, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.Output_label.setFont(font)
        self.Output_label.setObjectName("Output_label")
        MainWindow.setCentralWidget(self.centralwidget)

        #menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        #status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connecting the encryption and decryption button to the encr_decry class obj
        self.enc_button.clicked.connect(self.do_encrypt)
        self.dec_button.clicked.connect(self.do_decrypt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Caesar Cipher"))
        self.dec_button.setText(_translate("MainWindow", "Decrypt"))
        self.enc_button.setText(_translate("MainWindow", "Encrypt"))
        self.input_label.setText(_translate("MainWindow", "Input"))
        self.Enc_lable.setText(_translate("MainWindow", "Encryption Key"))
        self.title_label.setText(_translate("MainWindow", "Ceaser Cipher Encryption / Decryption"))
        self.Output_label.setText(_translate("MainWindow", "Output"))

    def do_encrypt(self):
        text = self.InputField.toPlainText()
        shift = self.key_in.text()
        text_out = enc_dec.encry(shift,text)
        self.output_field.setText(text_out)

    def do_decrypt(self):
        text = self.InputField.toPlainText()
        shift = self.key_in.text()
        text_out = enc_dec.decry(shift,text)
        self.output_field.setText(text_out)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
