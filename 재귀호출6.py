## 별 모양 출력하기

# 재귀함수
print('재귀함수')
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)

printStar(5)

# 반복문
print('반복문')
n = 5
for i in range(n):
    for j in range(n):
        print("*")
        break