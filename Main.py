import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from mpldatacursor import datacursor
from PyQt5 import  uic
from PIL import Image
import numpy as np
from PyQt5.QtWidgets import *
from PyQt5 import QtCore as qtc
import matplotlib
import histogramme_op as hop
from Dialog import Dialog
from Dialog2 import Dialog2
from Dialog3 import Dialog3
from Dialog4 import Dialog4
from Dialog5 import Dialog5
from Dialog6 import Dialog6
from Dialog7 import Dialog7
from Dialog8 import Dialog8
from quitter import quitter
from warning import warning
from file_dialog import file_dialog
import Segmentation as seg
import Filtre as f
import CCL as object_finder
import op_geo as geo
import gradient as g
#-----------------------------------------------------------------------------
uifile_1 = 'Main.ui'
form_1, base_1 = uic.loadUiType(uifile_1)


class Main(QMainWindow, form_1):
 
#-----------------------------------------------------------------------------
   
    @qtc.pyqtSlot(str)
    
    def importer_img(self,path):
        
            
        for i in reversed(range(self.plotLayout.count())):
            self.plotLayout.itemAt(i).widget().setParent(None)
        for i in reversed(range(self.imgLayout.count())):
            self.imgLayout.itemAt(i).widget().setParent(None)

        self.path = path
        self.label_2.setText(self.path)
        if self.path:
            self.display(self.path,None)

        self.intensite=range(256)
        self.img=None
        self.hs=None
        self.hn=None
        self.hc=None
        self.hcn=None
        self.rev=None
        self.hr=None
        self.imt=None
        self.ht=None
        self.exp=None
        self.hexp=None
        self.heg=None
        self.eg=None
        self.img_bin=None
        self.med=None
        self.gauss=None
        self.taille=None
        self.sigma=None
        self.moy=None
        self.obj=None
        self.grad=None

    def get_params_5(self):
        
            
        self.fdialog = file_dialog()
        self.fdialog.data.connect(self.importer_img)
        self.fdialog.show()



    def display(self,path=None,im=None):
        for i in reversed(range(self.imgLayout.count())):
            self.imgLayout.itemAt(i).widget().setParent(None)
        try:
            if path:
                im = Image.open(self.path).convert('RGB') #lire image


            self.figure = Figure(tight_layout=True)
            self.canvas = FigureCanvas(self.figure)
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.imgLayout.addWidget(self.toolbar)
            self.imgLayout.addWidget(self.canvas)
            self.graph = self.figure.add_subplot(111)
            self.graph.imshow(im)
            self.graph.axis('off')
            self.graph.set_title('IMAGE')
        except:
            self.w=warning(str_warning="IMAGE NON DISPONIBLE !")
            self.w.show()
            


    def display_1(self,path=None,im=None,title=''):

        for i in reversed(range(self.plotLayout.count())):
            self.plotLayout.itemAt(i).widget().setParent(None)
        try:
            if path:
                self.im = Image.open(self.path).convert('RGB') #lire image


            self.figure = Figure(tight_layout=True)
            self.canvas = FigureCanvas(self.figure)
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.plotLayout.addWidget(self.toolbar)
            self.plotLayout.addWidget(self.canvas)
            self.graph = self.figure.add_subplot(111)
            self.graph.imshow(im)
            self.graph.axis('off')
            self.graph.set_title(title)
        except:
            self.w=warning(str_warning="IMAGE NON DISPONIBLE !")
            self.w.show()
            
    def convert_to_ng(self):
        try:
            
                
            self.hs=None
            self.hn=None
            self.hc=None
            self.hcn=None
            self.rev=None
            self.hr=None
            self.imt=None
            self.ht=None
            self.exp=None
            self.hexp=None
            self.heg=None
            self.eg=None
            self.img_bin=None
            self.med=None
            self.gauss=None
            self.taille=None
            self.sigma=None
            self.moy=None
            self.obj=None
            self.grad=None
            self.im = Image.open(self.path).convert('RGB') #lire image
            self.img=hop.convert(self.im) # convertire en NG
            for i in reversed(range(self.plotLayout.count())):
                self.plotLayout.itemAt(i).widget().setParent(None)
            self.display(None,self.img)
        except:
            self.w=warning(str_warning="IMAGE NON DISPONIBLE !")
            self.w.show()


    def display_plot(self,data,title=''):
        for i in reversed(range(self.plotLayout.count())):
            self.plotLayout.itemAt(i).widget().setParent(None)

        self.figure = Figure(tight_layout=True)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.plotLayout.addWidget(self.toolbar)
        self.plotLayout.addWidget(self.canvas)
        self.graph = self.figure.add_subplot(111)

        self.graph.set_title(title)
        self.graph.grid(color='#2A3459')
        self.graph.set_xlabel('INTENSITE')
        self.graph.set_ylabel('NOMBRE DE PIXELS')
        self.graph.plot(data[0], data[1],color='red',marker='o')
        datacursor(self.graph, hover=True, formatter='nombre : {y:0.0f}\n intensité : {x:0.0f}'.format, arrowprops=dict(arrowstyle='simple', fc='red', alpha=0.5),bbox=dict(fc='red'))

        mplcyberpunk.make_lines_glow(self.graph)
        mplcyberpunk.add_underglow(self.graph)
    def display_hs(self):
        try:
            
                
            self.hs=hop.histogramme_simple(self.img)
            data=(self.intensite,self.hs)
            self.display(None,self.img)
            self.display_plot(data,'HISTOGRAMME SIMPLE')



        except:
           pass 
           

    def display_hc(self):
        try:
            
                
            self.hc=hop.histogramme_cumule(self.hs)
            data=(self.intensite,self.hc)
            self.display_plot(data,'HISTOGRAMME CUMULE')
            self.display(None,self.img)
        except:
            pass
    def display_hn(self):

        try:
            
                
            self.hn=hop.histogramme_norm(self.img, self.hs)
            data=(self.intensite,self.hn)
            self.display_plot(data,'HISTOGRAMME NORMALISE')
            self.display(None,self.img)
        except:
            pass

    def display_hcn(self):
        try:
            
                
            self.hcn=hop.histogramme_norm(self.img, self.hc)
            data=(self.intensite,self.hcn)
            self.display_plot(data,'HISTOGRAMME CUMULE NORMALISE')
            self.display(None,self.img)
        except:
            pass        
    def inverser_hist(self):
        try:

            
                
            self.rev=hop.inverser_histo(self.img)
            self.hr=hop.histogramme_simple(self.rev)
            data=(self.intensite,self.hr)
            self.display_plot(data,'HISTOGRAMME INVERSE')
            self.display(None,self.img)


        except:
            pass



    @qtc.pyqtSlot(float, float)
    def translation_h(self,alpha, beta):
        try:
            
                
            self.alpha = alpha
            self.beta = beta
            self.imt=hop.translation(self.img,self.alpha,self.beta)
            self.ht=hop.histogramme_simple(self.img)
            data=(self.intensite,self.ht)
            self.display_plot(data,'TRANSLATION D\'HISTOGRAMME ')
            self.display(None,self.img)
        except:
            pass




    def get_params(self):
        
            
        self.dialog = Dialog()
        self.dialog.data.connect(self.translation_h)
        self.dialog.show()




    def exp_dyn(self):
        try:
            
                
            self.exp=hop.expansion_dyn(self.img)
            self.hexp=hop.histogramme_simple(self.exp)
            data=(self.intensite,self.hexp)
            self.display_plot(data,'HISTOGRAMME EXPANSION DYNAMIQUE')
            self.display(None,self.img)
        except:
            pass

    def egalisation_h(self):
        try:
            
                
            self.eg=hop.egalisation_hist(self.img,self.hcn)
            self.heg=hop.histogramme_simple(self.eg)
            data=(self.intensite,self.heg)
            self.display_plot(data,'HISTOGRAMME EGALISE')
            self.display(None,self.img)
        except:
            
            pass

       
            
    def binarisation(self):
        try:
            
                
            self.display(None,self.img)
            self.img_bin=seg.bin(self.img)
            self.display_1(None,self.img_bin,'IMAGE BINARISEE')
        except:
            pass

    def find_obj(self):
        try:
            
            for i in reversed(range(self.plotLayout.count())):
                self.plotLayout.itemAt(i).widget().setParent(None)
            for i in reversed(range(self.imgLayout.count())):
                self.imgLayout.itemAt(i).widget().setParent(None)
            self.display(None,self.img_bin)
            tmp=self.img_bin.convert('L')
            tmp=np.array(tmp)
            ccl=object_finder.CCL(tmp)
            self.obj=object_finder.generate_obj_color_img(ccl)
            self.display_1(None,self.obj,'OBJET')
                
        except:
            pass





    @qtc.pyqtSlot(int)
    def median(self,taille):
        try:
            
                

            self.taille=taille
            self.med=self.img.convert('L')
            self.med=f.median(self.med,self.taille)
            self.med=self.med.convert('RGB')
            self.display_1(None,self.med,'FILTRE MEDIAN')

        except:
            pass


    @qtc.pyqtSlot(int)
    def moyener(self,taille):
        try:
            
                
            self.taille=taille
            self.moy=self.img.convert('L')
            self.moy=f.moyener(self.moy,self.taille)
            self.moy=self.moy.convert('RGB')
            self.display_1(None,self.moy,'FILTRE MOYENER')

        except:
            pass

    def get_params_4(self):
        
            
        self.dialog2 = Dialog2()
        self.dialog2.data2.connect(self.moyener)
        self.dialog2.show()


    def get_params_2(self):
        
            
        self.dialog2 = Dialog2()
        self.dialog2.data2.connect(self.median)
        self.dialog2.show()


    @qtc.pyqtSlot(int,float)
    def gaussian (self,taille,sigma):
        try:
            
                
            self.taille=taille
            self.sigma=sigma
            self.gauss=self.img.convert('L')
            self.gauss=f.gaussian_apply(self.gauss,self.taille,self.sigma)
            self.gauss=self.gauss.convert('RGB')
            self.display_1(None,self.gauss,'FILTRE GAUSSIAN')
        except:
            pass

    def get_params_3(self):
        
            
        self.dialog3 = Dialog3()
        self.dialog3.data3.connect(self.gaussian)
        self.dialog3.show()

    @qtc.pyqtSlot(str)
    def importer_video(self,video):
        try:
            
                
            self.video=video
            if self.video:
                self.diff()
        except:
            pass

    def get_params_6(self):
        
            
        self.fdialog2 = file_dialog()
        self.fdialog2.data.connect(self.importer_video)
        self.fdialog2.show()

    def diff(self):
        
        try:
           self.dialog4 = Dialog4(self.video)
           self.dialog4.show()
        except:
            pass


    def prewitt(self):
        try:
            
                
            self.grad=None
            self.grad=self.img.convert('L')
            self.grad=g.apply_filter(self.grad,'P')
            self.grad=self.grad.convert('RGB')
            self.display_1(None,self.grad,'FILTRE PREWITT')
        except:
            pass

    def sobel(self):
        try:
            
                
            self.grad=None
            self.grad=self.img.convert('L')
            self.grad=g.apply_filter(self.grad,'S')
            self.grad=self.grad.convert('RGB')
            self.display_1(None,self.grad,'FILTRE SOBEL')
        except:
            pass


    def roberts(self):
        try:
            
                
            self.grad=None
            self.grad=self.img.convert('L')
            self.grad=g.apply_filter(self.grad,'R')
            self.grad=self.grad.convert('RGB')
            self.display_1(None,self.grad,'FILTRE ROBERTS')
        except:
            pass


    @qtc.pyqtSlot(int)
    def rotation(self,angle):
        try:
            self.img=self.img.convert('L')
            im_rot=geo.rotation(self.img,angle)
            rot= Image.fromarray(np.uint8(im_rot)).convert('RGB')
            self.display_1(None, rot, 'ROTATION')
        except:
            pass

    def get_params_7(self):
        self.dialog5 = Dialog5()
        self.dialog5.data.connect(self.rotation)
        self.dialog5.show()


    @qtc.pyqtSlot(int,int)
    def translation(self, alpha,beta):
        try:
            self.img = self.img.convert('L')
            im_tr = geo.translation(self.img,alpha,beta)
            tr = Image.fromarray(np.uint8(im_tr)).convert('RGB')
            self.display_1(None, tr, 'TRANSLATION')
        except:
            pass


    def get_params_8(self):
        self.dialog6 = Dialog6()
        self.dialog6.data.connect(self.translation)
        self.dialog6.show()


    @qtc.pyqtSlot(float)
    def resize_img(self, factor):
        try:

            self.img = self.img.convert('L')
            matplotlib.image.imsave('./resized_img/original.png', self.img,cmap='gray')
            im_resised = geo.rescale_img(self.img, factor)
            matplotlib.image.imsave('./resized_img/resized_img.png', im_resised, cmap='gray')
            res = Image.fromarray(np.uint8(im_resised)).convert('RGB')
            self.display_1(None, res, 'RESIZED_IMG'+str(res.size))

        except:
            pass


    def get_params_9(self):
        self.dialog7 = Dialog7()
        self.dialog7.data.connect(self.resize_img)
        self.dialog7.show()
        
    def somme(self):
        self.dialog8 = Dialog8()
        self.dialog8.show()
        
    

    def __init__(self):
        super(base_1,self).__init__()
        self.setupUi(self)
        
        self.btn_minimize.clicked.connect(self.minimize)
        self.btn_close.clicked.connect(self.close)
        self.pushButton_7.clicked.connect(self.get_params_5)
        self.pushButton_2.clicked.connect(self.convert_to_ng)
        self.pushButton_3.clicked.connect(self.display_hs)
        self.pushButton.clicked.connect(self.display_hc)
        self.pushButton_4.clicked.connect(self.display_hn)
        self.pushButton_5.clicked.connect(self.display_hcn)
        self.pushButton_12.clicked.connect(self. inverser_hist)
        self.pushButton_13.clicked.connect(self.exp_dyn)
        self.pushButton_14.clicked.connect(self.get_params)
        self.pushButton_15.clicked.connect(self.egalisation_h)
        self.pushButton_6.clicked.connect(self.binarisation)
        self.pushButton_8.clicked.connect(self.find_obj)
        self.pushButton_10.clicked.connect(self.get_params_2)
        self.pushButton_9.clicked.connect(self.get_params_3)
        self.pushButton_11.clicked.connect(self.get_params_4)
        self.pushButton_16.clicked.connect(self. get_params_6)
        self.pushButton_17.clicked.connect(self.prewitt)
        self.pushButton_18.clicked.connect(self.sobel)
        self.pushButton_19.clicked.connect(self.roberts)
        self.pushButton_20.clicked.connect(self.get_params_7)
        self.pushButton_21.clicked.connect(self.get_params_8)
        self.pushButton_22.clicked.connect(self.get_params_9)
        self.pushButton_23.clicked.connect(self.somme)
        
    def minimize(self):
        self.showMinimized()
    def closeEvent(self, event):
        event.ignore()
        self.q=quitter()
        self.q.show()
        
