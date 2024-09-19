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

uifile_2 = 'Dialog.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class Dialog(QDialog, form_2):
    data= qtc.pyqtSignal(float, float)
    
    def input_values(self):
       
        try:
            self.alpha=float(self.lineEdit.text())
            self.beta=float(self.lineEdit_2.text())
            self.close()
            self.data.emit(self.alpha,self.beta)
            
            
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