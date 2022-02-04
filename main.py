import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QClipboard
import design5

from pyzbar.pyzbar import decode
from PIL import Image
from cv2 import cv2
import numpy as np
import webbrowser

class QRdecoder(QtWidgets.QMainWindow, design5.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.img_button.clicked.connect(self.browse_folder)
        self.cam_button.clicked.connect(self.camera_scan)
        self.copy_button.clicked.connect(self.copy_link)
        self.open_button.clicked.connect(self.open_link)
    
    def scanning(self, directory):
        img = Image.open(directory)
        decodedObject = decode(img)
        data = decodedObject[0].data
        self.label.setText(str(data, 'utf-8'))
        self.label.setAlignment(Qt.AlignCenter)
      
    def browse_folder(self, image):
        try:
            directory = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите изображение", '/home')[0]
            pixmap = QPixmap(directory)
            width = self.image.width()
            height = self.image.height()
            self.image.setPixmap(pixmap.scaled(width, height, Qt.KeepAspectRatio))
            self.image.setAlignment(Qt.AlignCenter)
            self.scanning(directory)
        except:
            self.label.setText('Сначала выберите подходящий файл')
            self.label.setAlignment(Qt.AlignCenter)
    
    def copy_link(self, label):
        link = QApplication.clipboard()
        link.clear(mode=link.Clipboard)
        link.setText(self.label.toPlainText(), mode=link.Clipboard)

    def open_link(self, label):
        text = self.label.toPlainText()
        if text and text != 'Сначала выберите подходящий файл':
            try:
                webbrowser.open(str(self.label.toPlainText()), new=2)
            except:
                pass
            
    def camera_scan(self, image):
        for i in range(5):
            camera = cv2.VideoCapture(i)
            if camera:
                break
        while True:
            _, frame = camera.read()
            decodedObject = decode(frame)
            if len(decodedObject) > 0:
                self.label.setText(str(decodedObject[0].data, 'utf-8'))
                del(camera)
                cv2.destroyAllWindows()
                break
            cv2.imshow('Press ESC to close window', frame)
            key = cv2.waitKey(1)
            if key == 27:
                del(camera)
                cv2.destroyAllWindows()
                break

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QRdecoder() 
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()