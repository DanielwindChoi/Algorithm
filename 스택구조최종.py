## 함수 선언 부분 ##
def isStackFull() :
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else :
        return False

        ## 함수 선언 부분 ##
def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

def push(data) :
    global SIZE,stack, top
    if (isStackFull()):
        print("스택 꽉!")
        return
    top += 1
    stack[top]=data