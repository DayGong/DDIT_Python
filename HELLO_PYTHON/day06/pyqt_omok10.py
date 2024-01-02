import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QRect, QSize
from Cython.Compiler.Naming import self_cname

form_class = uic.loadUiType("pyqt_omok10.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.flag_bw = True
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                btn = QPushButton(self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setIconSize(QSize(40, 40))
                btn.setGeometry(QRect(40*i, 40*j, 40, 40))
                btn.clicked.connect(self.mydol)
        
        self.show()
        
        self.pb.clicked.connect(self.myclick)
            
    def mydol(self):
        if self.flag_bw:
            self.sender().setIcon(QtGui.QIcon("1.png"))
        else:
            self.sender().setIcon(QtGui.QIcon("2.png"))
        
        self.flag_bw = not self.flag_bw
        
    def myclick(self):
        print("reset")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()