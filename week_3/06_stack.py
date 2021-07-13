class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None 
    
    #push 기능 구현
    def push(self, value):
        new_head=Node(value) #새로운 머리 생성
        new_head.next=self.head # 새로운 머리가 기존 머리를 가르킴
        self.head=new_head
        return

    # pop 기능 구현
    def pop(self):
        delete_head = self.head # 제거할 node 를 변수에 잡습니다.
        self.head = self.head.next # 그리고 head 를 현재 head 의 다음 걸로 잡으면 됩니다.
        return delete_head

    # peek 기능 구현
    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None