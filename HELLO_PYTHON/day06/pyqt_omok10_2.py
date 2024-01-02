import sys

from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QRect, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow


form_class = uic.loadUiType("pyqt_omok10_2.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.arr2d = [
            [1,0,0,0,0 ,0,0,0,0,0],
            [1,2,2,0,0 ,0,0,0,0,0],
            [0,1,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0]
        ]
        self.arr_pb = []
        
        self.flag_bw = True
        self.setupUi(self)
        
        for i in range(10):
            for j in range(10):
                imsi = QPushButton(self)
                imsi.setIcon(QtGui.QIcon("0.png"))
                imsi.setIconSize(QSize(40, 40))
                imsi.setGeometry(QRect(40*j, 40*i, 40, 40))
                imsi.clicked.connect(self.myturn)
                self.arr_pb.append(imsi)
        
        self.show()
        self.myrender()
        
        self.pb.clicked.connect(self.myclick)
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.arr_pb[i*10+j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2d[i][j] == 1:
                    self.arr_pb[i*10+j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.arr_pb[i*10+j].setIcon(QtGui.QIcon("2.png"))
    
    def myturn(self):
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