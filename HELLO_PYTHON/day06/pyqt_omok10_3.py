import sys

from PyQt5 import uic, QtGui
from PyQt5.Qt import QPushButton, QRect, QSize, QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow
from Cython.Compiler.Naming import self_cname


form_class = uic.loadUiType("pyqt_omok10_3.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.arr2d = [
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0],
            [0,0,0,0,0 ,0,0,0,0,0]
        ]
        self.arr2b = []
        
        self.flag_bw = True
        self.flag_over = False
        self.setupUi(self)
        
        for i in range(10):
            line = []
            for j in range(10):
                imsi = QPushButton(self)
                imsi.setIcon(QtGui.QIcon("0.png"))
                imsi.setIconSize(QSize(40, 40))
                imsi.setGeometry(QRect(40*j, 40*i, 40, 40))
                imsi.clicked.connect(self.myturn)
                imsi.setToolTip("{},{}".format(i, j))
                line.append(imsi)
        
            self.arr2b.append(line)
            
        self.pb.clicked.connect(self.myreset)
        self.show()
        self.myrender()
        
    
    def myrender(self):
        for i in range(10):
            for j in range(10):
                if self.arr2d[i][j] == 0:
                    self.arr2b[i][j].setIcon(QtGui.QIcon("0.png"))
                if self.arr2d[i][j] == 1:
                    self.arr2b[i][j].setIcon(QtGui.QIcon("1.png"))
                if self.arr2d[i][j] == 2:
                    self.arr2b[i][j].setIcon(QtGui.QIcon("2.png"))
    
    def getDR(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                j += 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getDL(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                j -= 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getUR(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                j += 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getUL(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                j -= 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
    
    def getRI(self, i, j, stone):
        ret = 0
        try:
            while True:
                j += 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
    
    def getLE(self, i, j, stone):
        ret = 0
        try:
            while True:
                j -= 1
                
                if i < 0:
                    return ret
                
                if j < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
        
    def getUP(self, i, j, stone):
        ret = 0
        try:
            while True:
                i -= 1
                
                if i < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret

    def getDW(self, i, j, stone):
        ret = 0
        try:
            while True:
                i += 1
                
                if i < 0:
                    return ret
                
                if self.arr2d[i][j] == stone :
                    ret += 1
                else :
                    return ret
        except:
            return ret
            
    def myturn(self):
        if self.flag_over:
            return
        
        str_ij = self.sender().toolTip()
        arr_ij = str_ij.split(",")
        i = int(arr_ij[0])
        j = int(arr_ij[1])
        
        if self.arr2d[i][j] > 0:
            return
        
        stone = -1
        if self.flag_bw:
            self.arr2d[i][j] = 1
            stone = 1
        else:
            self.arr2d[i][j] = 2
            stone = 2
            
        up = self.getUP(i, j, stone)
        dw = self.getDW(i, j, stone)
        le = self.getLE(i, j, stone)
        ri = self.getRI(i, j, stone)
        ul = self.getUL(i, j, stone)
        ur = self.getUR(i, j, stone)
        dl = self.getDL(i, j, stone)
        dr = self.getDR(i, j, stone)
        
        d1 = up + dw + 1
        d2 = ul + dr + 1
        d3 = le + ri + 1
        d4 = dl + ur + 1
        
        self.myrender()
        
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5:
            self.flag_over = True
            if self.flag_bw:
                QMessageBox.about(self,'게임 종료', '흑돌 승리');
            else:
                QMessageBox.about(self,'게임 종료', '백돌 승리');
        
        self.flag_bw = not self.flag_bw
        
    def myreset(self):
        for i in range(10):
            for j in range(10):
                self.arr2d[i][j] = 0
                
        self.myrender()
        self.flag_bw = True
        self.flag_over = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    app.exec_()