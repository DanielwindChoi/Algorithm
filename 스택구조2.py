## 함수
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

def push(data):
    global SIZE, stack, top
    if (isStackFull()==True):
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

def isStackEmpty() :
    global SIZE, stack, top
    if (top <= -1) :
        return
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()) :
        print('스택 텅~')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() : # 다음에 들어올 값을 먼저 보는것
    if (isStackEmpty()) :
        print('스택 텅~')
        return None
    return stack[top]


## 전역
SIZE = 5
stack = [ None for _ in range(SIZE)]
top = -1

## 메인
# stack = ['커피', '녹치', '꿀물', '콜라', '환타']
# top = 4

# stack = ['커피', '녹치', '꿀물', '콜라', 'None']
# top = 3

# push('보리차')
# print(stack)
# push('사이다')
# print(stack)

# print(isStackFull())

# stack = ['커피', 'None', 'None', 'None', 'None']
# top = 0

print('다음 나올 예정:', peek)
print(pop())
print(pop())