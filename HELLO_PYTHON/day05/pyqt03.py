#pyqt ui 불러오기 (8줄 정도 됨)
#우리 화면에서 Good Evening
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("pyqt03.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        dan = self.le.text()
        idan = int(dan)
        
        res = ""
        for i in range(1, 9+1):
            res += "{} * {} = {}\n".format(idan, i, (idan * i))
        self.te.setText(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()