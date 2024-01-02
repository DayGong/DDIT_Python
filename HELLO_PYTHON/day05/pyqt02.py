#pyqt ui 불러오기 (8줄 정도 됨)
#우리 화면에서 Good Evening
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("pyqt02.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        num = self.le.text()
        res = int(num)-1
        self.le.setText( str(res) )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()