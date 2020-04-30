# -*- coding: utf-8 -*-

import numpy as np
import sys
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtWidgets import *
import qimage2ndarray

basic_ui = uic.loadUiType("Imageviewer.ui")[0]

fileName = ""
class WindowClass(QMainWindow, basic_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.Imageshow)
        self.pushButton_2.clicked.connect(self.Imageflip) 
        self.show()

    def Imageshow(self): 
        fileName, _ = QFileDialog.getOpenFileName(self, "Open File", ".")

        if fileName:
            self.image = QImage(fileName)

            if self.image.isNull(): 
                QMessageBox.information(self, "imageviewer", "Cannot load%s." % fileName)
                return

            qPixmapVar = QPixmap.fromImage(self.image) 
            qPixmapVar = qPixmapVar.scaled(256, 256)
            self.label.setPixmap(qPixmapVar)

               
    def Imageflip(self):
        
        image_array = qimage2ndarray.rgb_view(self.image)
        image_array = np.flip(image_array, 0)
        self.image = qimage2ndarray.array2qimage(image_array, normalize=False) 

        qPixmapVar1 = QPixmap.fromImage(self.image)
        qPixmapVar1 = qPixmapVar1.scaled(256, 256)
        self.label.setPixmap(qPixmapVar1)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
