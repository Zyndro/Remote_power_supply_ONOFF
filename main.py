import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import serial


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PSU'
        self.left = 300
        self.top = 300
        self.width = 200
        self.height = 200
        self.port="COM3"
        self.init_ui()
        self.move(0,0)
        self.show()
        self.serial = None

    def init_ui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #on
        self.buttonON = QPushButton('On', self)
        self.buttonON.move(50, 90)
        self.buttonON.clicked.connect(self.turn_on)
        #off
        self.buttonOFF = QPushButton('Off', self)
        self.buttonOFF.move(50, 130)
        self.buttonOFF.clicked.connect(self.turn_off)
        #port
        self.portbox = QComboBox(self)
        self.portbox.addItems([" ", "COM1","COM2","COM3","COM4","COM5","COM6","COM7","COM8"])
        self.portbox.setGeometry(70, 20, 55, 30)
        self.portbox.activated.connect(self.update_port)
        self.buttonON.setEnabled(False)
        self.buttonOFF.setEnabled(False)

    def turn_on(self):
        self.serial.write(b"OUT1")

    def turn_off(self):
        self.serial.write(b"OUT0")

    def update_port(self):
        self.port = self.portbox.currentText()
        if self.portbox.itemText(0) == " ":
            self.portbox.removeItem(0)
        try:
            self.serial = serial.Serial(port=str(self.port), baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)
            self.portbox.setEnabled(False)
            print("ok")
            self.buttonON.setEnabled(True)
            self.buttonOFF.setEnabled(True)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
