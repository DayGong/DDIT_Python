#pyqt ui 불러오기 (8줄 정도 됨)
#우리 화면에서 Good Evening
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt04.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        arr = list(range(1, 45+1))

        for i in range(1000):
            rnd = int(random()*45)
            tmp = arr[0]
            arr[0] = arr[rnd]
            arr[rnd] = tmp
            
        for i in range(6):
            for j in range(6):
                if arr[i] < arr[j]:
                    a = arr[i]
                    b = arr[j]
                    arr[i] = b
                    arr[j] = a
        
        self.pte1.setPlainText(str(arr[0]))
        self.pte2.setPlainText(str(arr[1]))
        self.pte3.setPlainText(str(arr[2]))
        self.pte4.setPlainText(str(arr[3]))
        self.pte5.setPlainText(str(arr[4]))
        self.pte6.setPlainText(str(arr[5]))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()