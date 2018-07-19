from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget
from PyQt5.QtGui import *
import sys
import time
import serial
import random
from wi2n import *
class selectname(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.shut = 0
    def run(self):
        self.readnamelist()
        ui.button.clicked.connect(self.quit)
        while True:
           time.sleep(0.05)
           if self.shut %2 == 1:
                ui.name.setText(self.nameDispaly[random.randint(0,self.namemax-1)])
    def quit(self):
        self.shut += 1
    def readnamelist(self):
        with open('NameList.txt','r') as conf:
            self.nameDispaly = conf.readlines()
            print(len(self.nameDispaly))
            self.namemax = len(self.nameDispaly)
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    thread = selectname()
    thread.start()
    sys.exit(app.exec_())