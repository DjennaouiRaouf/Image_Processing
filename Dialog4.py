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

import video
import cv2
from warning import warning
from PIL import Image
uifile_2 = 'Dialog4.ui'
form_2, base_2 = uic.loadUiType(uifile_2)

class Dialog4(QDialog, form_2):

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


    def get_img_from_video(self):
        self.im_1=None
        self.im_2=None
        self.frame_1=None
        self.frame_2=None
        try:
            self.frame_1=int(self.lineEdit.text())
            self.frame_2=int(self.lineEdit_2.text())
            frame_list=video.get_frames(self.video)
            self.n=len(frame_list)
            try:
                self.im_1=frame_list[self.frame_1]
                self.im_2=frame_list[self.frame_2]

                del frame_list
            except:
                self.w=warning(str_warning="FRAMES ENTRE:{0 .."+str(self.n-1)+"}")
                self.w.show()

                    
        except:
            self.w=warning(str_warning="ERREUR DE SAISIE !")
            self.w.show()


    def input_values(self):
        try:
            self.get_img_from_video()
            self.im_1 = cv2.cvtColor(self.im_1, cv2.COLOR_BGR2RGB)
            self.img_1 = Image.fromarray(self.im_1)
            self.display(self.frame1_layout,1,self.img_1)
            self.im_2 = cv2.cvtColor(self.im_2, cv2.COLOR_BGR2RGB)
            self.img_2 = Image.fromarray(self.im_2)
            self.display(self.frame2_layout,2,self.img_2)
            diff=video.difference(self.img_1,self.img_2)
            self.display(self.diff_layout,'DIFFERENCE',diff)
        except:
            self.w=warning(str_warning="IMAGE NON DISPONIBLE !")
            self.w.show()




    def __init__(self,video,parent=None):
        QDialog.__init__(self,parent)
        self.setupUi(self)
        self.video=video
        self.im_1=None
        self.im_2=None
        self.frame_1=None
        self.frame_2=None
        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.pushButton.clicked.connect(self.input_values)
        self.pushButton_2.clicked.connect(self.close)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
