import sys
from PyQt5 import QtCore, QtGui, uic
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

uifile_2 = 'file_dialog.ui'
form_2, base_2 = uic.loadUiType(uifile_2)


class file_dialog(QDialog, form_2):
    data = qtc.pyqtSignal(str)

    def on_clicked(self, index):
        path = self.dirModel.fileInfo(index).absoluteFilePath()
        self.listview.setRootIndex(self.fileModel.setRootPath(path))
        self.path = path

    def file_path(self, index):
        try:
            self.file = None
            self.file = self.path + '/' + index.data()
            flag = os.path.isfile(self.file)
            if flag:
                self.data.emit(self.file)
                self.close()
        except:
            pass

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setupUi(self)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.btn_close_2.clicked.connect(self.close)
        self.setWindowModality(QtCore.Qt.ApplicationModal)

        self.path = None
        self.file = None

        path = r"C:\Users\R-DJENNAOUI\Desktop\PROJET"

        self.dirModel = QFileSystemModel()
        self.dirModel.setRootPath(r"C:\Users\R-DJENNAOUI\Desktop\PROJET")
        self.dirModel.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)

        self.fileModel = QFileSystemModel()
        self.fileModel.setFilter(QDir.NoDotAndDotDot | QDir.Files)

        self.treeview.setModel(self.dirModel)
        self.listview.setModel(self.fileModel)

        self.treeview.setRootIndex(self.dirModel.index(path))
        self.listview.setRootIndex(self.fileModel.index(path))
        self.treeview.setIndentation(20)
        self.treeview.setSortingEnabled(True)
        self.treeview.setDragEnabled(False)
        self.treeview.setAcceptDrops(False)
        self.treeview.setDropIndicatorShown(True)
        self.treeview.setEditTriggers(QTreeView.NoEditTriggers)
        for i in range(1, self.treeview.model().columnCount()):
            self.treeview.header().hideSection(i)

        self.treeview.clicked.connect(self.on_clicked)
        self.listview.clicked.connect(self.file_path)


