import sys

from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("pyqt_omok.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        
        self.lbl.mousePressEvent = self.yourclick
        
    def yourclick(self, event):
        self.lbl.setPixmap(QtGui.QPixmap("1.png"))
            
    def myclick(self):
        self.pb.setIcon(QtGui.QIcon("1.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()