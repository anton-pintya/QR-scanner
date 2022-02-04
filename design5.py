from PyQt5 import QtCore, QtGui, QtWidgets, Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("QR-code сканнер")
        MainWindow.resize(400, 400)
        MainWindow.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 400))
        self.centralwidget.setMaximumSize(QtCore.QSize(1000, 1000))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        
        self.image = QtWidgets.QLabel(self.centralwidget)
        self.image.setEnabled(True)
        self.image.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.image.setLineWidth(3)
        self.image.setText("")
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        
        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setReadOnly(True)
        self.label.setMinimumSize(QtCore.QSize(0, 25))
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        self.label.setStyleSheet("background-color: white;")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label.setFrameStyle(Qt.QFrame.Panel)
        self.verticalLayout.addWidget(self.label)
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setMinimumSize(QtCore.QSize(0, 56))
        self.horizontalGroupBox.setMaximumSize(QtCore.QSize(16777215, 56))
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalGroupBox.setTitle('Опции с сообщением')
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.open_button = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.open_button.setObjectName("open_button")
        self.horizontalLayout.addWidget(self.open_button)    
        self.copy_button = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.copy_button.setObjectName("copy_button")
        self.horizontalLayout.addWidget(self.copy_button)
        self.verticalLayout.addWidget(self.horizontalGroupBox)
        
        self.img_button = QtWidgets.QPushButton(self.centralwidget)
        self.img_button.setStyleSheet("")
        self.img_button.setObjectName("img_button")
        self.verticalLayout.addWidget(self.img_button)
        
        self.cam_button = QtWidgets.QPushButton(self.centralwidget)
        self.cam_button.setObjectName("cam_button")
        self.verticalLayout.addWidget(self.cam_button)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QR-code сканнер"))
        self.copy_button.setText(_translate("MainWindow", "Скопировать ссылку"))
        self.open_button.setText(_translate("MainWindow", "Открыть в браузере"))
        self.img_button.setText(_translate("MainWindow", "Выбрать файл"))
        self.cam_button.setText(_translate("MainWindow", "Считывать с камеры"))
