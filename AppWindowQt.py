# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QLabel, QMainWindow
from AppGuiFunctions import GuiFunctions
import sys


class QLabel_alterada(QLabel):
    clicked = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()

class Window2(QMainWindow):

    def __init__(self, width, height, file_path):
        super().__init__()
        self.width = width
        self.height = height
        self.file_path = file_path
        self.setupUi()

    def setupUi(self):
        self.setObjectName("MainWindow2")
        self.resize(self.width, self.height)
        
        self.postprocess_photo = QLabel(self)
        self.postprocess_photo.setGeometry(QtCore.QRect(0, 0, self.width, self.height))        
        font = QtGui.QFont()
        font.setPointSize(11)        
        self.postprocess_photo.setFont(font)
        self.postprocess_photo.setAutoFillBackground(True)
        self.postprocess_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.postprocess_photo.setObjectName("postprocess_photo")
        self.postprocess_photo.setPixmap(QtGui.QPixmap(self.file_path))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow2", "Processed Image"))



class Ui_MainWindow(object):

    def __init__(self):
        self.working_path = "processimage/inputresizedimage.jpg"
        self.displayoutput = "processimage/postprocessresized.jpg"
        self.gui_functions = GuiFunctions()
        self.imgwidth = 401
        self.imgheight = 401
        self.accepted_extensions = set(["PNG", "png", "jpg", "jpeg"])
        self.file_has_been_loaded = False
        self.photo_has_been_processed = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.chosen_photo = QLabel_alterada(self.centralwidget)
        self.chosen_photo.setGeometry(QtCore.QRect(0, 0, 401, 401))        
        font = QtGui.QFont()
        font.setPointSize(11)        
        self.chosen_photo.setFont(font)
        self.chosen_photo.setAutoFillBackground(True)
        self.chosen_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.chosen_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.chosen_photo.setObjectName("chosen_photo")
        self.chosen_photo.clicked.connect(lambda: self.openFileDialogBox())         
        
        self.processed_photo = QLabel_alterada(self.centralwidget)
        self.processed_photo.setGeometry(QtCore.QRect(400, 0, 401, 401))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.processed_photo.setFont(font)
        self.processed_photo.setAutoFillBackground(True)
        self.processed_photo.setFrameShape(QtWidgets.QFrame.Box)
        self.processed_photo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.processed_photo.setAlignment(QtCore.Qt.AlignCenter)
        self.processed_photo.setObjectName("processed_photo")
        self.processed_photo.clicked.connect(lambda: self.openExtraWindow()) 
        
        self.wdsrbx4 = QtWidgets.QPushButton(self.centralwidget)
        self.wdsrbx4.setGeometry(QtCore.QRect(0, 410, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.wdsrbx4.setFont(font)
        self.wdsrbx4.setObjectName("wdsrbx4")
        self.wdsrbx4.clicked.connect(lambda: self.processImage("wdsr-b-finetunedx4"))
        
        self.srganx4 = QtWidgets.QPushButton(self.centralwidget)
        self.srganx4.setGeometry(QtCore.QRect(400, 410, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.srganx4.setFont(font)
        self.srganx4.setObjectName("srganx4")
        self.srganx4.clicked.connect(lambda: self.processImage("srganx4"))
        
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(330, 500, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(lambda: self.saveFileDialogBox())
        
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
        self.actionSave.triggered.connect(lambda: self.saveFileDialogBox())
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Enhancer"))
        
        self.chosen_photo.setText(_translate("MainWindow", "Click Here To Add Image"))
        self.chosen_photo.setStatusTip(_translate("MainWindow", "Click Click Click Click..."))

        self.processed_photo.setText(_translate("MainWindow", "Click Here to View Your UpScaled Image"))
        self.processed_photo.setStatusTip(_translate("MainWindow", "Click Here to View Your UpScaled Image More Closely..."))

        self.wdsrbx4.setText(_translate("MainWindow", "WDSR B x4"))
        self.wdsrbx4.setStatusTip(_translate("MainWindow", "This Will Take Some Time..."))
        self.srganx4.setText(_translate("MainWindow", "SRGAN x4"))
        self.srganx4.setStatusTip(_translate("MainWindow", "This Will Take Some Time..."))
        self.saveButton.setText(_translate("MainWindow", "Save Image"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setStatusTip(_translate("MainWindow", "Open New File"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Save the upscaled image"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))

    def processImage(self, model):
        if not self.file_has_been_loaded :
            self.showNoFilePopup()
        else :
            successRes = self.gui_functions.superresUpscaler(model)
            if successRes :
                self.processed_photo.setPixmap(QtGui.QPixmap("processimage/downscaled_finalprocessedimage_" + model + ".jpg"))
                self.photo_has_been_processed = True
            else :
                self.showFatalPopup()

    def displayChosenImage(self):
        self.chosen_photo.setPixmap(QtGui.QPixmap(self.working_path))
    
    def openExtraWindow(self):
        if self.photo_has_been_processed :
            self.dialog = Window2(self.gui_functions.imgrealwidth , self.gui_functions.imgrealheight, self.gui_functions.finaloutputpath)
            self.dialog.show()
        else :
            self.showNoUpscalingDonePopup()

    def openFileDialogBox(self):
        file_path = QFileDialog.getOpenFileName()[0]
        extension = file_path.split('.')[-1] ##Use this for checking filetype and throwing errors and stuff
        
        if extension in self.accepted_extensions :
            self.gui_functions.openFile(file_path, self.imgwidth, self.imgheight)
            self.file_has_been_loaded = True
            self.displayChosenImage()

            self.processed_photo.setText(QtCore.QCoreApplication.translate("MainWindow", "Click Here to View Your UpScaled Image"))
            self.photo_has_been_processed = False
        elif extension == "" :
            pass
        else :
            self.showExtensionsMismatchPopup(extension)

    def saveFileDialogBox(self):
        if not self.file_has_been_loaded :
            self.showNoFilePopup()
        else :
            file_path = QFileDialog.getSaveFileName()[0]
            extension = file_path.split('.')[-1] ##Use this for checking filetype and throwing errors and stuff

            if extension == file_path :
                file_path = file_path + ".jpg"
                self.gui_functions.saveFile(file_path)
            else :
                self.gui_functions.saveFile(file_path)

    def showNoFilePopup(self):
        popmsg = QMessageBox()
        popmsg.setWindowTitle("Image Enhancer Alert")
        popmsg.setText("Please open a file first :)")
        popmsg.setIcon(QMessageBox.Critical)

        x = popmsg.exec_()

    def showNoUpscalingDonePopup(self):
        popmsg = QMessageBox()
        popmsg.setWindowTitle("Image Enhancer Alert")
        popmsg.setText("Please choose an Image UpScaling Algorithm First !")
        popmsg.setIcon(QMessageBox.Critical)

        x = popmsg.exec_()

    def showExtensionsMismatchPopup(self, extension):
        popmsg = QMessageBox()
        popmsg.setWindowTitle("Image Enhancer Alert")
        popmsg.setText("." + extension + " is currently not supported !")
        popmsg.setIcon(QMessageBox.Critical)

        popmsg.setDetailedText(str(self.accepted_extensions) + " are the supported extensions")

        x = popmsg.exec_()

    def showFatalPopup(self):
        popmsg = QMessageBox()
        popmsg.setWindowTitle("Image Enhancer Fatal Alert")
        popmsg.setText("Image UpScaling with chosen Algorithm encountered a fatal error !")
        popmsg.setIcon(QMessageBox.Critical)

        x = popmsg.exec_()

    def execute(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        sys.exit(app.exec_())