from random import random

def getHJ():
    HJ = random()
    ret = ""
    
    if HJ < 0.5:
        ret = "홀"
    else:
        ret = "짝"
 
    return ret;

mine = input("나: ")
com = getHJ()
result = ""

if mine == com:
    result = "이김"
else:
    result = "짐"
    
print("컴: ", com)
print("결과: ", result)