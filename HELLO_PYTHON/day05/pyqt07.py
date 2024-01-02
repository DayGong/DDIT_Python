import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic

form_class = uic.loadUiType("pyqt07.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.btnClick)
        
    def getStar(self, num):
        ret = ""
        for i in range(num):
            ret += "*"
        ret += "\n"
        return ret
            
    def btnClick(self):
        first = self.le_first.text()
        last = self.le_last.text()
        
        ifirst = int(first)
        ilast = int(last)
        
        result = ""
        
        for i in range(ifirst, ilast+1):
            result += self.getStar(i)
        
        self.pte.setPlainText(result)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()