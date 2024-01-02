class Musk:
    def __init__(self):
        self.cnt_stock = 100
        
    def straw(self):
        self.cnt_stock += 1
        
class JDragon:
    def __init__(self):
        self.money = 400
        
    def buyPhone(self, cnt):
        self.money += cnt
        
class SugarBoy:
    def __init__(self):
        self.cnt_chain = 1200
        
    def paper(self):
        self.cnt_chain += 1
        
class Chowon(Musk, JDragon, SugarBoy):
    def __init__(self):
        Musk.__init__(self)
        JDragon.__init__(self)
        SugarBoy.__init__(self)
        
if __name__ == '__main__':
    cho = Chowon()
    print("초원이 주식:", cho.cnt_stock)
    print("초원이 돈:", cho.money)
    print("초원이 체인점:", cho.cnt_chain)
    cho.straw()
    cho.buyPhone(100)
    cho.paper()
    print("초원이 주식:", cho.cnt_stock)
    print("초원이 돈:", cho.money)
    print("초원이 체인점:", cho.cnt_chain)