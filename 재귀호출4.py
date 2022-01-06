# 팩토리얼 구하기(10부터 1까지 곱하는 예)
# 반복문

factValue = 1 # 곱셈이므로 초기값 1로 설정
for n in range(10, 0, -1):
    factValue *= n
print("10*9*...*1 =", factValue)

def factorial(num):
    if num <= 1:
        return 1
    return num*factorial(num-1)

print('\n10!', factorial(10))

def factorial1(num1) :
    if num1 <= 1:
        print('1 반환')
        return 1
    print("%d * %d! 호출" % (num1, num1-1))
    retVal = factorial1(num1-1)

    print("%d * %d! 호출" % (num1, num1-1))
    return num1 * retVal

print('\n5! =', factorial1(5))