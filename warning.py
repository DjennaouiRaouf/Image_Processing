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
uifile_2 = 'warning.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class warning(QDialog, form_2):
    
    
    def __init__(self,parent=None,str_warning=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.label.setText(str_warning)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.pushButton.clicked.connect(self.close)
        
        