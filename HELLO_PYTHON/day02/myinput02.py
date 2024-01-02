# 첫 수를 입력하시오 4
# 끝 수를 입력하시오 5
# 4와 5의 합은 9입니다.

fstnum = input("첫 수를 입력하시오 ")
scdnum = input("끝 수를 입력하시오 ")

arr = range(int(fstnum), int(scdnum)+1)

result = 0

for i in arr:
    result += i

print(fstnum +"와 " + scdnum + "의 합은 " + str(result) + "입니다.")
print("{}와 {}의 합은 {}입니다.".format(fstnum, scdnum, result))