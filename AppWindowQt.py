# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from AppGuiFunctions import GuiFunctions
import sys

class Ui_MainWindow(object):

    def __init__(self):
        self.working_path = "processimage.jpg"
        self.gui_functions = GuiFunctions()
        self.imgwidth = 401
        self.imgheight = 401
        self.accepted_extensions = set(["PNG", "png", "jpg", "jpeg"])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.chosen_photo = QtWidgets.QLabel(self.centralwidget)
        self.chosen_photo.setGeometry(QtCore.QRect(0, 0, 401, 401))        
        font = QtGui.QFont()
        font.setPointSize(11)        
        self.chosen_photo.setFont(font)
        self.chosen_photo.setAutoFillBackground(True)
        self.chosen_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.chosen_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_photo.setObjectName("chosen_photo")
        
        self.processed_photo = QtWidgets.QLabel(self.centralwidget)
        self.processed_photo.setGeometry(QtCore.QRect(400, 0, 401, 401))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.processed_photo.setFont(font)
        self.processed_photo.setAutoFillBackground(True)
        self.processed_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.processed_photo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.processed_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.processed_photo.setObjectName("processed_photo")
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(0, 410, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button1.setFont(font)
        self.button1.setObjectName("button1")
        
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(400, 410, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.button2.setFont(font)
        self.button2.setObjectName("button2")
        
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(330, 500, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionNew.triggered.connect(lambda: self.openFileDialogBox())
        
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Enhancer"))
        self.chosen_photo.setText(_translate("MainWindow", "Click Here To Add Image"))
        self.processed_photo.setText(_translate("MainWindow", "Your UpScaled Image"))
        self.button1.setText(_translate("MainWindow", "SRGAN x2"))
        self.button2.setText(_translate("MainWindow", "SRGAN x4"))
        self.saveButton.setText(_translate("MainWindow", "Save Image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the upscaled image"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def displayChosenImage(self):
        self.chosen_photo.setPixmap(QtGui.QPixmap(self.working_path))
    
    def openFileDialogBox(self):
        file_path = QFileDialog.getOpenFileName()[0]
        extension = file_path.split('.')[-1] ##Use this for checking filetype and throwing errors and stuff
        
        if extension in self.accepted_extensions :
            self.gui_functions.openFile(file_path, self.imgwidth, self.imgheight)
            self.displayChosenImage()
        else :
            self.showExtensionsMismatchPopup(extension)

    def showExtensionsMismatchPopup(self, extension):
        popmsg = QMessageBox()
        popmsg.setWindowTitle("Image Enhancer Alert")
        popmsg.setText("." + extension + " is currently not supported !")
        popmsg.setIcon(QMessageBox.Critical)

        x = popmsg.exec_()

    def main(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

if __name__ == "__main__":
    obj = Ui_MainWindow()
    obj.main()