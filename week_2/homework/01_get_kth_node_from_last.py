class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        length = 1 # 시작 노드의 길이를 세기 위해 1부터 시작합니다
        cur = self.head
        while cur.next is not None: #cur옆이 비어있을때 까지
            cur = cur.next 
            length+=1 #길이 증가
        end_length = length - k #길이-k가 원하는 값에 앞에서 부터 위치
        cur = self.head #앞에서 부터 찾기 위한 재정의
        for i in range(end_length):
            cur = cur.next
        return cur

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!