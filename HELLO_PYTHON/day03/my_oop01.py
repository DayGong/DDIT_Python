class Animal:
    def __init__(self):
        self.iq = 50
    
    def training(self, cnt):
        self.iq += cnt    

class Human(Animal):
    def __init__(self):
        super().__init__()
        self.cnt_lang = 0
    
    def momstouch(self, stroke):
        self.cnt_lang += stroke
    
hum = Human()
print("iq:", hum.iq)
print("cnt_lang:", hum.cnt_lang)
hum.training(30)
hum.momstouch(30)
print("iq:", hum.iq)
print("cnt_lang:", hum.cnt_lang)