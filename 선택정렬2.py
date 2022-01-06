import random # random을 임포트 하고
## 함수
def selectionSort(ary) : # 함수의 정의
    n = len(ary) 
    for cy in range(0, n-1): # 사이클이 도는 횟수 : n개의 갯수를 n-1개 만큼 비교하면 됨
        minIdx = cy # 최소값을 바꿔줌
        for i in range(cy+1, n) :
            if (ary[minIdx] > ary[i]) :
                minIdx = i
        ary[cy], ary[minIdx] = ary[minIdx], ary[cy]
    return ary

## 전역
dataAry = [ random.randint(10,99) for _ in range(20)] # 전역변수로 20개의 랜덤데이터를 뽑는 배열을 생성
 
## 메인
print('정렬 전 -->', dataAry)
dataAry =selectionSort(dataAry)
print('정렬 후 -->', dataAry)