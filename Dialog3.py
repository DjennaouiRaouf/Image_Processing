import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from warning import warning

uifile_2 = 'Dialog3.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class Dialog3(QDialog, form_2):
    data3= qtc.pyqtSignal(int, float)
    
    def input_values(self):
       
        try:
            self.taille=int(self.lineEdit.text())
            self.sigma=float(self.lineEdit_2.text())
            self.close()
            self.data3.emit(self.taille,self.sigma)
            
            
        except:
            self.w=warning(str_warning="ERREUR DE SAISIE !")
            self.w.show()
  
    
    def __init__(self,parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.pushButton.clicked.connect(self.input_values)
        self.pushButton_2.clicked.connect(self.close)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
