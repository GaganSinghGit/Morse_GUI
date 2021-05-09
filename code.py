from PyQt5 import QtCore, QtGui, QtWidgets
import RPi.GPIO as GPIO
from time import sleep

led = 11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led,GPIO.OUT, initial= GPIO.LOW)





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 215)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.inputBox = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBox.setGeometry(QtCore.QRect(102, 50, 191, 32))
        self.inputBox.setMaxLength(12)
        self.inputBox.setObjectName("inputBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(150, 110, 99, 30))
        self.pushButton.setObjectName("pushButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 28))
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
        self.pushButton.setText(_translate("MainWindow", "RUN"))

    
    
        

if __name__ == "__main__":
    
    
    import sys
    MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
   'C':'-.-.', 'D':'-..', 'E':'.',
   'F':'..-.', 'G':'--.', 'H':'....',
   'I':'..', 'J':'.---', 'K':'-.-',
   'L':'.-..', 'M':'--', 'N':'-.',
   'O':'---', 'P':'.--.', 'Q':'--.-',
   'R':'.-.', 'S':'...', 'T':'-',
   'U':'..-', 'V':'...-', 'W':'.--',
   'X':'-..-', 'Y':'-.--', 'Z':'--..',
   '1':'.----', '2':'..---', '3':'...--',
   '4':'....-', '5':'.....', '6':'-....',
   '7':'--...', '8':'---..', '9':'----.',
   '0':'-----', ', ':'--..--', '.':'.-.-.-',
   '?':'..--..', '/':'-..-.', '-':'-....-',
   '(':'-.--.', ')':'-.--.-'
    }
    def dot():
        GPIO.output(led, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)
    def dash():
        GPIO.output(led, GPIO.HIGH)
        sleep(1)
        GPIO.output(led, GPIO.LOW)
        sleep(1)
        
    def sendSignal():
        message = ui.inputBox.text()
        print(message)
        my_cipher = ''
        for myletter in message:
            if myletter != ' ':
                my_cipher += MORSE_CODE_DICT[myletter] + ' '
            else:
                my_cipher += ' '
        print(my_cipher)
        for letter in my_cipher:
            if letter == '.':
                dot()
                print("dot")
            if letter == '-':
                dash()
                print("dash")
            if letter == ' ':
                sleep(1)
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    ui.pushButton.clicked.connect(sendSignal)
    
    MainWindow.show()
    sys.exit(app.exec_())
