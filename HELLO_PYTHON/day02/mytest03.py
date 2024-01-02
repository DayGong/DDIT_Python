# 출력할 단수를 입력하시오 5
# 5 * 1 = 5
# 5 * 2 = 10

dan = input("출력할 단수를 입력하시오 ")
idan = int(dan)

for i in range(1, 9+1):
    print("{} * {} = {}".format(idan, i, idan * i))