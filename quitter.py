import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5.QtCore import *
uifile_2 = 'quitter.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class quitter(QDialog, form_2):
    
    def fermer(self):
        QCoreApplication.instance().quit()  
    
    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton.clicked.connect(self.fermer)
        self.pushButton_2.clicked.connect(self.close)
        