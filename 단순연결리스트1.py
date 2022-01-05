# 함수
class Node():
    def __init__(self):
        self.data = None
        self.Link = None

# 전역

# 메인
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.Link = node2

node3 = Node()
node3.data = "쯔위"
node2.Link = node3

node4 = Node()
node4.data = "사나"
node3.Link = node4

node5 = Node()
node5.data = "지효"
node4.Link = node5

# print(node1.data, end = ' ')
# print(node1.Link.data, end = ' ')
# print(node1.Link.Link.data, end = ' ')
# print(node1.Link.Link.Link.data, end = ' ')
# print(node1.Link.Link.Link.Link.data, end = ' ')
newNode =Node()
newNode.data = '재남'
newNode.Link = node2.Link
node2.Link = newNode

# 삭제
node2.Link = node3.Link
del(node3)

current = node1
print(current.data, end= ' ')
while current.Link != None :
    current = current.Link
    print(current.data, end=' ')


