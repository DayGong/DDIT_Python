def showDan(dan):
    for i in range(1, 9+1):
        print("{} * {} = {}".format(dan, i, dan * i))

inDan = input("단을 입력하세요: ")
showDan(int(inDan))