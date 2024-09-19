import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic
from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton, QFileDialog,QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib
import arithm_op

from PyQt5 import QtCore as qtc
import cv2
from warning import warning
from PIL import Image
import arithm_op
uifile_2 = 'Dialog8.ui'
form_2, base_2 = uic.loadUiType(uifile_2)
from file_dialog import file_dialog
class Dialog8(QDialog, form_2):

    def display(self,frame_i,i,im=None):
        try:
            for i in reversed(range(frame_i.count())):
                frame_i.itemAt(i).widget().setParent(None)

            self.figure = Figure(tight_layout=True)
            self.canvas = FigureCanvas(self.figure)
            self.toolbar = NavigationToolbar(self.canvas, self)
            frame_i.addWidget(self.toolbar)
            frame_i.addWidget(self.canvas)
            self.graph = self.figure.add_subplot(111)
            self.graph.imshow(im)
            self.graph.axis('off')
            self.graph.set_title('IMAGE'+str(i))
        except:
            self.w=warning(str_warning="IMAGE NON DISPONIBLE !")
            self.w.show()
        
    @qtc.pyqtSlot(str)
    def importer_img_1(self,path):
        
        for i in reversed(range(self.frame1_layout.count())):
            self.frame1_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.frame1_layout.count())):
            self.frame2_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.somme_layout.count())):
            self.somme_layout.itemAt(i).widget().setParent(None)
        self.path1 = path
        self.label_8.setText(self.path1)
        
    
      
    def get_params_5(self):     
        self.fdialog = file_dialog()
        self.fdialog.data.connect(self.importer_img_1)
        self.fdialog.show()

    
    @qtc.pyqtSlot(str)
    def importer_img_2(self,path):
        
        for i in reversed(range(self.frame1_layout.count())):
            self.frame1_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.frame1_layout.count())):
            self.frame2_layout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.somme_layout.count())):
            self.somme_layout.itemAt(i).widget().setParent(None)
        self.path2 = path
        self.label_7.setText(self.path2)
        
    
      
    def get_params_6(self):     
        self.fdialog = file_dialog()
        self.fdialog.data.connect(self.importer_img_2)
        self.fdialog.show()
    
    def somme(self):
        im_1=Image.open(self.path1).convert('LA')
        im_2=Image.open(self.path2).convert('LA')
        self.display(self.frame1_layout,1,im_1)
        self.display(self.frame2_layout,2,im_2)
        im_1=im_1.convert('L')
        im_2=im_2.convert('L')
        s=arithm_op.somme(im_1, im_2)
        self.display(self.somme_layout,'somme',s)
    def __init__(self,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        
        self.im_1=None
        self.im_2=None
        self.frame_1=None
        self.frame_2=None
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_13.clicked.connect(self.get_params_5)
        self.pushButton_12.clicked.connect(self.get_params_6)
        self.pushButton.clicked.connect(self.somme)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

