from random import random
# 나 : 홀
# 컴 : 홀 / 짝
# 결과 : 이김 / 짐

myChoice = input("나: ")
comChoice = ""
result = ""

comRandom = random();
if comRandom > 0.5:
    comChoice = "홀"
else:
    comChoice = "짝"

if myChoice == comChoice:
    result = "이김"
else:
    result = "짐"

print("컴: {}".format(comChoice))
print("결과: {}".format(result))