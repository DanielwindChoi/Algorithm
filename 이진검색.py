# 이진검색도 실무에서 많이 쓸 수 있다. 내부수익률 구하는 거랑 똑같네.
import random
## 이진검색
## 함수, 클래스
def binSearch(ary, fData) :
    pos = -1 # 포지션 의미
    start = 0
    end = len(ary)-1

    while start <= end :
        mid = (start + end) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return pos 

## 전역
dataAry = [ random.randint(10,999) for _ in range(50)]
findData = dataAry[random.randint(0,49)]
dataAry.sort()

## 메인
print('배열 -->', dataAry)
position = binSearch(dataAry, findData)
if position == -1 :
    print(findData, '없어요ㅠㅠ')
else :
    print(findData, '는', position, '위치에 있어요')