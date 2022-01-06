## 재귀호출
def addNumber(num) :
    if num <= 1 :
        return 1
    return num + addNumber(num-1)
print(addNumber(10))

# 반복문
sumValue = 0
for n in range(10, 0, -1):
    sumValue += n
print("10=9+...+1=", sumValue)