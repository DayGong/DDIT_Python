#pyqt ui 불러오기 (8줄 정도 됨)
#우리 화면에서 Good Evening
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from random import random

form_class = uic.loadUiType("pyqt05.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def btnClick(self):
        mine = self.le_mine.text()
        com = ""
        result = ""
        
        com_rnd = random()
        
        if com_rnd > 0.66:
            com = "가위"
        elif com_rnd > 0.33:
            com = "바위"
        else:
            com = "보"
        
        if mine == "가위" and com == "가위" : result = "비김"
        if mine == "가위" and com == "바위" : result = "짐"
        if mine == "가위" and com == "보"  : result = "이김"
        
        if mine == "바위" and com == "가위"  : result = "이김"
        if mine == "바위" and com == "바위"  : result = "비김"
        if mine == "바위" and com == "보"  : result = "짐"
        
        if mine == "보" and com == "가위"  : result = "짐"
        if mine == "보" and com == "바위"  : result = "이김"
        if mine == "보" and com == "보"  : result = "비김"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()