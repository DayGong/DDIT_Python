import sys

from Cython.Compiler.Naming import self_cname
from PyQt5 import uic
from PyQt5.Qt import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt06.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb0.clicked.connect(self.numClick)
        self.pb1.clicked.connect(self.numClick)
        self.pb2.clicked.connect(self.numClick)
        self.pb3.clicked.connect(self.numClick)
        self.pb4.clicked.connect(self.numClick)
        self.pb5.clicked.connect(self.numClick)
        self.pb6.clicked.connect(self.numClick)
        self.pb7.clicked.connect(self.numClick)
        self.pb8.clicked.connect(self.numClick)
        self.pb9.clicked.connect(self.numClick)
        self.pb_call.clicked.connect(self.btnClick)
    
    def numClick(self):
        btnNum = self.sender().text()
        str_old = self.le.text()
        
        self.le.setText(str_old + btnNum)
        
    def btnClick(self):
        str_tel = self.le.text()
        QMessageBox.about(self,'전화걸기', str_tel)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()