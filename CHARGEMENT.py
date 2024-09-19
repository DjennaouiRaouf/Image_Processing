import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt
from Main import Main
uifile_1 = 'chargement.ui'
form_1, base_1 = uic.loadUiType(uifile_1)


class chargement(QMainWindow, form_1):
#------------------------------------------------------------------------------
    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setWindowFlags(flags)
        self.show()
        self.timer = QTimer()
        self.timer.timeout.connect(self.handleTimer)
        self.timer.start(100)

    def handleTimer(self):
        value = self.progressBar.value()
        if value < 100:
            value = value + 1
            self.progressBar.setValue(value)
        else:
            self.timer.stop()
            self.main = Main()
            self.main.showFullScreen()
            self.close()






          
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = chargement()
    sys.exit(app.exec_())


