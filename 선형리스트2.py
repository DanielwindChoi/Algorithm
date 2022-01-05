# 함수 선언 부분
def add_data(friend):

    katok.append(None)
    KLen = len(katok)
    katok[KLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    KLen = len(katok)
    for i in range(KLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i -1] = None
    katok[position] = friend
    
def delete_data(position) :
    katok[position] = None
    KLen =len(katok)
    for i in range(position+1, KLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    del(katok[KLen-1])

# 전역 변수 선언 부분
katok = []
select = -1

# 메인 코드 부분
if __name__ == "__main__":

    while(select != 4):

        select = int(input(1))

        if (select == 1):
            data = input()
            add_data(data)
            print(katok)
        elif (select == 2):
            data = input()
            add_data(data)
            print(katok)
        elif (select == 3):
            data = input()
            add_data(data)
            print(katok)
        elif (select == 4):
            print(katok)
            exit
        else :
            print("1~4 중 하나 입력하세요~")
            continue    