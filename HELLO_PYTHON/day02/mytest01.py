# 첫 수를 입력하시오 1
# 끝 수를 입력하시오 4
# 1에서 4까지의 합은 10입니다.

fstnum = input("첫 수를 입력하시오 ")
scdnum = input("끝 수를 입력하시오 ")

arr = range(int(fstnum), int(scdnum)+1)

result = 0

for i in arr:
    result += i

print("{}와 {}의 합은 {}입니다.".format(fstnum, scdnum, result))