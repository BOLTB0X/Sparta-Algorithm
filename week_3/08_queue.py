class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # head -> tail
    # [4]  ->  [2]
    def enqueue(self, value): #맨 뒤에 데이터 추가하기            
        new_node = Node(value)
        if self.is_empty(): # 만약 비어있다면,
            self.head = new_node           # head 에 new_node를
            self.tail = new_node           # tail 에 new_node를 넣어준다.
            return

        self.tail.next = new_node          
        self.tail = new_node
        				           # 그리고 tail을 [3] 으로 지정합니다.
    def dequeue(self): #맨 위 데이터 빼기
        if self.is_empty():
            return "Queue is empty!"        # 만약 비어있다면 에러!

        delete_head = self.head             # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next          # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.

        return delete_head.data

    def peek(self): #맨 앞의 데이터 보기
        if self.is_empty():
            return "Queue is empty!"
    
        return self.head.data

    def is_empty(self): #큐가 비었는지 안 비었는지 여부 반환해주기
        return self.list.head is None